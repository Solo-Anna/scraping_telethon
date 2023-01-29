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

            response = VacancyFilter().sort_profession(title, body)
            profession = response['profession']
            params = response['params']

            # STEP1/ we need to write to DB by professions that message with last message's id in agregator_channel
            #       I can get this with DBOperations()

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


    async def show_process(self, n, len):
        check = n*100//len
        if check > self.percent:
            quantity = check // 5
            self.percent = check
            self.message = await self.bot_dict['bot'].edit_message_text(f"progress {'|'* quantity} {self.percent}%", self.bot_dict['chat_id'], self.message.message_id)


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

