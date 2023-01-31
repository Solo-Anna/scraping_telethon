import re
import time
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
# from _apps.scraping_push_to_channels import PushChannels
from db_operations.scraping_db import DataBaseOperations
from __backup__.pattern_Alex2809 import cities_pattern, params


class AngelGetInformation:

    def __init__(self, bot_dict):

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
        self.search_words = ['pm',]

        self.extended = ['game', 'product', 'mobile', 'marketing', 'sales_manager', 'analyst',
                             'frontend', 'designer', 'devops', 'hr', 'backend', 'qa', 'junior', 'ba']

        # self.search_words.extend(self.extended)
        self.current_message = None
        # self._apps = bot_dict['_apps']
        # self.chat_id = bot_dict['chat_id']


    async def get_content(self, db_tables=None):
        """
        If DB_tables = 'all', that it will push to all DB include professions.
        If None (default), that will push in all_messages only
        :param count_message_in_one_channel:
        :param db_tables:
        :return:
        """
        self.db_tables = db_tables

        self.count_message_in_one_channel = 1

        self.options = Options()
        # self.options.add_argument("--headless")
        # self.options.add_argument("--disable-dev-shm-usage")
        # self.options.add_argument("--no-sandbox")

        # await self._apps.send_message(self.chat_id, 'https://angel.co/ is starting', disable_web_page_preview=True)

        link = 'https://angel.co/jobs/'
        response_dict = await self.get_info(link)

        return response_dict

    async def get_info(self, link):

        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)



        pass



        for word in self.search_words:

            self.current_message = await self.bot.send_message(self.chat_id, f'Поиск вакансий по слову {word}...')

            self.browser.get('http://hh.ru')
            time.sleep(1)

            holder = self.browser.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/div[1]/div/div/div[2]/div/form/div/div[1]/fieldset/input")
            holder.send_keys(word)
            time.sleep(1)
            button_find = self.browser.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/div[1]/div/div/div[2]/div/form/div/div[2]/button")
            button_find.click()

            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            # response_dict = await self.get_link_message(self.browser.page_source, word)
            await self.get_link_message(self.browser.page_source, word)


            # for key in response_dict:
            #     full_response_dict[key].extend(response_dict[key])
            #
            # pass

        self.browser.quit()
        return self.to_write_excel_dict

    async def get_link_message(self, raw_content, word):
        message_dict ={}
        results_dict = {}
        to_write_excel_dict = {
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

        base_url = 'https://hh.ru'
        links = []
        soup = BeautifulSoup(raw_content, 'lxml')
        # self.browser.quit()

        list_links = soup.find_all('a', class_='serp-item__title')
        print(f'\nПо слову {word} найдено {len(list_links)} вакансий\n')

        self.current_message = await self.bot.edit_message_text(
            f'{self.current_message.text}\nПо слову {word} найдено {len(list_links)} вакансий\n\n',
            self.current_message.chat.id,
            self.current_message.message_id)
        # --------------------- LOOP -------------------------
        for i in list_links:
            vacancy_url = i.get('href')
            vacancy_url = re.findall(r'https:\/\/hh.ru\/vacancy\/[0-9]{6,12}', vacancy_url)[0]
            print('vacancy_url = ', vacancy_url)
            links.append(vacancy_url)

            self.browser.get(vacancy_url)
            time.sleep(2)
            try:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except Exception as e:
                print('Screen did not scroll: ', e)

            soup = BeautifulSoup(self.browser.page_source, 'lxml')


            # get vacancy ------------------------
            vacancy = soup.find('div', class_='vacancy-title').find('span').get_text()
            print('vacancy = ', vacancy)

            # get title --------------------------
            title = vacancy
            print('title = ',title)

            # get body --------------------------
            body = soup.find('div', class_='vacancy-section').get_text()
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
            # # get contacts by click --------------------------
            # button = self.browser.find_element(By.XPATH,
            #                                    "//button[@class='bloko-button bloko-button_kind-success bloko-button_scale-large bloko-button_stretched bloko-button_appearance-outlined']")
            # button.click()
            # time.sleep(2)
            # soup_contacts = BeautifulSoup(self.browser.page_source, 'lxml')
            # contacts = soup_contacts.find('div', class_='contacts__item').get_text()
            # print('contacts = ', contacts)




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

            # ------------------- compose title and body ------------------------------------

            self.to_write_excel_dict['chat_name'].append('https://hh.ru/')
            self.to_write_excel_dict['title'].append(title)
            self.to_write_excel_dict['body'].append(body)
            self.to_write_excel_dict['vacancy'].append(vacancy)
            self.to_write_excel_dict['vacancy_url'].append(vacancy_url)
            self.to_write_excel_dict['company'].append(company)
            self.to_write_excel_dict['company_link'].append('')
            self.to_write_excel_dict['english'].append(english)
            self.to_write_excel_dict['relocation'].append(relocation)
            self.to_write_excel_dict['job_type'].append(job_type)
            self.to_write_excel_dict['city'].append(city)
            self.to_write_excel_dict['salary'].append(salary)
            self.to_write_excel_dict['experience'].append('')
            self.to_write_excel_dict['time_of_public'].append(date)
            self.to_write_excel_dict['contacts'].append(contacts)

            # results_dict['chat_name'] = 'geek_jobs.ru'
            # results_dict['title'] = title
            # results_dict['body'] = body
            # results_dict['time_of_public'] = date
            # message_dict['message'] = f'{title}\n{body}'
            self.current_message = await self.bot.edit_message_text(
                f'{self.current_message.text}\n{self.count_message_in_one_channel}. {vacancy}\n',
                self.current_message.chat.id,
                self.current_message.message_id)

            print(f"\n{self.count_message_in_one_channel} from_channel hh.ru search {word}")
            self.count_message_in_one_channel += 1
            print('time_sleep')
            # time.sleep(random.randrange(10, 15))

        print('Prepare to write to excel')
        # df = pd.DataFrame(
        #     {
        #         'title': to_write_excel_dict['title'],
        #         'body': to_write_excel_dict['body'],
        #         'vacancy': to_write_excel_dict['vacancy'],
        #         'vacancy_url': to_write_excel_dict['vacancy_url'],
        #         'company': to_write_excel_dict['company'],
        #         'english': to_write_excel_dict['english'],
        #         'relocation': to_write_excel_dict['relocation'],
        #         'job_type': to_write_excel_dict['job_type'],
        #         'city': to_write_excel_dict['city'],
        #         'salary': to_write_excel_dict['salary'],
        #         'experience': to_write_excel_dict['experience'],
        #         'time_of_public': to_write_excel_dict['time_of_public'],
        #         'contacts': to_write_excel_dict['contacts'],
        #     }
        # )

        # df.to_excel(f'./../excel/hh_{word}.xlsx', sheet_name='Sheet1')
        print('Has written to Excel')

        self.current_message = await self.bot.send_message(
            self.chat_id,
            f'\nMessages are writting to Admin table, please wait a few time ...\n'
        )

        return to_write_excel_dict

    # def normalize(self, date):
    #     text = str(text)
    #     text = text.replace('<div id="vacancy-description">', '')
    #     text = text.replace('<br>', f'\n').replace('<br/>', '')
    #     text = text.replace('<p>', f'\n').replace('</p>', '')
    #     text = text.replace('<li>', f'\n\t- ').replace('</li>', '')
    #     text = text.replace('<strong>', '').replace('</strong>', '')
    #     text = text.replace('<div>', '').replace('</div>', '')
    #     text = text.replace('<h4>', f'\n').replace('</h4>', '')
    #     text = text.replace('<ul>', '').replace('</ul>', '')
    #     text = text.replace('<i>', '').replace('</i>', '')
    #     text = text.replace('<ol>', '').replace('</ol>', '')
    #     text = text.replace('\u200b', '')
    #     text = re.sub(r'<[\W\w\d]{1,10}>', '', text)
    #
    #     return text

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

# loop = asyncio.new_event_loop()
# loop.run_until_complete(HHGetInformation().get_content())

