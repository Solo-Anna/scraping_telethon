import re
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from db_operations.scraping_db import DataBaseOperations
from sites.write_each_vacancy_to_db import write_each_vacancy
from settings.browser_settings import options, chrome_driver_path
from utils.additional_variables.additional_variables import sites_search_words
from helper_functions.helper_functions import edit_message, send_message

class SvyaziGetInformation:

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
        self.main_url = 'https://www.svyazi.app'


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

    async def get_info(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            await self.bot.send_message(self.chat_id, f'https://www.svyazi.app/jobs',
                                  disable_web_page_preview=True)
            self.browser.get(f'https://www.svyazi.app/jobs')
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            vacancy_exists_on_page = await self.get_link_message(self.browser.page_source)
            # if not vacancy_exists_on_page:
            #     break
        except:
            pass
        await self.bot.send_message(self.chat_id, 'www.svyazi.app parsing: Done!', disable_web_page_preview=True)
        self.browser.quit()

    async def get_link_message(self, raw_content):

        links = []
        soup = BeautifulSoup(raw_content, 'lxml')

        list_links = soup.find_all('div', role='listitem')
        if list_links:
            print(f'\nНайдено {len(list_links)} вакансий\n')
            self.current_message = await self.bot.send_message(self.chat_id, f'www.svyazi.app:\nНайдено {len(list_links)} вакансий', disable_web_page_preview=True)

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

    def normalize_date(self, date):
        convert = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12',
        }

        date = date.split(f' ')
        month = date[1]
        day = date[0]

        year = datetime.now().strftime('%Y')
        date = datetime(int(year), int(convert[month]), int(day), 12, 00, 00)

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
        vacancy = soup.find('h2', class_='heading-2').get_text()
        print('vacancy = ', vacancy)

        # get title --------------------------
        title = vacancy
        print('title = ',title)

        # get body --------------------------
        body = soup.find('div', class_='jobs_overview').get_text()
        body = body.replace('\n\n', '\n')
        body = re.sub(r'\<[A-Za-z\/=\"\-\>\s\._\<]{1,}\>', " ", body)
        print('body = ',body)

        # get tags --------------------------
        # level = ''
        # try:
        #     level = soup.find('div', class_='category').get_text()
        # except:
        #     pass
        #
        tags = ''
        tags_list = []
        try:
            tags = soup.find('div', class_='levels-div')
        except:
            pass
        print('tags = ',tags)
        tags_list = re.findall(r'>[^\n=">]+<', str(tags))
        tags = ''
        for tag in tags_list:
            tags += f"#{tag[1:-1]}, "
        tags = tags[:-2]
        print(tags)

        body = f'{body}\n{tags}'

        english = ''
        if re.findall(r'[Аа]нглийский', tags) or re.findall(r'[Ee]nglish', tags):
            english = 'English'

        # get city --------------------------
        job_type = soup.find('div', class_='div-block-3')
        print('city_and_salary = ', job_type)
        job_type_list = re.findall(r'>[^\n=">]+<', str(job_type))
        job_type = ''
        for tag in job_type_list:
            job_type += f"{tag[1:-1].replace(',', '')}, "
        job_type = job_type[:-2]

        print('city_and_salary = ', job_type)

        # try:
        #     city = soup.find('div', class_='location').get_text()
        # except:
        #     city = ''
        # print('city = ',city)

        # get company --------------------------
        try:
            company = soup.find('h6', class_='heading-6').get_text()
        except:
            company = ''
        print('company = ',company)

        # get salary --------------------------
        salary = ''
        # try:
        #     salary = soup.find('div', class_='jobinfo').find('span', class_='salary').get_text()
        # except:
        #     salary = ''
        # print('salary = ',salary)

        # get experience --------------------------
        # job_format = soup.find('div', class_='jobinfo').find('span', class_='jobformat').get_text()
        #
        # print('job_format = ', job_format)

        contacts = ''

        try:
            date = soup.find('p', class_="subtitle").get_text()
        except:
            date = ''
        if date:
            date = self.normalize_date(date)
        print('date = ', date)

        # ------------------------- search relocation ----------------------------
        relocation = ''
        if re.findall(r'[Рр]елокация', body):
            relocation = 'релокация'

        # ------------------------- search city ----------------------------
        city = ''
        # for key in cities_pattern:
        #     for item in cities_pattern[key]:
        #         match = re.findall(rf"{item}", body)
        #         if match and key != 'others':
        #             for i in match:
        #                 city += f"{i} "

        # ------------------------- search english ----------------------------
        # english_additional = ''
        # for item in params['english_level']:
        #     match1 = re.findall(rf"{item}", body)
        #     match2 = re.findall(rf"{item}", tags)
        #     if match1:
        #         for i in match1:
        #             english_additional += f"{i} "
        #     if match2:
        #         for i in match2:
        #             english_additional += f"{i} "
        #
        # if english and ('upper' in english_additional or 'b1' in english_additional or 'b2' in english_additional \
        #         or 'internediate' in english_additional or 'pre' in english_additional):
        #     english = english_additional
        # elif not english and english_additional:
        #     english = english_additional

        DataBaseOperations(None).write_to_db_companies([company])

        #-------------------- compose one writting for ione vacancy ----------------

        results_dict = {
            'chat_name': 'https://svyazi.app/',
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
            'salary':salary,
            'experience': '',
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

        print(f"\n{self.count_message_in_one_channel} from_channel hh.ru search {word}")
        self.count_message_in_one_channel += 1

# loop = asyncio.new_event_loop()
# loop.run_until_complete(HHGetInformation(bot_dict={}).get_content())


