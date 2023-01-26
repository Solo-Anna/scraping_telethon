import asyncio
import configparser
import json
import os
import psycopg2
from flask import Flask
import random
from db_operations.scraping_db import DataBaseOperations
from utils.additional_variables.additional_variables import admin_database, admin_table_fields
from helper_functions.helper_functions import to_dict_from_admin_response

db=DataBaseOperations(None)

config = configparser.ConfigParser()
config.read("./settings/config.ini")

database = config['DB_local_clone']['database']
user = config['DB_local_clone']['user']
password = config['DB_local_clone']['password']
host = config['DB_local_clone']['host']
port = config['DB_local_clone']['port']
localhost = config['Host']['host']

con = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
)

async def main_endpoints():
    app = Flask(__name__)

    @app.route("/")
    async def hello_world():
        return "It's the empty page"


    @app.route("/get-all-vacancies")
    async def get_all_vacancies():
        all_vacancies = {}
        all_vacancies['vacancies'] = {}
        response = db.get_all_from_db(
            table_name=admin_database,
            param="WHERE profession <> 'no_sort'",
            field=admin_table_fields
        )
        number=0
        for vacancy in response:
            vacancy_dict = await to_dict_from_admin_response(
                response=vacancy,
                fields=admin_table_fields
            )
            if number<100:
                all_vacancies['vacancies'][str(number)] = vacancy_dict
            number += 1
        return json.dumps(all_vacancies)


    @app.route("/get")
    async def hello_world2():
        data = await get_from_db()
        index = random.randrange(0, len(data))
        data = data[index]
        print(data)
        data_dict = {
            'vacancy': {
                'id': data[0],
                'title': data[2],
                'body': data[3],
                'profession': data[4]
            }
        }
        return json.dumps(data_dict, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))

    async def get_from_db():
        cur = con.cursor()
        query = "SELECT * FROM admin_last_session WHERE profession <> 'no_sort'"
        with con:
            cur.execute(query)
        response = cur.fetchall()
        return response

    app.run(host=localhost, port=int(os.environ.get('PORT', 5000)))


def run_endpoints():
    asyncio.run(main_endpoints())

