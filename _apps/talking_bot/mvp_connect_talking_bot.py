import configparser
import logging
import os
from datetime import datetime
import psycopg2
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from settings.os_getenv import talking_token


from _apps.talking_bot.db.db_oparations import DB

config = configparser.ConfigParser()
config.read("./settings/config.ini")

database = config['DB_local_clone']['database']
user = config['DB_local_clone']['user']
password = config['DB_local_clone']['password']
host = config['DB_local_clone']['host']
port = config['DB_local_clone']['port']

logging.basicConfig(level=logging.INFO)
bot = Bot(token=talking_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class TalkingBot:

    def __init__(self):
        self.message_hystory = []
        self.user_id = None
        self.user_chat_to = None
        self.user_first_name = None
        self.user_last_name = None
        self.admin_id = 758905227
        self.dict_users = {}
        self.client = None
        self.active_dialog = {}
        self.user_name = ''
        self.active_users_ids_list = []
        self.markup_close = ReplyKeyboardMarkup(resize_keyboard=True)
        self.markup_close.add(KeyboardButton('Закрыть диалог'))
        self.message_from_admin_to_user = {}
        self.temporary_msg = None
        self.con = psycopg2.connect(
            database=database,
            user=user,
            host=host,
            password=password,
            port=port
        )

        self.cur = self.con.cursor()
        self.db = DB(self.con, self.cur)
        self.keyboard_users_in_active_dialogs = ReplyKeyboardMarkup(resize_keyboard=True)
        self.keyboard_users_in_active_dialogs.row(KeyboardButton('Close active dialog'), KeyboardButton('Switch active dialog'))
        self.talking_keyboard = None
        # 5755261667 (Ruslan)
        # 1763672666 (Настя)
        # 758905227 (Александр)


    def main_self(self):

        @dp.message_handler(commands=['start'])
        async def send_welcome(message: types.Message):

            if message.from_user.id != self.admin_id:
                self.message_hystory.append(await bot.send_message(self.admin_id, f'<i>Стартовал пользователь с id {message.from_user.id}\n{message.from_user.username}</i>', parse_mode='html'))
                # self.message_hystory.append(await bot.send_message(message.chat.id, f'<i>Стартовал пользователь с id {message.from_user.id}\n{message.from_user.username}</i>', parse_mode='html'))

                print('user has started')


                self.talking_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
                talking_start = KeyboardButton('Начать диалог')
                self.talking_keyboard.add(talking_start)
                await bot.send_message(message.chat.id, f"Добрый день, {message.from_user.first_name}!\n"
                                                        f"Для начала диалога, нажмите кнопку \"Начать диалог\" внизу ⬇️.\n"
                                                        f"Как только оператор примет Ваш запрос, Вы увидите сообщение \"Оператор на связи\"",
                                       reply_markup=self.talking_keyboard)
            else:
                self.message_hystory.append(await bot.send_message(self.admin_id, 'Бот активен'))

        @dp.message_handler(commands=['del*'])
        async def send_welcome(message: types.Message):
            self.db.drop_table(table_name='users')
            self.db.drop_table(table_name='dialogs')

        @dp.message_handler(content_types=['text'])
        async def messages(message):
            if message.text == 'Switch active dialog':

                # get from db all active dialogs
                active_dialogs = self.db.get_all_from_db('users', """WHERE active='True'""")
                if active_dialogs:
                    active_dialogs_keyboard = InlineKeyboardMarkup()
                    for i in active_dialogs:
                        active_dialogs_keyboard.add(InlineKeyboardButton(f"{i[1]}|{i[2]} {i[3]}", callback_data=f"{i[1]}|{i[2]} {i[3]}"))
                    await bot.send_message(self.admin_id, 'Choose dialog', reply_markup=active_dialogs_keyboard)
                else:
                    self.db.update_user_active_status(
                        id_user=self.active_dialog['id'],
                        status=True
                    )
                    await bot.send_message(self.admin_id, 'You have any active dialogs')

                # compose inline menu with active dialogs
                # show it whit message choose


            elif message.text == 'Начать диалог':

                #getting all data from user
                user_id = message.from_user.id
                user_first_name = message.from_user.first_name
                user_last_name = message.from_user.last_name
                user_chat_to = message.chat.id
                username = message.from_user.username

                client = f'{user_id} {user_first_name} {user_last_name}'
                self.dict_users[client] = {}
                self.dict_users[client] = {
                    'id': user_id,
                    'first_name': user_first_name,
                    'last_name': user_last_name,
                    'user_chat_to': user_chat_to,
                    'username': username,
                    'admin_sees': f"{user_id}|{user_first_name} {user_last_name}",
                    'active': False
                }

                # add user to DB
                self.db.create_user(self.dict_users[client])

                self.message_hystory.append(await bot.send_message(user_chat_to, f'Запрос отправлен, скоро с вами свяжется оператор'))
                markup = InlineKeyboardMarkup()
                button = InlineKeyboardButton('Начать диалог', callback_data=f'start_dialog/{user_id}')
                markup.add(button)

                self.message_hystory.append(await bot.send_message(self.admin_id, f'Поступил запрос от пользователя\n'
                                                                                  f'id - {user_id}\n'
                                                                                  f'first name - {user_first_name}\n'
                                                                                  f'last name - {user_last_name}',
                                                                   reply_markup=markup)
                                            )

            elif message.text == 'Закрыть диалог':
                self.active_dialog={}
                markup_choose_dialog = InlineKeyboardMarkup()
                pass

            elif message.from_user.id in self.active_users_ids_list:
                if message.from_user.id != self.active_dialog['id']:
                    admin_sees = self.db.get_all_from_db('users', f"""WHERE id_user='{message.from_user.id}'""")[0]
                    id_user=admin_sees[1]
                    admin_sees = f"{admin_sees[1]}|{admin_sees[2]} {admin_sees[3]}"
                else:
                    admin_sees = self.active_dialog['admin_sees']
                    id_user = self.active_dialog['id']
                await bot.send_message(self.admin_id, f"{admin_sees}:\n{message.text}")
                self.db.add_dialogs(id_user=id_user, text=f"{datetime.now().strftime('%d-%m %H:%M')} user\n{message.text}\n")
            else:
                if self.active_dialog:
                    await bot.send_message(self.active_dialog['user_chat_to'], f"оператор:\n{message.text}")
                    self.db.add_dialogs(id_user=self.active_dialog['id'],
                                        text=f"{datetime.now().strftime('%d-%m %H:%M')} you:\n{message.text}\n")

                else:
                    if message.from_user.id == self.user_id:
                        await bot.send_message(message.chat.id, 'You have any active dialog')
                    # else:
                    #     await bot.send_message(message.chat.id, 'Для активации диалога нажмите кнопку [Начать диалог]', reply_markup=self.talking_keyboard)



        @dp.callback_query_handler()
        async def catch_callback(callback: types.CallbackQuery):
            if 'start_dialog' in callback.data:

                id_user = callback.data.split('/')[1]

                # to find this user:
                for key in self.dict_users:
                    if int(self.dict_users[key]['id']) == int(id_user):
                        self.dict_users[key]['active'] = True
                        self.user_name = key
                        self.db.update_user_active_status(
                            id_user=self.dict_users[key]['id'],
                            status=True
                        )
                        self.active_dialog = self.dict_users[key]
                        self.active_users_ids_list.append(self.active_dialog['id'])

                self.message_hystory.append(await bot.send_message(self.active_dialog['user_chat_to'], f"Оператор на связи"))

                await bot.send_message(self.admin_id, f"Активная сессия с {self.active_dialog['admin_sees']} начата", reply_markup=self.keyboard_users_in_active_dialogs)

            if callback.data.isalnum():
                for i in self.dict_users:
                    if self.dict_users[i]['id'] == int(callback.data):
                        await self.temporary_msg.delete()
                        await bot.send_message(self.dict_users[i]['user_chat_to'], f"оператор:\n{self.message_from_admin_to_user['message']}")
                        # await bot.edit_message_text(f"{self.dict_users[i]['admin_sees']}\n{self.message_from_admin_to_user['message']}",
                        #                             chat_id=self.message_from_admin_to_user['chat_id'],
                        #                             message_id=self.message_from_admin_to_user['message_id']
                        #                             )

                        break

            if callback.data.split('|')[0].isalnum():
                # switch active dialog and update DB
                id_user=int(callback.data.split('|')[0])
                self.db.update_user_active_status(id_user=id_user, status=True)
                active_dialog = self.db.get_all_from_db(table_name='users', param=f"""WHERE id_user='{id_user}'""")
                self.active_dialog['id']=active_dialog[0][1]
                self.active_dialog['first_name']=active_dialog[0][2]
                self.active_dialog['last_name']=active_dialog[0][3]
                self.active_dialog['username']=active_dialog[0][4]
                self.active_dialog['user_chat_to'] = active_dialog[0][6]
                self.active_dialog['active']=active_dialog[0][7]
                self.active_dialog['admin_sees'] = f"{self.active_dialog['id']}|{self.active_dialog['first_name']} {self.active_dialog['last_name']}"

                # get dialog from db
                t = self.db.get_all_from_db('dialogs')
                dialog_from_db = self.db.get_all_from_db('dialogs', f"""WHERE id_user='{id_user}'""")
                dialog_message = ''
                for i in dialog_from_db:
                    dialog_message += i[2]
                await bot.send_message(self.admin_id, dialog_message)
                # set self.active_dialog like it
                pass

        async def clear_screen():
            for msg in reversed(self.message_hystory):
                await msg.delete()
                self.message_hystory.pop()
                pass

        executor.start_polling(dp, skip_updates=True)
def talking_bot_run():
    TalkingBot().main_self()

# talking_bot_run()