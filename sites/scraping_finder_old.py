import asyncio
import os
from datetime import datetime, timedelta
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
from patterns.pattern_Alex2809 import cities_pattern, params


class FindJobGetInformation:

    def __init__(self, bot_dict):
        self.base_url = 'https://finder.vc'
        self.browser = None
        self.current_message = None
        self.bot = bot_dict['bot']
        self.chat_id = bot_dict['chat_id']
        self.count_message_in_one_channel = 1


    async def get_content(self, count_message_in_one_channel=20):

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_SHIM', None)
        # self.browser = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


        self.count_message_in_one_channel = count_message_in_one_channel

        # options = Options()
        # options.add_argument("--headless")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--no-sandbox")

        link = self.base_url + '/vacancies?category=1'
        # self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.browser.get(link)
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        result_dict = await self.get_link_message(self.browser.page_source)

        return result_dict

    async def get_link_message(self, raw_content):
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
        self.current_message = await self.bot.send_message(self.chat_id, 'https://finder.vc is starting', disable_web_page_preview=True)

        links = []
        soup = BeautifulSoup(raw_content, 'lxml')
        list_links = soup.find_all('a', class_='vacancy-card vacancy-card_result')

        self.current_message = await self.bot.edit_message_text(
            f'{self.current_message.text}\nНайдено {len(list_links)} вакансий',
            self.current_message.chat.id,
            self.current_message.message_id,
            disable_web_page_preview=True
        )

        for i in list_links:

            links.append(i.get('href'))
            print(self.base_url + i.get('href'))  # собираем все ссылки в list, чтобы получить оттуда полный текст вакансии
            response = requests.get(self.base_url + i.get('href'))
            soup = BeautifulSoup(response.text, 'lxml')

            try:
                vacancy = soup.find('h1', class_='vacancy-info-header__title').get_text()
            except:
                vacancy = ''
            print('title = ', vacancy)

            try:
                title = soup.find('h1', class_='vacancy-info-header__title').get_text()  # Программист 1С
            except:
                title = ''
            print('title = ', title)

            try:
                body = soup.find('div', class_="vacancy-info-body__description").get_text()
            except:
                body = ''
            print('body = ', body)

            try:
                description = soup.find('div', class_='vacancy-info-body__lists').get_text()
            except:
                description = ''
            print('requirements = ', description)

            try:
                terms = soup.find('ul', class_="vacancy-info-body__list").get_text()
            except:
                terms = ''
            print('terms = ', terms)

            try:
                company = soup.find('a', class_='link').get_text()
            except:
                company = ''
            print('hiring = ', company)

            try:
                time_job = soup.find('div', class_="employment-label__text").get_text()
                # body = f'\nГрафик работы: {time_job}\n' + body
            except:
                time_job = ''
            print('time_job = ', time_job)

            try:
                item = soup.find_all('div', class_="row-text")
                salary = item[0].get_text()
                experience = item[1].get_text()
                # body = f'\nЗарплата: {cost}\nОпыт: {experience}\n' + body
            except:
                salary = ''
                experience= ''
            print('cost = ', salary)
            print('experience = ', experience)

            time_of_public = soup.find('div', class_='vacancy-info-header__publication-date').get_text()
            print('time_of_public = ', time_of_public)
            time_of_public = self.convert_date(time_of_public)
            print('time_of_public after = ', time_of_public)

# --------------------- get contacts after click button ----------------------------
            link_vacancy = self.base_url + links[-1]
            print('vacancy_url = ', link_vacancy)
            self.browser.get(link_vacancy)
            time.sleep(2)
            button = self.browser.find_element(By.XPATH,
                                               "//button[@class='vacancy-info-footer__button button button_primary button_bold button_uppercase button_mobile-block']")
            button.click()
            time.sleep(2)
            soup_contacts = BeautifulSoup(self.browser.page_source, 'lxml')
            contacts = soup_contacts.find('div', class_='contacts__item').get_text()
            print('contacts = ', contacts)

            body += f'\n{description}'

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

