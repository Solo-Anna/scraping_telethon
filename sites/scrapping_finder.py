import re
from datetime import datetime, timedelta
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from db_operations.scraping_db import DataBaseOperations
from patterns.pattern_Alex2809 import cities_pattern, params
from sites.write_each_vacancy_to_db import write_each_vacancy
from settings.browser_settings import options, chrome_driver_path
from utils.additional_variables.additional_variables import sites_search_words
from helper_functions.helper_functions import edit_message, send_message

class FinderGetInformation:

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
        self.url_main = 'https://finder.vc'


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

        till = 13
        for self.page_number in range(1, till):
            try:
                await self.bot.send_message(self.chat_id, f'https://finder.vc/vacancies?category=1&page={self.page_number}',
                                      disable_web_page_preview=True)
                self.browser.get(f'https://finder.vc/vacancies?category=1&page={self.page_number}')
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                vacancy_exists_on_page = await self.get_link_message(self.browser.page_source)
                if not vacancy_exists_on_page:
                    break
            except:
                break
        await self.bot.send_message(self.chat_id, 'finder.vc parsing: Done!', disable_web_page_preview=True)

    async def get_link_message(self, raw_content):

        links = []
        soup = BeautifulSoup(raw_content, 'lxml')

        list_links = soup.find_all('div', class_='vacancies-page__card')
        if list_links:
            print(f'\nНайдено {len(list_links)} вакансий\n')
            self.current_message = await self.bot.send_message(self.chat_id, f'finder.vc:\nНайдено {len(list_links)} вакансий на странице {self.page_number}', disable_web_page_preview=True)

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
                await self.get_content_from_link(i, links)

            #----------------------- the statistics output ---------------------------
            self.written_vacancies = 0
            self.rejected_vacancies = 0
            return True
        else:
            return False

    def normalize_text(self, text):
        text = str(text)
        text = text.replace('<div id="vacancy-description">', '')
        text = text.replace('<br>', f'\n').replace('<br/>', '')
        text = text.replace('<p>', f'\n').replace('</p>', '')
        text = text.replace('<li>', f'\n\t- ').replace('</li>', '')
        text = text.replace('<strong>', '').replace('</strong>', '')
        text = text.replace('<div>', '').replace('</div>', '')
        text = text.replace('<h4>', f'\n').replace('</h4>', '')
        text = text.replace('<ul>', '').replace('</ul>', '')
        text = text.replace('<i>', '').replace('</i>', '')
        text = text.replace('<ol>', '').replace('</ol>', '')

        return text

    def convert_date(self, date):
        date = date.split(' ')
        if date[1] == 'сегодня':
            date = datetime.now()
        elif date[1] == 'вчера':
            date  = datetime.now()-timedelta(days=1)
        elif date[1] == 'неделю':
            date = datetime.now()-timedelta(days=7)
        elif re.findall(r'д[е]{0,1}н[ьейя]{1,2}', date[2]):
            date = datetime.now()-timedelta(days=int(date[1]))
        elif re.findall(r'месяц[ева]{0,2}', date[2]):
            date = datetime.now() - timedelta(days=int(date[1]*30))
        return date


    def clean_company_name(self, text):
        text = re.sub('Прямой работодатель', '', text)
        text = re.sub(r'[(]{1} [a-zA-Z0-9\W\.]{1,30} [)]{1}', '', text)
        text = re.sub(r'Аккаунт зарегистрирован с (публичной почты|email) \*@[a-z.]*[, не email компании!]{0,1}', '', text)
        text = text.replace(f'\n', '')
        return text

    async def compose_in_one_file(self):
        hiring = []
        link = []
        contacts = []

        for i in range(1, 48):
            excel_data_df = pd.read_excel(f'./../messages/geek{i}.xlsx', sheet_name='Sheet1')

            hiring.extend(excel_data_df['hiring'].tolist())
            link.extend(excel_data_df['hiring_link'].tolist())
            contacts.extend(excel_data_df['contacts'].tolist())

        df = pd.DataFrame(
            {
            'hiring': hiring,
            'access_hash': link,
            'contacts': contacts,
            }
        )

        df.to_excel(f'all_geek.xlsx', sheet_name='Sheet1')

    async def write_to_db_table_companies(self):
        excel_data_df = pd.read_excel('all_geek.xlsx', sheet_name='Sheet1')
        companies = excel_data_df['hiring'].tolist()
        links = excel_data_df['access_hash'].tolist()

        companies = set(companies)

        db=DataBaseOperations(con=None)
        db.write_to_db_companies(companies)

    async def get_content_from_link(self, i, links):
        vacancy_url = i.find('a').get('href')
        vacancy_url = self.url_main + vacancy_url
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
        try:
            vacancy = soup.find('h1', class_='vacancy-info-header__title').get_text()
        except:
            vacancy = ''
        print('title = ', vacancy)

        # get title --------------------------
        title = vacancy
        print('title = ',title)

        # get body --------------------------
        try:
            body = soup.find('div', class_='vacancy-info-body__description').get_text()
        except:
            body = ''

        try:
            body_list = soup.find_all('div', class_="vacancy-info-body__info")
        except:
            body_list = []

        if body_list:
            body += '\n'
            for content in body_list:
                body += f"{content.find('div', class_='vacancy-info-body__title').get_text()}\n"
                temporary_body_list = content.find_all('li', class_='vacancy-info-body__item')
                for li in temporary_body_list:
                    body += f"- {li.get_text()}\n"

        print('body = ', body)
        #
        # # get tags --------------------------
        # try:
        #     description = soup.find('div', class_='vacancy-info-body__lists').get_text()
        # except:
        #     description = ''
        # print('requirements = ', description)

        # try:
        #     terms = soup.find('ul', class_="vacancy-info-body__list").get_text()
        # except:
        #     terms = ''
        # print('terms = ', terms)

        try:
            company = soup.find('a', class_='link').get_text()
        except:
            company = ''
        print('company = ', company)

        try:
            job_type = soup.find('div', class_="employment-label__text").get_text()
            # body = f'\nГрафик работы: {time_job}\n' + body
        except:
            job_type = ''
        print('job_type = ', job_type)

        try:
            salary = soup.find('div', class_='row-wrapper vacancy-info-header__row').get_text()
            # experience = soup.find('div', class_='vacancy-info-header__row')
            experience = ''

        except:
            salary = ''
            experience = ''
        print('salary = ', salary)
        print('experience = ', experience)

        time_of_public = soup.find('div', class_='vacancy-info-header__publication-date').get_text()
        print('time_of_public = ', time_of_public)
        time_of_public = self.convert_date(time_of_public)
        print('time_of_public after = ', time_of_public)

        contacts = ''

        # try:
        #     date = soup.find('p', class_="vacancy-creation-time-redesigned").get_text()
        # except:
        #     date = ''
        # if date:
        #     date = re.findall(r'[0-9]{1,2}\W[а-я]{3,}\W[0-9]{4}', date)
        #     date = date[0]
        #     date = self.normalize_date(date)
        # print('date = ', date)

        # body = f""
        # ------------------------- search relocation ----------------------------
        relocation = ''
        if re.findall(r'[Рр]елокация', body):
            relocation = 'релокация'

        # ------------------------- search city ----------------------------
        city = ''
        for key in cities_pattern:
            for item in cities_pattern[key]:
                match = re.findall(rf"{item}", body)
                if match and key != 'others':
                    for i in match:
                        city += f"{i} "

        # ------------------------- search english ----------------------------
        english = ''
        for item in params['english_level']:
            match = re.findall(rf"{item}", body)
            if match:
                for i in match:
                    english += f"{i} "

        english_additional = ''
        for item in params['english_level']:
            match1 = re.findall(rf"{item}", body)
            match2 = re.findall(rf"{item}", title)
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
            'chat_name': 'https://finder.vc/',
            'title': title,
            'body': body,
            'vacancy': vacancy,
            'vacancy_url': vacancy_url,
            'company': company,
            'company_link': '',
            'english': english,
            'relocation': relocation,
            'job_type': job_type,
            'city': city,
            'salary': salary,
            'experience': experience,
            'time_of_public': time_of_public,
            'contacts': contacts,
            'session': self.current_session
        }

        response_from_db = write_each_vacancy(results_dict)

        await self.output_logs(
            response_from_db=response_from_db,
            vacancy=vacancy
        )

    async def output_logs(self, response_from_db, vacancy, word=None):

        additional_message = ''
        profession = response_from_db['profession']
        response_from_db = response_from_db['response_from_db']

        if response_from_db:
            additional_message = f'-exists in db\n'
            self.rejected_vacancies += 1

        elif not response_from_db:
            prof_str = ", ".join(profession['profession'])
            additional_message = f"<b>+w: {prof_str}</b>\n"

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

            # self.current_message = await self.bot.edit_message_text(
            #     f'{self.current_message.text}{new_text}',
            #     self.current_message.chat.id,
            #     self.current_message.message_id,
            #     parse_mode='html',
            #     disable_web_page_preview=True
            # )
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



