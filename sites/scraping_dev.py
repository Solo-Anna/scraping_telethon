
import re
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import helper_functions.helper_functions
from db_operations.scraping_db import DataBaseOperations
from sites.sites_additional_utils.get_structure import get_structure, get_structure_advance
from sites.write_each_vacancy_to_db import write_each_vacancy
from settings.browser_settings import options, chrome_driver_path
from utils.additional_variables.additional_variables import sites_search_words
from helper_functions.helper_functions import edit_message, send_message, get_name_session

junior_link = 'https://jobs.devby.io/?filter[levels][]=intern&filter[levels][]=junior'
link_search = 'https://jobs.devby.io/?&filter[search]=project%20manager'

class DevGetInformation:

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
        self.main_url = 'https://jobs.devby.io'


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

        # # get juniors -------------------------
        # link = junior_link
        # await self.bot.send_message(self.chat_id, link, disable_web_page_preview=True)
        #
        # print('page link: ', link)
        # try:
        #     self.browser.get(link)
        # except Exception as telethon:
        #     print('bot could not to get the link', telethon)
        #
        # try:
        #     self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # except:
        #     pass
        # word = 'junior'
        # await self.get_link_message(self.browser.page_source, word)
        #-------------------------------------

        for word in self.search_words:
            self.page_number = 1
            if len(word.split(' '))>1:
                word1 = word.split(' ')[0]
                word2 = word.split(' ')[1]
                link = f'https://jobs.devby.io/?&filter[search]={word1}%20{word2}'
            else:
                link = f'https://jobs.devby.io/?&filter[search]={word}'

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

            # till = 13
            # for self.page_number in range(1, till):
            #     try:
            #         await self.bot.send_message(self.chat_id, f'https://hh.ru/search/vacancy?text={word}&from=suggest_post&salary=&schedule=remote&no_magic=true&ored_clusters=true&enable_snippets=true&search_period=1&excluded_text=&page={self.page_number}&hhtmFrom=vacancy_search_list',
            #                               disable_web_page_preview=True)
            #         self.browser.get(f'https://hh.ru/search/vacancy?text={word}&from=suggest_post&salary=&schedule=remote&no_magic=true&ored_clusters=true&enable_snippets=true&search_period=1&excluded_text=&page={self.page_number}&hhtmFrom=vacancy_search_list')
            #         self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #         vacancy_exists_on_page = await self.get_link_message(self.browser.page_source, word)
            #         if not vacancy_exists_on_page:
            #             break
            #     except:
            #         break
        await self.bot.send_message(self.chat_id, 'dev.by parsing: Done!', disable_web_page_preview=True)

    async def get_link_message(self, raw_content, word):

        links = []
        soup = BeautifulSoup(raw_content, 'lxml')

        list_links = soup.find_all('div', class_='vacancies-list-item__position')
        if list_links:
            print(f'\nПо слову {word} найдено {len(list_links)} вакансий\n')
            self.current_message = await self.bot.send_message(self.chat_id, f'dev.by:\nПо слову {word} найдено {len(list_links)} вакансий на странице {self.page_number}', disable_web_page_preview=True)

            # -------------------- check what is current session --------------

            self.current_session = get_name_session()

            # current_session = DataBaseOperations(None).get_all_from_db(
            #     table_name='current_session',
            #     param='ORDER BY id DESC LIMIT 1',
            #     without_sort=True,
            #     order=None,
            #     field='session',
            #     curs=None
            # )
            # for value in current_session:
            #     self.current_session = value[0]

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
        vacancy_url = i.find('a', class_='vacancies-list-item__link_block').get('href')
        vacancy_url = self.main_url + vacancy_url
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
        vacancy = soup.find('div', class_='vacancy__header__name').get_text().replace('Вакансия ', '')
        print('vacancy = ', vacancy)

        # get title --------------------------
        title = vacancy
        print('title = ',title)

        # get body --------------------------
        body = ''
        body_content = soup.find('div', class_='vacancy__body').find('div', class_='text')
        structure = await get_structure_advance(body_content)
        body_content_list_p = body_content.find_all('strong')
        body_content_list_ul = body_content.find_all('ul')
        for element in structure:
            if element == 'p':
                try:
                    temp = body_content_list_p[0].get_text()
                    # print('************\nPPP', temp, '\n***************')
                    body += f"\n{temp}\n"
                    # print('\n', temp)
                    body_content_list_p.pop(0)
                except:
                    break
            if element == 'ul':
                if body_content_list_ul:
                    temp = body_content_list_ul[0]
                    for li in temp:
                        if li.text != ' ' and li != '\n' and li.text:
                            try:
                                # print('************\nLI', li, '\n***************')
                                body += f"-{li.get_text().strip()}\n"
                                # print('-', li.get_text())
                            except:
                                break
                    body_content_list_ul.pop(0)

        # for element in body_content_list_p:
        #     body += f"{element.get_text()}\n"

        print('body = ', body)

        # get tags --------------------------
        tags = ''
        try:
            tags_list = soup.find_all('div', class_="vacancy__tags__item")
            for i in tags_list:
                tags += f"#{i.get_text().replace(' ', '')} "
            tags = tags[0:-1]
        except:
            pass
        print('tags = ',tags)

        body = f"{body}\n{tags}"

        tags = ''
        tags_list = soup.find_all('div', class_='vacancy__info-block__item')
        for element in tags_list:
            tags += f'{element.get_text()}, '
        tags = tags[:-2]

        level = re.findall(r'Уровень: [a-zA-Zа-яА-Я]+', tags)
        if level:
            level = level[0].replace('Уровень:', '').strip()
        else:
            level = ''
        body += f" #{level}"
        print('level = ', level)

        english = re.findall(r'Уровень английского: [a-zA-Zа-яА-Я0-9\s]+', tags)
        if english:
            english = english[0].replace('Уровень английского:', '').strip()
        else:
            english = ''
        print("english ", english)

        # get city --------------------------
        city = re.findall(r'Город: [a-zA-Zа-яА-Я]+', tags)
        if city:
            city = city[0].replace('Город:', '').strip()
        else:
            city = ''
        print('city = ', city)

        # get company --------------------------
        try:
            company = soup.find('div', class_='vacancy__footer__company-name').get_text()
        except:
            company = ''
        print('company = ',company)

        # get salary --------------------------
        # try:
        #     salary = soup.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').get_text()
        # except:
        #     salary = ''
        # print('salary = ',salary)

        # get experience --------------------------
        experience = re.findall(r'Опыт: [a-zA-Zа-яА-Я0-9\s]+', tags)
        if experience:
            experience = experience[0].replace('Опыт:', '').strip()
        else:
            experience = ''
        print('experience = ',experience)

        remote = re.findall(r'Возможна удалённая работа: [a-zA-Z\sа-яА-Я0-9]+', tags)
        if remote:
            remote = remote[0].replace('Возможна удалённая работа:', '').strip()
        else:
            remote = ''
        print('remote = ',remote)

        full_time = re.findall(r'Режим работы: [a-zA-Zа-яА-Я0-9\s]+', tags)
        if full_time:
            full_time = full_time[0].replace('Режим работы:', '').strip()
        else:
            full_time = ''
        print('full_time = ', full_time)

        job_type = ''
        if remote:
            job_type += f"Удаленный формат: {remote}\n"
        if full_time:
            job_type += f"График работы: {full_time}"

        contacts = ''
        salary = ''

        date = datetime.now()

        # ------------------------- search relocation ----------------------------
        relocation = ''
        if re.findall(r'[Рр]елокация', body):
            relocation = 'релокация'


        # # ------------------------- search english ----------------------------
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
            'chat_name': 'https://dev.by',
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