# ------------------- compose title and body ------------------------------------
#             if contacts:
            to_write_excel_dict['chat_name'].append('https://finder.vc')
            to_write_excel_dict['title'].append(title)
            to_write_excel_dict['body'].append(body)
            to_write_excel_dict['vacancy'].append(vacancy)
            to_write_excel_dict['vacancy_url'].append(str(link_vacancy))
            to_write_excel_dict['company'].append(company)
            to_write_excel_dict['english'].append('')
            to_write_excel_dict['relocation'].append(relocation)
            to_write_excel_dict['job_type'].append(time_job)
            to_write_excel_dict['city'].append(city)
            to_write_excel_dict['salary'].append(salary)
            to_write_excel_dict['experience'].append(experience)
            to_write_excel_dict['time_of_public'].append(time_of_public)
            to_write_excel_dict['contacts'].append(contacts)
            self.current_message = await self.bot.edit_message_text(
                f'{self.current_message.text}\n{self.count_message_in_one_channel}. {vacancy}\n',
                self.current_message.chat.id,
                self.current_message.message_id,
                disable_web_page_preview=True)
            self.count_message_in_one_channel += 1
        self.browser.quit()

        df = pd.DataFrame(
            {
                'title': to_write_excel_dict['title'],
                'body': to_write_excel_dict['body'],
                'vacancy': to_write_excel_dict['vacancy'],
                'vacancy_url': to_write_excel_dict['vacancy_url'],
                'company': to_write_excel_dict['company'],
                'english': to_write_excel_dict['english'],
                'relocation': to_write_excel_dict['relocation'],
                'job_type': to_write_excel_dict['job_type'],
                'city': to_write_excel_dict['city'],
                'salary': to_write_excel_dict['salary'],
                'experience': to_write_excel_dict['experience'],
                'time_of_public': to_write_excel_dict['time_of_public'],
                'contacts': to_write_excel_dict['contacts'],
            }
        )
        try:
            df.to_excel('./../excel/finder.vc.xlsx', sheet_name='Sheet1')
            print('записал в файл')
        except Exception as e:
            print('Finder didnt write to excel: ', e)

        self.current_message = await self.bot.send_message(
            self.chat_id,
            f'\nMessages are writting to DB, please wait a few time ...\n'
        )

        return to_write_excel_dict



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


    # def convert_date(self, str):
    #     convert = {
    #         'января': '1',
    #         'февраля': '2',
    #         'марта': '3',
    #         'апреля': '4',
    #         'мая': '5',
    #         'июня': '6',
    #         'июля': '7',
    #         'августа': '8',
    #         'сентября': '9',
    #         'октября': '10',
    #         'ноября': '11',
    #         'декабря': '12',
    #     }
    #
    #     month = str.split(' ')[1].strip()
    #     day = str.split(' ')[0].strip()
    #     year = datetime.now().strftime('%Y')
    #
    #     for i in convert:
    #         if i == month:
    #             month = convert[i]
    #             break
    #
    #     date = datetime(int(year), int(month), int(day), 12, 00)
    #
    #     return date

    def clean_company_name(self, text):
        text = re.sub('Прямой работодатель', '', text)
        text = re.sub(r'[(]{1} [a-zA-Z0-9\W\.]{1,30} [)]{1}', '', text)
        text = re.sub(r'Аккаунт зарегистрирован с (публичной почты|email) \*@[a-z.]*[, не email компании!]{0,1}', '', text)
        text = text.replace(f'\n', '')
        return text

# print('go')
# task = asyncio.create_task(FindJobGetInformation().get_content())
# loop = asyncio.new_event_loop()
# loop.run_until_complete(FindJobGetInformation().get_content())
# loop.run_until_complete(FindJobGetInformation().get_content())
