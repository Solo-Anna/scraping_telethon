import asyncio
import random
import pandas as pd
import configparser
import time
from datetime import timedelta
from db_operations.scraping_db import DataBaseOperations
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from utils.tg_channels.links import list_links
from telethon.tl.functions.messages import GetHistoryRequest
# from filters.scraping_get_profession_Alex_next_2809 import AlexSort2809
from filters.filter_jan_2023.filter_jan_2023 import VacancyFilter
from logs.logs import Logs
from helper_functions import helper_functions as helper
logs = Logs()

config = configparser.ConfigParser()
config.read("./settings/config.ini")

#--------------------------- забираем значения из config.ini-------------------------------
# api_id = config['Ruslan']['api_id']
# api_hash = config['Ruslan']['api_hash']

quant = 1  # счетчик вывода количества запушенных в базу сообщений (для контроля в консоли)

# database = config['DB3']['database']
# user = config['DB3']['user']
# password = config['DB3']['password']
# host = config['DB3']['host']
# port = config['DB3']['port']
#
# con = psycopg2.connect(
#     database=database,
#     user=user,
#     password=password,
#     host=host,
#     port=port
# )


class WriteToDbMessages():

    def __init__(self, client, bot_dict):

        self.client = client
        self.bot_dict = bot_dict
        self.last_id_agregator = 0
        self.valid_profession_list = ['marketing', 'ba', 'game', 'product', 'mobile',
                                      'pm', 'sales_manager', 'analyst', 'frontend',
                                      'designer', 'devops', 'hr', 'backend', 'frontend', 'qa', 'junior']
        self.start_date_time = None
        self.companies = []
        self.msg = []
        self.current_session = ''
        self.message = None
        self.percent = 0
        self.current_message = ''
        self.exist_dict = {
            'written': 0,
            'existed': 0
        }
        self.msg = None

    async def dump_all_participants(self, channel):

        logs.write_log(f"scraping_telethon2: function: dump_all_participants")
        path = ''
        """Записывает json-файл с информацией о всех участниках канала/чата"""
        offset_user = 0  # номер участника, с которого начинается считывание
        limit_user = 100  # максимальное число записей, передаваемых за один раз

        all_participants = []  # список всех участников канала
        filter_user = ChannelParticipantsSearch('')

        print(f'Start scraping participants from {channel}\n\n')

        try:
            while True:
                participants = await self.client(GetParticipantsRequest(channel,
                                                               filter_user, offset_user, limit_user, hash=0))
                if not participants.users:
                    break
                all_participants.extend(participants.users)
                offset_user += len(participants.users)

                print('len(all_participants = ', len(all_participants))
                print('pause 5-13 sec')
                time.sleep(random.randrange(5, 13))

            all_users_details = []  # список словарей с интересующими параметрами участников канала
            # channel_name = f'@{channel.username} | {channel.title}'
            for participant in all_participants:

                print(f'\n{participant.id}\n{participant.access_hash}')

                first_name = str(participant.first_name).replace('\'', '')
                last_name = str(participant.last_name).replace('\'', '')

                all_users_details.append({'id': participant.id,
                                          'access_hash': participant.access_hash,
                                          'first_name': first_name,
                                          'last_name': last_name,
                                          'user': participant.username,
                                          'phone': participant.phone,
                                          'is_bot': participant.bot})

            print('Numbers of followers = ', len(all_users_details))

            #--------------запись в файл------------
            file_name = channel.split('/')[-1]

            for i in all_users_details:
                print(i)
                print(i['id'], i['access_hash'])
            j1 = [str(i['id']) for i in all_users_details]
            j2 = [str(i['access_hash']) for i in all_users_details]
            j3 = [str(i['user']) for i in all_users_details]
            j4 = [str(i['first_name']) for i in all_users_details]
            j5 = [str(i['last_name']) for i in all_users_details]


            df = pd.DataFrame(
                {
                'from channel': channel,
                'id_participant': j1,
                'access_hash': j2,
                'username': j3,
                'first_name': j4,
                'last_name': j5
                 }
            )

            path = f'./excel/participants/participants_from_{file_name}.xlsx'
            df.to_excel(path, sheet_name='Sheet1')

            #------------- конец записи в файл ------------

            print(f'\nPause 10-20 sec...')
            time.sleep(random.randrange(10, 20))
            print('...Continue')


        except Exception as e:
            print(f'Error для канала {channel}: {e}')
        return path

    async def dump_all_messages(self, channel, limit_msg):

        logs.write_log(f"scraping_telethon2: function: dump_all_messages")

        print('dump')
        self.count_message_in_one_channel = 1
        block = False
        offset_msg = 0  # номер записи, с которой начинается считывание
        # limit_msg = 1   # максимальное число записей, передаваемых за один раз
        all_messages = []  # список всех сообщений
        total_messages = 0
        total_count_limit = limit_msg  # значение 0 = все сообщения
        history = None

        new_text = f"<em>channel {channel}</em>"

        self.msg = await helper.send_message(
            bot=self.bot_dict['bot'],
            chat_id=self.bot_dict['chat_id'],
            text=new_text
        )
        # self.msg = await self.bot_dict['bot'].send_message(self.bot_dict['chat_id'], f'<em>channel {channel}</em>', parse_mode='html', disable_web_page_preview = True)

        # data = await self.client.get_entity('https://t.me/fake_adminka')
        # print(data)

        while True:
            try:
                history = await self.client(GetHistoryRequest(
                    peer=channel,
                    offset_id=offset_msg,
                    offset_date=None, add_offset=0,
                    limit=limit_msg, max_id=0, min_id=0,
                    hash=0))
            except Exception as e:
                await self.bot_dict['bot'].send_message(
                                        self.bot_dict['chat_id'],
                                        f"Getting history:\n{str(e)}: {channel}\npause 25-30 seconds...",
                                        parse_mode="HTML",
                                        disable_web_page_preview = True)
                time.sleep(2)

            # if not history.messages:
            if not history:
                print(f'Not history for channel {channel}')
                await self.bot_dict['bot'].send_message(self.bot_dict['chat_id'], f'Not history for channel {channel}', disable_web_page_preview = True)
                break
            messages = history.messages
            for message in messages:
                if not message.message:  # если сообщение пустое, например "Александр теперь в группе"
                    pass
                else:
                    all_messages.append(message.to_dict())

            try:
                offset_msg = messages[len(messages) - 1].id
            except Exception as e:
                print('192 - offset_msg = messages[len(messages) - 1].id\n', e)
                break
            total_messages = len(all_messages)
            if (total_count_limit != 0 and total_messages >= total_count_limit) or not messages:
                break

        await self.process_messages(channel, all_messages)
        print('pause 5-12 sec.')
        await asyncio.sleep(random.randrange(5, 12))

    async def process_messages(self, channel, all_messages):

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

        for one_message in reversed(all_messages):
            await self.operations_with_each_message(channel, one_message)

        new_text = f"\nhas written {self.exist_dict['written']}\nexist: {self.exist_dict['existed']}"
        self.msg = await helper.edit_message(
            bot=self.bot_dict['bot'],
            text=new_text,
            msg=self.msg
        )

        # await self.msg.edit_text(f"{self.msg.text}\nhas written {self.exist_dict['written']}\nexist: {self.exist_dict['existed']}", disable_web_page_preview = True)
        self.exist_dict['written'] = 0
        self.exist_dict['existed'] = 0


    async def operations_with_each_message(self, channel, one_message):

        response_dict = await helper.transformTitleBodyBeforeDb(one_message['message'])
        # title = one_message['message'].partition(f'\n')[0]
        # body = one_message['message'].replace(title, '').replace(f'\n\n', f'\n')
        title = response_dict['title']
        body = response_dict['body']
        response = DataBaseOperations(None).check_exists_message(
            title=title,
            body=body
        )
        print('response ', response)
        if response:
            date = (one_message['date'] + timedelta(hours=3))
            results_dict = {
                'chat_name': channel,
                'title': title,
                'body': body,
                'profession': '',
                'vacancy': '',
                'vacancy_url': '',
                'company': '',
                'english': '',
                'relocation': '',
                'job_type': '',
                'city': '',
                'salary': '',
                'experience': '',
                'contacts': '',
                'time_of_public': date,
                'created_at': '',
                'session': self.current_session
            }

            print(f"----------------\nchannel = {channel}")
            print(f"vacancy_link {channel}/{one_message['id']}")
            print(f"title = {title[0:60]}")
    # =============================== scheme next steps =======================================
            # we are in the messages loop, it takes them by one
            # -----------------------LOOP---------------------------------
            # STEP0/ I have to get id for last message in agregator_channel
            #          I did it previous step (look at up)

            # STEP NEXT/ Get the profession/ previous it needs to get companies list from table companies
            #           I have got the companies previous. Look at up
            # self.companies = DataBaseOperations(con=con).get_all_from_db(table_name='companies', without_sort=True)  # check!!!

            response = VacancyFilter().sort_profession(title, body)
            profession = response['profession']
            params = response['params']

            # STEP1/ we need to write to DB by professions that message with last message's id in agregator_channel
            #       I can get this with DBOperations()

            # if 'no_sort' not in profession['profession']:
            # profession = await self.clear_not_valid_professions(profession)  # delete not valid keys (middle, senior and others)
            # print('valid professions ', profession['profession'])
            if profession['profession']:
                for key in params:
                    if not results_dict[key] and params[key]:
                        results_dict[key] = params[key]
                    # write to profession's tables. Returns dict with professions as a key and False, if it was written and True if existed
                    # -------------------------------- write all message for admin in one table--------------------------------
                DataBaseOperations(None).push_to_admin_table(
                    results_dict=results_dict,
                    profession=profession,
                    check_or_exists=True,
                    params=params
                )
                self.exist_dict['written'] += 1
        else:
            print(f'{title[:40]}:\nthis vacancy has existed already\n---------\n')
            self.exist_dict['existed'] += 1

    async def delete_messages(self):

        logs.write_log(f"scraping_telethon2: function: delete_messages")

        for i in self.msg:
            i.delete()
        self.msg = []

    # async def get_last_and_tgpublic_shorts(self, current_session, shorts=False, fulls_all=False, one_profession=None):
    #     """
    #     It gets last messages from profession's tables,
    #     composes shorts from them
    #     and send to profession's tg channels
    #     Here user decide short or full sending
    #
    #     """
    #     logs.write_log(f"scraping_telethon2: function: get_last_and_tgpublic_shorts")
    #
    #     self.companies = DataBaseOperations(None).get_all_from_db(table_name='companies', without_sort=True)  # check!!!
    #
    #     # get current session
    #     if not current_session:
    #         pass
    #         current_session = DataBaseOperations(None).get_all_from_db(
    #             table_name='current_session',
    #             param='ORDER BY id DESC LIMIT 1',
    #             without_sort=True,
    #             order=None,
    #             field='session',
    #             curs=None
    #         )
    #         for value in current_session:
    #             self.current_session = value[0]
    #     else:
    #         self.current_session = current_session
    #
    #     if one_profession:
    #         self.last_id_agregator = await self.get_last_id_agregator()
    #
    #     if shorts:
    #         await self.send_sorts()  # 1. for send shorts
    #     elif not fulls_all:
    #         await self.send_fulls(all=False, one_profession=one_profession)  # 2. for send last full messages from db
    #     else:
    #         await self.send_fulls(all=True, one_profession=one_profession)  # 2. for send last full messages from db
    #
    #     await self.bot_dict['bot'].send_message(self.bot_dict['chat_id'], 'Telegram channels parsing: DONE')

    # async def send_sorts(self):
    #
    #     logs.write_log(f"scraping_telethon2: function: send_sorts")
    #
    #     messages_counter = 1
    #     short_message = ''
    #     for pro in self.valid_profession_list:
    #         print(f"It gets from profession's tables = {pro}")
    #         # get last records from table with profession PRO
    #         # param = f"WHERE created_at > '{time_start['year']}-{time_start['month']}-{time_start['day']} {time_start['hour']}:{time_start['minute']}:{time_start['sec']}'"
    #         param = f"WHERE session='{self.current_session}'"
    #         response_messages = DataBaseOperations(None).get_all_from_db(pro,
    #                                                                         param=param)  # check!!!
    #         for response in response_messages:
    #             title = response[2]
    #             body = response[3]
    #             agregator_id = response[7]
    #             # response_params = AlexSort2809().sort_by_profession_by_Alex(title, body, self.companies)
    #             response_params = AlexSort2809().sort_by_profession_by_Alex(title, body)
    #
    #             params = response_params['params']
    #             short_message += f"Вакансия: \n"
    #             short_message += f"Компания: {params['company_hiring']}\n" if params['company_hiring'] else ''
    #             short_message += f"English: {params['english_level']}\n" if params['english_level'] else ''
    #             short_message += f"Тип работы: {params['jobs_type']}\n" if params['jobs_type'] else ''
    #             short_message += f"Релокация: {params['relocation']}\n" if params['relocation'] else ''
    #             short_message += f"Город: {params['city']}\n" if params['city'] else ''
    #             short_message += hlink('Подробнее >>>\n\n', f"{config['My_channels']['agregator_link']}/{agregator_id}")
    #
    #             # STEP4/ send this shorts in channels
    #             if messages_counter > 5 or messages_counter == len(response_messages):
    #                 short_message = f"Вакансии для {pro}:\n\n" + short_message
    #                 await self.bot_dict['bot'].send_message(
    #                     config['My_channels'][f"{pro}_channel"],
    #                     short_message, parse_mode='HTML',
    #                     disable_web_page_preview = True)
    #
    #                 print(f'\nprinted short in channel {pro}\n')
    #                 time.sleep(2)
    #                 short_message = ''
    #                 messages_counter = 1
    #             else:
    #                 messages_counter += 1
    #
    # async def send_fulls(self, all, one_profession=None):
    #
    #     logs.write_log(f"scraping_telethon2: function: send_fulls")
    #
    #     professions_amount = []
    #     param = ''
    #     profession_list = {}
    #     profession_list['profession'] = []
    #     results_dict = {}
    #
    #     if not all:
    #         param = f"WHERE session='{self.current_session}'"
    #
    #     if one_profession:
    #         one_profession = one_profession[2:]
    #         if param:
    #             param += f" AND profession LIKE '%{one_profession}%'"
    #         else:
    #             param = f"WHERE profession LIKE '%{one_profession}%'"
    #
    #     # 1) choose all records with one_profession
    #     response_messages = DataBaseOperations(None).get_all_from_db('admin_last_session', param=param)
    #     await self.bot_dict['bot'].send_message(self.bot_dict['chat_id'], f"There are {len(response_messages)} vacancies")
    #     self.message = await self.bot_dict['bot'].send_message(self.bot_dict['chat_id'], f'progress {self.percent}%')
    #     n = 0
    #     for message in response_messages:
    #         n += 1
    #         await self.show_process(n, len(response_messages))
    #
    #         if message[4]:
    #             profession_list['profession'] = []
    #             print(message[4])
    #             if ',' in message[4]:
    #                 pro = message[4].split(',')
    #             else:
    #                 pro = [message[4]]
    #
    #             for i in pro:
    #                 profession_list['profession'].append(i.strip())
    #
    #             if one_profession:
    #                 professions_amount = profession_list['profession']  # count how much of professions
    #                 profession_list['profession'] = [one_profession,]  # rewrite list if one_profession
    #
    #             results_dict['chat_name'] = message[1]
    #             results_dict['title'] = message[2]
    #             results_dict['body'] = message[3]
    #             results_dict['profession'] = message[4]
    #             results_dict['vacancy'] = message[5]
    #             results_dict['vacancy_url'] = message[6]
    #             results_dict['company'] = message[7]
    #             results_dict['english'] = message[8]
    #             results_dict['relocation'] = message[9]
    #             results_dict['job_type'] = message[10]
    #             results_dict['city'] = message[11]
    #             results_dict['salary'] = message[12]
    #             results_dict['experience'] = message[13]
    #             results_dict['contacts'] = message[14]
    #             results_dict['time_of_public'] = message[15]
    #             results_dict['created_at'] = message[16]
    #             results_dict['agregator_link'] = message[17]
    #             results_dict['session'] = message[18]
    #             sended_to_agregator = message[19]
    #
    #             if sended_to_agregator:
    #                 results_dict['agregator_link'] = sended_to_agregator
    #
    #             # compose message_to_send
    #             message_to_send = ''
    #             if results_dict['vacancy']:
    #                 message_to_send += f"<b>Вакансия:</b> {results_dict['vacancy']}\n"
    #             if results_dict['company']:
    #                 message_to_send += f"<b>Компания:</b> {results_dict['company']}\n"
    #             if results_dict['english']:
    #                 message_to_send += f"<b>Английский:</b> {results_dict['english']}\n"
    #             if results_dict['relocation']:
    #                 message_to_send += f"<b>Релокация:</b> {results_dict['relocation']}\n"
    #             if results_dict['job_type']:
    #                 message_to_send += f"<b>Тип работы:</b> {results_dict['job_type']}\n"
    #             if results_dict['city']:
    #                 message_to_send += f"<b>Город/страна:</b> {results_dict['city']}\n"
    #             if results_dict['salary']:
    #                 message_to_send += f"<b>Зарплата:</b> {results_dict['salary']}\n"
    #             if results_dict['experience']:
    #                 message_to_send += f"<b>Опыт работы:</b> {results_dict['experience']}\n"
    #             if results_dict['contacts']:
    #                 message_to_send += f"<b>Контакты:</b> {results_dict['contacts']}\n"
    #             elif results_dict['vacancy_url']:
    #                 message_to_send += f"<b>Ссылка на вакансию:</b> {results_dict['vacancy_url']}\n\n"
    #
    #             message_to_send += f"{results_dict['title']}\n"
    #             message_to_send += results_dict['body']
    #
    #             if len(message_to_send) > 4096:
    #                 message_to_send = message_to_send[0:4092] + '...'
    #
    #             # push to profession tables
    #             profession_list = await self.clear_not_valid_professions(profession_list)
    #             response_dict = DataBaseOperations(None).push_to_bd(results_dict, profession_list, self.last_id_agregator)
    #
    #             # push to agregator
    #             # if profession is not no_sort than public in agregator, else public to n0_sort
    #             if 'no_sort' not in response_dict and False in response_dict.values() and not sended_to_agregator:  # sended_to_agregator shows it was sended to agregator yet
    #                 await self.bot_dict['bot'].send_message(config['My_channels']['agregator_channel'], message_to_send, parse_mode='html')
    #                 results_dict['agregator_link'] = self.last_id_agregator
    #
    #                 # if it was sending to agregator that I give it the number agregator message for mark that as has sended already
    #                 DataBaseOperations(None).run_free_request(request=f"UPDATE admin_last_session SET sended_to_agregator='{self.last_id_agregator}' WHERE id={message[0]}")
    #
    #                 self.last_id_agregator += 1
    #                 print(f'Send to TG channel agregator\n')
    #                 await asyncio.sleep(random.randrange(5, 17))
    #
    #             # push to profession channels
    #             print('for check: id message = ', message[0])
    #             pass
    #             for channel in response_dict:
    #                 if not response_dict[channel]:
    #                     try:
    #                         await self.bot_dict['bot'].send_message(config['My_channels'][f'{channel}_channel'],
    #                                                                 message_to_send, parse_mode='html')
    #                     except Exception as telethon:
    #                         await self.bot_dict['bot'].send_message(self.bot_dict['chat_id'],
    #                                                                 f"error: channel - {channel}")  # I had the error from sending to some channel
    #                     print(f'Send to TG channel {channel}\n')
    #                     await asyncio.sleep(random.randrange(5, 17))
    #
    #             if not one_profession or (one_profession and len(professions_amount)<2):  # 3) if this vacancy has not another professions - delete it
    #                 # delete from admin_last_session
    #                 id_message_from_admin = message[0]
    #                 DataBaseOperations(None).delete_data(
    #                     table_name='admin_last_session',
    #                     param=f"WHERE id={id_message_from_admin}"
    #                 )
    #                 print(f'Message id {id_message_from_admin} was deleted')
    #             else:
    #                 #  4) if this vacancy has another professions - don't delete.
    #                 # 	But add it message_id in agregator channel to it to know that it was publishing
    #                 # 	And delete from professions that one_profession
    #                 profession = ''
    #                 for pro in professions_amount:
    #                     if pro != one_profession:
    #                         profession += f"{pro}, "
    #                 profession = profession[:-2]
    #                 DataBaseOperations(None).run_free_request(request=f"UPDATE admin_last_session SET profession='{profession}' WHERE id={message[0]}")
    #
    #         else:
    #             print('message[4] doesnt exist. id=  ', message[0])
    #         pass

    async def show_process(self, n, len):
        check = n*100//len
        if check > self.percent:
            quantity = check // 5
            self.percent = check
            self.message = await self.bot_dict['bot'].edit_message_text(f"progress {'|'* quantity} {self.percent}%", self.bot_dict['chat_id'], self.message.message_id)

    # async def clear_not_valid_professions(self, profession):
    #
    #     logs.write_log(f"scraping_telethon2: function: clear_not_valid_professions")
    #
    #     # check if is it set or list? There is used methods for set, not for list and generated the error
    #     if type(profession['profession']) is list:
    #         profession['profession'] = set(profession['profession'])
    #
    #     if 'fullstack' in profession['profession']:
    #         if 'backend' not in profession['profession']:
    #             profession['profession'].update({'backend'},)
    #         if 'frontend' not in profession['profession']:
    #             profession['profession'].update({'frontend'},)
    #
    #     exclude_list = []
    #     values_list = profession['profession']
    #     for value in values_list:
    #         if value not in self.valid_profession_list:
    #             exclude_list.append(value)
    #     for exclude in exclude_list:
    #         profession['profession'].remove(exclude)
    #     if not profession['profession']:
    #         profession['profession'] = ['no_sort']
    #     return profession

    async def get_last_id_agregator(self):

        logs.write_log(f"scraping_telethon2: function: get_last_id_agregator")

        history_argegator = await self.client(GetHistoryRequest(
            peer=config['My_channels']['agregator_link'],
            offset_id=0,
            offset_date=None, add_offset=0,
            limit=1, max_id=0, min_id=0,
            hash=0))
        last_id_agregator = history_argegator.messages[0].id
        print('last id in agregator = ', last_id_agregator)
        await asyncio.sleep(random.randrange(1, 3))
        return last_id_agregator

    async def main_start(self, list_links, limit_msg, action):

        print('main_start')
        # self.last_id_agregator = 0
        # self.last_id_agregator = await self.get_last_id_agregator()+1

        if action == 'get_message':
            for url in list_links:
                await self.dump_all_messages(url, limit_msg)  # resolve the problem of a wait seconds

        elif action == 'get_participants':
            for url in list_links:
                await self.dump_all_participants(url)


    async def start(self, limit_msg, action):
        print('start')
        await self.main_start(list_links, limit_msg, action)

async def main(client, bot_dict, action='get_message'):
    get_messages = WriteToDbMessages(client, bot_dict)
    await get_messages.start(limit_msg=20, action=action)  #get_participants get_message

