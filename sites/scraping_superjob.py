import re
from datetime import datetime, timedelta
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from db_operations.scraping_db import DataBaseOperations
from __backup__.pattern_Alex2809 import params
from sites.write_each_vacancy_to_db import write_each_vacancy
from settings.browser_settings import options
from sites.sites_additional_utils.get_structure import get_structure
from utils.additional_variables.additional_variables import sites_search_words
from helper_functions.helper_functions import edit_message, send_message

class SuperJobGetInformation:

    def __init__(self, bot_dict, search_word=None):

        self.db_tables = None
        self.options = None
        self.page = None
        self.to_write_excel_dict = {
            'chat_name': [],
            'title': [],
            'body': [],
            'vacancy': [],
            'vacancy_url': [],
            'company': [],
            'company_link': [],
            'english': [],
            'relocation': [],
            'job_type': [],
            'city': [],
            'salary': [],
            'experience': [],
            'time_of_public': [],
            'contacts': []
        }
        if not search_word:
            self.search_words = sites_search_words
        else:
            self.search_words=[search_word]
        self.page_number = 1

        self.current_message = None
        self.msg = None
        self.written_vacancies = 0
        self.rejected_vacancies = 0
        if bot_dict:
            self.bot = bot_dict['bot']
            self.chat_id = bot_dict['chat_id']
        self.browser = None
        self.main_url = 'https://russia.superjob.ru'


    async def get_content(self, db_tables=None):
        """
        If DB_tables = 'all', that it will push to all DB include professions.
        If None (default), that will push in all_messages only
        :param count_message_in_one_channel:
        :param db_tables:
        :return:
        """
        # self.browser.delete_all_cookies()
        # print('all cookies have deleted')
        self.db_tables = db_tables

        self.count_message_in_one_channel = 1

        await self.get_info()
        self.browser.quit()

    async def get_info(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        for word in self.search_words:
            self.page_number = 0
            till = 13
            for self.page_number in range(1, till):
                try:
                    await self.bot.send_message(self.chat_id, f'https://www.superjob.ru/vacancy/search/?keywords={word}&remote_work_binary=0&geo%5Bc%5D%5B0%5D=1&noGeo=1&page={self.page_number}',
                                          disable_web_page_preview=True)
                    self.browser.get(f'https://www.superjob.ru/vacancy/search/?keywords={word}&remote_work_binary=0&geo%5Bc%5D%5B0%5D=1&noGeo=1&page={self.page_number}')
                    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    vacancy_exists_on_page = await self.get_link_message(self.browser.page_source, word)
                    if not vacancy_exists_on_page:
                        break
                except:
                    break
        await self.bot.send_message(self.chat_id, 'superjob.ru parsing: Done!', disable_web_page_preview=True)

    async def get_link_message(self, raw_content, word):

        links = []
        soup = BeautifulSoup(raw_content, 'lxml')

        list_links = soup.find_all('div', class_='f-test-search-result-item')
        if list_links:
            print(f'\nПо слову {word} найдено {len(list_links)} вакансий\n')
            self.current_message = await self.bot.send_message(self.chat_id, f'superjob.ru:\nПо слову {word} найдено {len(list_links)} вакансий на странице {self.page_number}', disable_web_page_preview=True)

            # -------------------- check what is current session --------------

            current_session = DataBaseOperations(None).get_all_from_db(
                table_name='current_session',
                param='ORDER BY id DESC LIMIT 1',
                without_sort=True,
                order=None,
                field='session',
                curs=None
            )
            for value in current_session:
                self.current_session = value[0]

            # --------------------- LOOP -------------------------
            self.written_vacancies = 0
            self.rejected_vacancies = 0

            for i in list_links:
                await self.get_content_from_link(i, links, word)

            #----------------------- the statistics output ---------------------------
            self.written_vacancies = 0
            self.rejected_vacancies = 0
            return True
        else:
            return False

    def normalize_date(self, date):
        date_today = datetime.now().strftime('%d')
        month = datetime.now().strftime('%m')
        year = datetime.now().strftime('%Y')
        hour = datetime.now().strftime('%H')
        minutes = datetime.now().strftime('%M')

        if ':' in date:
            date = date.split(':')
            hour = date[0]
            minutes = date[1]
        if 'вчера' in date:
            date_today = date_today - timedelta(days=1)
            hour = 12
            minutes = 00

        date = datetime(int(year), int(month), int(date_today), int(hour), int(minutes), 00)

        return date

    def clean_company_name(self, text):
        text = re.sub('Прямой работодатель', '', text)
        text = re.sub(r'[(]{1} [a-zA-Z0-9\W\.]{1,30} [)]{1}', '', text)
        text = re.sub(r'Аккаунт зарегистрирован с (публичной почты|email) \*@[a-z.]*[, не email компании!]{0,1}', '', text)
        text = text.replace(f'\n', '')
        return text

    async def write_to_db_table_companies(self):
        excel_data_df = pd.read_excel('all_geek.xlsx', sheet_name='Sheet1')
        companies = excel_data_df['hiring'].tolist()
        links = excel_data_df['access_hash'].tolist()

        companies = set(companies)

        db=DataBaseOperations(con=None)
        db.write_to_db_companies(companies)

    async def get_content_from_link(self, i, links, word):
        vacancy_url = i.find('span', class_='_2s70W _31udi _7mW5l _17ECX _1B2ot _3EXZS _3pAka ofdOE').find('a').get('href')
        vacancy_url = f"{self.main_url}{vacancy_url}"
        print('vacancy_url = ', vacancy_url)
        links.append(vacancy_url)

        print('self.broswer.get(vacancy_url)')
        # await self.bot.send_message(self.chat_id, vacancy_url, disable_web_page_preview=True)
        # self.browser = browser
        self.browser.get(vacancy_url)
        # self.browser.get('https://google.com')
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        print('soup = BeautifulSoup(self.browser.page_source, \'lxml\')')
        soup = BeautifulSoup(self.browser.page_source, 'lxml')
        print('passed soup = BeautifulSoup(self.browser.page_source, \'lxml\')')

        # get vacancy ------------------------
        vacancy = soup.find('h1', class_='_2s70W _2sfSN _1qivw _17ECX _1B2ot _3EXZS ofdOE').get_text()
        print('vacancy = ', vacancy)

        # get title --------------------------
        title = vacancy
        print('title = ',title)

        # get body --------------------------
        body = 'Описание вакансии:\n'
        body_content = soup.find('span', class_='_39I1Z _1G5lt _3EXZS _3pAka _3GChV _2GgYH').find('span')
        print(body_content)
        structure = await get_structure(body_content)
        body_content_list_p = body_content.find_all('p')
        body_content_list_ul = body_content.find_all('ul')
        for element in structure:
            if element == 'p':
                try:
                    temp = body_content_list_p[0].get_text()
                    body += f"\n{temp}\n"
                    # print('\n', temp)
                    body_content_list_p.pop(0)
                except:
                    break
            if element == 'ul':
                if body_content_list_ul:
                    temp = body_content_list_ul[0]
                    for li in temp:
                        if li.text != ' ' and li.text:
                            try:
                                body += f"-{li.get_text()}\n"
                                # print('-', li.get_text())
                            except:
                                break
                    body_content_list_ul.pop(0)

        print('body = ', body)

        # get tags --------------------------
        tags = ''
        try:
            # div[class =_3ULio] ul[class] span[role=button]
            content = soup.find('div', class_='_2Zt8G _2-ptM _14Gd3 -woq8')
            tags_list = content.find('div', class_='_1hmM6 oC346').find_all('span', role='button')
            for i in tags_list:
                tags += f'{i.get_text()}, '
            tags = tags[0:-2]
        except:
            pass
        print('tags = ',tags)
        body = f"{body}\nПрофессиональные навыки:\n{tags}"

        content = soup.find('div', class_='_2zPWM _2s70W _2sfSN _1qivw _17ECX _1yHIx _1Qy3a _1GAZu')
        salary = ''
        try:
            salary = content.find('span', class_='_4Gt5t _3Kq5N').get_text()
        except:
            pass
        experience = ''
        job_type = ''
        experience_list = content.find_all('span', class_='_4maqB _3EXZS _3GChV')
        for element in experience_list:
            if 'пыт работы' in element.text or 'занятость' in element.text:
                experience += f"{element.text}, "
        if experience:
            job_type = experience[:-2]
        print('job_type = ', job_type)

        city = ''
        try:
            city = content.find('span', class_='_4maqB _3EXZS _3GChV').get_text()
        except:
            pass
        print('city = ', city)

        english = ''
        if re.findall(r'[Аа]нглийский', tags) or re.findall(r'[Ee]nglish', tags):
            english = 'English'

        # get city --------------------------
        # try:
        #     city = soup.find('a', class_='bloko-link bloko-link_kind-tertiary bloko-link_disable-visited').get_text()
        # except:
        #     city = ''
        # print('city = ',city)

        # get company --------------------------
        try:
            company = soup.find('div', class_='_2zPWM _1KDZn _2sfSN _7mW5l _17ECX _2refD _3QGKD tp1pf dEawn _1yHIx I2gCw').\
                find('span', class_='_1WrFk _3EXZS _3pAka _3GChV').get_text()
        except:
            company = ''
        print('company = ',company)

        contacts = ''

        try:
            date = soup.find_all('span', class_="_1G5lt _3EXZS ZZHii _3GChV")[1].get_text()
        except:
            date = ''
        if date:

            date = self.normalize_date(date)
        else:
            date = datetime.now()
        print('date = ', date)

        # ------------------------- search relocation ----------------------------
        relocation = ''
        if re.findall(r'[Рр]елокация', body):
            relocation = 'релокация'

        # ------------------------- search city ----------------------------
        # city = ''
        # for key in cities_pattern:
        #     for item in cities_pattern[key]:
        #         match = re.findall(rf"{item}", body)
        #         if match and key != 'others':
        #             for i in match:
        #                 city += f"{i} "

        # ------------------------- search english ----------------------------
        english_additional = ''
        for item in params['english_level']:
            match1 = re.findall(rf"{item}", body)
            match2 = re.findall(rf"{item}", tags)
            if match1:
                for i in match1:
                    english_additional += f"{i} "
            if match2:
                for i in match2:
                    english_additional += f"{i} "

        if english and ('upper' in english_additional or 'b1' in english_additional or 'b2' in english_additional \
                or 'internediate' in english_additional or 'pre' in english_additional):
            english = english_additional
        elif not english and english_additional:
            english = english_additional

        DataBaseOperations(None).write_to_db_companies([company])

        #-------------------- compose one writting for ione vacancy ----------------

        results_dict = {
            'chat_name': 'https://superjob.ru/',
            'title': title,
            'body': body,
            'vacancy': vacancy,
            'vacancy_url': vacancy_url,
            'company': company,
            'company_link': '',
            'english': english,
            'relocation': relocation,
            'job_type': job_type,
            'city':city,
            'salary':salary,
            'experience':'',
            'time_of_public':date,
            'contacts':contacts,
            'session': self.current_session
        }

        response_from_db = write_each_vacancy(results_dict)

        await self.output_logs(
            response_from_db=response_from_db,
            vacancy=vacancy,
            vacancy_url=vacancy_url
        )

    async def output_logs(self, response_from_db, vacancy, word=None, vacancy_url=None):

        additional_message = ''
        profession = response_from_db['profession']
        response_from_db = response_from_db['response_from_db']

        if response_from_db:
            additional_message = f'-exists in db\n'
            self.rejected_vacancies += 1

        elif not response_from_db:
            prof_str = ", ".join(profession['profession'])
            additional_message = f"<b>+w: {prof_str}</b>\n{vacancy_url}\n{profession['tag']}\n{profession['anti_tag']}\n"

            if 'no_sort' not in profession['profession']:
                self.written_vacancies += 1
            else:
                self.written_vacancies += 1

        if len(f"{self.current_message}\n{self.count_message_in_one_channel}. {vacancy}\n{additional_message}") < 4096:
            new_text = f"\n{self.count_message_in_one_channel}. {vacancy}\n{additional_message}"

            self.current_message = await edit_message(
                bot=self.bot,
                text=new_text,
                msg=self.current_message
            )

        else:
            new_text = f"{self.count_message_in_one_channel}. {vacancy}\n{additional_message}"
            self.current_message = await send_message(
                bot=self.bot,
                chat_id=self.chat_id,
                text=new_text
            )

            # self.current_message = await self.bot.send_message(self.chat_id,
            #                                                    f"{self.count_message_in_one_channel}. {vacancy}\n{additional_message}")

        print(f"\n{self.count_message_in_one_channel} from_channel hh.ru search {word}")
        self.count_message_in_one_channel += 1

# loop = asyncio.new_event_loop()
# loop.run_until_complete(HHGetInformation(bot_dict={}).get_content())