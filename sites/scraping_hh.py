import re
from datetime import datetime
import pandas as pd
import requests
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
class HHGetInformation:

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
            link = f'https://hh.ru/search/vacancy?text={word}&from=suggest_post&salary=&schedule=remote&no_magic=true&ored_clusters=true&enable_snippets=true&search_period=1&excluded_text='
            await self.bot.send_message(self.chat_id, link, disable_web_page_preview=True)

            print('page link: ', link)
            try:
                self.browser.get(link)
            except Exception as e:
                print('bot could not to get the link', e)

            try:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except:
                pass
            await self.get_link_message(self.browser.page_source, word)

            till = 13
            for self.page_number in range(1, till):
                try:
                    await self.bot.send_message(self.chat_id, f'https://hh.ru/search/vacancy?text={word}&from=suggest_post&salary=&schedule=remote&no_magic=true&ored_clusters=true&enable_snippets=true&search_period=1&excluded_text=&page={self.page_number}&hhtmFrom=vacancy_search_list',
                                          disable_web_page_preview=True)
                    self.browser.get(f'https://hh.ru/search/vacancy?text={word}&from=suggest_post&salary=&schedule=remote&no_magic=true&ored_clusters=true&enable_snippets=true&search_period=1&excluded_text=&page={self.page_number}&hhtmFrom=vacancy_search_list')
                    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    vacancy_exists_on_page = await self.get_link_message(self.browser.page_source, word)
                    if not vacancy_exists_on_page:
                        break
                except:
                    break
        await self.bot.send_message(self.chat_id, 'hh.ru parsing: Done!', disable_web_page_preview=True)

    async def get_link_message(self, raw_content, word):

        links = []
        soup = BeautifulSoup(raw_content, 'lxml')

        list_links = soup.find_all('a', class_='serp-item__title')
        if list_links:
            print(f'\nПо слову {word} найдено {len(list_links)} вакансий\n')
            self.current_message = await self.bot.send_message(self.chat_id, f'hh.ru:\nПо слову {word} найдено {len(list_links)} вакансий на странице {self.page_number+1}', disable_web_page_preview=True)

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
        convert = {
            'января': '01',
            'февраля': '02',
            'марта': '03',
            'апреля': '04',
            'мая': '05',
            'июня': '06',
            'июля': '07',
            'августа': '08',
            'сентября': '09',
            'октября': '10',
            'ноября': '11',
            'декабря': '12',
        }

        date = date.split(f'\xa0')
        month = date[1]
        day = date[0]
        year = date[2]

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

    async def get_content_from_link(self, i, links, word):
        vacancy_url = i.get('href')
        vacancy_url = re.findall(r'https:\/\/hh.ru\/vacancy\/[0-9]{6,12}', vacancy_url)[0]
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
        vacancy = soup.find('div', class_='vacancy-title').find('span').get_text()
        print('vacancy = ', vacancy)

        # get title --------------------------
        title = vacancy
        print('title = ',title)

        # get body --------------------------
        body = soup.find('div', class_='vacancy-section').get_text()
        body = body.replace('\n\n', '\n')
        body = re.sub(r'\<[A-Za-z\/=\"\-\>\s\._\<]{1,}\>', " ", body)
        print('body = ',body)

        # get tags --------------------------
        tags = ''
        try:
            tags_list = soup.find('div', class_="bloko-tag-list")
            for i in tags_list:
                tags += f'{i.get_text()}, '
            tags = tags[0:-2]
        except:
            pass
        print('tags = ',tags)

        english = ''
        if re.findall(r'[Аа]нглийский', tags) or re.findall(r'[Ee]nglish', tags):
            english = 'English'

        # get city --------------------------
        try:
            city = soup.find('a', class_='bloko-link bloko-link_kind-tertiary bloko-link_disable-visited').get_text()
        except:
            city = ''
        print('city = ',city)

        # get company --------------------------
        try:
            company = soup.find('span', class_='vacancy-company-name').get_text()
            company = company.replace('\xa0', ' ')
        except:
            company = ''
        print('company = ',company)

        # get salary --------------------------
        try:
            salary = soup.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').get_text()
        except:
            salary = ''
        print('salary = ',salary)

        # get experience --------------------------
        try:
            experience = soup.find('p', class_='vacancy-description-list-item').find('span').get_text()
        except:
            experience = ''
        print('experience = ',experience)

        # get job type and remote --------------------------
        raw_content_2 = soup.findAll('p', class_='vacancy-description-list-item')
        counter = 1
        job_type = ''
        for value in raw_content_2:
            match counter:
                case 1:
                    experience = value.find('span').get_text()
                case 2:
                    job_type = str(value.get_text())
                    print(value.get_text())
                case 3:
                    print(value.get_text())
                    job_type += f'\n{value.get_text}'
            counter += 1
        job_type = re.sub(r'\<[a-zA-Z\s\.\-\'"=!\<_\/]+\>', " ", job_type)

        if re.findall(r'удаленная работа', job_type):
            remote = True

        contacts = ''

        try:
            date = soup.find('p', class_="vacancy-creation-time-redesigned").get_text()
        except:
            date = ''
        if date:
            date = re.findall(r'[0-9]{1,2}\W[а-я]{3,}\W[0-9]{4}', date)
            date = date[0]
            date = self.normalize_date(date)
        print('date = ', date)

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
            'chat_name': 'https://hh.ru/',
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
        profession = response_from_db['profession']
        response_from_db = response_from_db['response_from_db']
        if response_from_db:
            additional_message = f'-exists in db\n'
            self.rejected_vacancies += 1

        elif not response_from_db and 'no_sort' not in profession['profession']:
            prof_str = ''
            for j in profession['profession']:
                prof_str += f"{j}, "
            prof_str = prof_str[:-2]
            additional_message = f"<b>+w: {prof_str}</b>\n" \
                                 f"tags: {profession['tag']}\n" \
                                 f"anti_tags: {profession['anti_tag']}"
            self.written_vacancies += 1

        else:
            # additional_message = f'(no_sort)\n'
            prof_str = ''
            for j in profession['profession']:
                prof_str += f"{j}, "
            prof_str = prof_str[:-2]
            additional_message = f"<b>+w: {prof_str}</b>\n" \
                                 f"tags: {profession['tag']}\n" \
                                 f"anti_tags: {profession['anti_tag']}"
            # self.rejected_vacancies += 1
            self.written_vacancies += 1


        if len(f"{self.current_message}\n{self.count_message_in_one_channel}. {vacancy}\n{additional_message}")< 4096:
            self.current_message = await self.bot.edit_message_text(
                f'{self.current_message.text}\n{self.count_message_in_one_channel}. {vacancy}\n{additional_message}',
                self.current_message.chat.id,
                self.current_message.message_id,
                parse_mode='html',
                disable_web_page_preview=True
            )
            pass
        else:
            self.current_message = await self.bot.send_message(self.chat_id, f"{self.count_message_in_one_channel}. {vacancy}\n{additional_message}")
            pass
        print(f"\n{self.count_message_in_one_channel} from_channel hh.ru search {word}")
        self.count_message_in_one_channel += 1
# loop = asyncio.new_event_loop()
# loop.run_until_complete(HHGetInformation(bot_dict={}).get_content())


