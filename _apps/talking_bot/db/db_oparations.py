from datetime import datetime


class DB:
    def __init__(self, con, cur):
        self.con = con
        self.cur = cur

    def create_user(self, user_dict):

        # self.show_users()
        self.check_table_users_exists()
        user_exists = self.check_user_exist(user_dict['id'])

        if not user_dict['username']:
            username = ''
        else:
            username = user_dict['username'].strip()

        if not user_exists:
            new_post = f"""INSERT INTO users (id_user, first_name, last_name, username, data_first_connect, user_chat_to, active)
                            VALUES ({user_dict['id']}, '{user_dict['first_name']}', '{user_dict['last_name']}',
                            '{username}', '{datetime.now()}', '{user_dict['user_chat_to']}', '{False}')"""
            with self.con:
                print(new_post)
                self.cur.execute(new_post)
                print('New user has been created')

    def check_table_users_exists(self):
        query = """CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    id_user VARCHAR(20),
                    first_name VARCHAR (30),
                    last_name VARCHAR (30),
                    username VARCHAR (50),
                    data_first_connect TIMESTAMP,
                    user_chat_to VARCHAR (30),
                    active BOOLEAN
            );"""
        with self.con:
            self.cur.execute(query)
            print('Table users has been created or exists')

    def add_dialogs(self, id_user, text):

        self.check_table_dialogs_exists()
        query = f"""INSERT INTO dialogs (id_user, message) VALUES ('{id_user}', '{text}');"""
        with self.con:
            self.cur.execute(query)
            print('dialog has been updated')

    def check_table_dialogs_exists(self):
        query = """CREATE TABLE IF NOT EXISTS dialogs (
                       id SERIAL PRIMARY KEY,
                       id_user VARCHAR(20),
                       message VARCHAR (4096)
               );"""
        with self.con:
            self.cur.execute(query)
            print('Table users has been created or exists')

    def drop_table(self, table_name):
        query = f"""DROP TABLE {table_name}"""
        with self.con:
            self.cur.execute(query)
            print('Users table has been dropped')

    def update_user_active_status(self, id_user, status):
        # request from DB get id_user
        user_exists = self.get_all_from_db(table_name='users', param=f"""WHERE id_user='{id_user}'""")
        if user_exists:
            query = f"UPDATE users SET active='{status}' WHERE id_user='{id_user}'"
            with self.con:
                self.cur.execute(query)
                print('User has been updated')

    def check_user_exist(self, id):
        query = f"""SELECT * FROM users WHERE id_user='{id}'"""
        with self.con:
            self.cur.execute(query)
        user_exists = self.cur.fetchall()
        if user_exists:
            return True
        else:
            return False

    def show_users(self):
        query = """SELECT * FROM users"""
        with self.con:
            self.cur.execute(query)
        print(self.cur.fetchall())

    def get_all_from_db(self, table_name, param=None):
        query=f"""SELECT * FROM {table_name} {param}"""
        with self.con:
            self.cur.execute(query)
        return self.cur.fetchall()