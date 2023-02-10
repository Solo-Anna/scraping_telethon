import asyncio
import configparser
import datetime
import json
import os
import psycopg2
from flask import Flask
import random
from db_operations.scraping_db import DataBaseOperations
from utils.additional_variables.additional_variables import admin_database, admin_table_fields
from helper_functions.helper_functions import to_dict_from_admin_response
from flask_cors import CORS
from flask import request
from utils.additional_variables.additional_variables import path_post_request_file, post_request_for_example, valid_professions
from patterns._export_pattern import export_pattern
from patterns.data_pattern._data_pattern import pattern
from filters.filter_jan_2023.filter_jan_2023 import VacancyFilter
from helper_functions import helper_functions as helper
from utils.additional_variables import additional_variables as variable
import requests

db=DataBaseOperations(None)
vacancy_search = VacancyFilter()
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
    CORS(app)

    @app.route("/")
    async def hello_world():
        return "It's the empty page"

    @app.route("/get-all-vacancies")
    async def get_all_vacancies():
        return await get_all_vacancies_from_db()

    @app.route("/get-all-vacancies-admin")
    async def get_all_vacancies_admin():
        response = await get_all_vacancies_from_db()
        # response['pattern'] = await get_export_pattern_dict()
        return response

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

    @app.route("/post-vacancies", methods = ['POST'])
    async def post_data():
        request_data = request.json
        await write_to_file(text=request_data)
        # request_data = post_request_for_example
        all_vacancies = await compose_request_to_db(request_data)
        # return {'It works': request_data}
        return all_vacancies

    @app.route("/search-by-text", methods = ['POST'])
    async def search_by_text():
        responses_dict = {}
        request_data = request.json
        # profession = vacancy_search.sort_profession(
        #     title=request_data['filter_request'],
        #     body='',
        #     check_contacts=False,
        #     check_vacancy=False,
        #     check_profession=True
        # )
        param = "WHERE"
        if request_data['vacancy']:
            request_data['vacancy'] = request_data['vacancy'].lower()
            if param[-1:] == "'":
                param += f" AND"
            param += f" LOWER(vacancy) LIKE '%{request_data['vacancy']}%'"

        if request_data['level']:
            request_data['level'] = request_data['level'].lower()
            if param[-1:] == "'":
                param += f" AND"
            param += f" LOWER(profession) LIKE '%{request_data['level']}%'"


        if request_data['profession']:
            request_data['profession'] = request_data['profession'].lower()
            if param[-1:] == "'":
                param += f" AND"
            param += f" LOWER(profession) LIKE '%{request_data['profession']}%'"

        if request_data['language']:
            request_data['language'] = request_data['language'].lower()
            if param[-1:] == "'":
                param += " AND"
            param += f" (LOWER(title) LIKE '%{request_data['language']}%' or LOWER(body) LIKE '%{request_data['language']}%')"

        today = datetime.datetime.now()
        date_from = (today - datetime.timedelta(days=variable.vacancy_fresh_time_days)).strftime("%Y-%m-%d")
        param += f" AND DATE(created_at) > '{date_from}'"
        # param = f"WHERE DATE(created_at) > '{date_from}'"

        responses = db.get_all_from_db(
            table_name=variable.admin_database,
            param=param,
            without_sort=False,
            field=variable.admin_table_fields
        )
        if responses and type(responses) is not str:
            count = 0
            for response in responses:
                response_dict = await helper.to_dict_from_admin_response(
                    response=response,
                    fields=variable.admin_table_fields
                )
                responses_dict[count] = {}
                responses_dict[count] = response_dict
                count +=1
                if count>=10:
                    break
            # await write_to_file(text=request_data)
            print(len(responses))
            return {
                "vacancies_number": len(responses),
                "vacancies": responses_dict
            }
        return {
            "vacancies_number": 0,
            "vacancies": ""
        }

    async def get_from_db():
        cur = con.cursor()
        query = "SELECT * FROM admin_last_session WHERE profession <> 'no_sort'"
        with con:
            cur.execute(query)
        response = cur.fetchall()
        return response

    async def get_all_vacancies_from_db(param="WHERE profession <> 'no_sort'"):
        all_vacancies = {}
        all_vacancies['vacancies'] = {}
        response = db.get_all_from_db(
            table_name=admin_database,
            param=param,
            field=admin_table_fields
        )
        number = 0
        print(param)
        for vacancy in response:
            vacancy_dict = await to_dict_from_admin_response(
                response=vacancy,
                fields=admin_table_fields
            )
            if number < 100:
                all_vacancies['vacancies'][str(number)] = vacancy_dict
            number += 1
        return all_vacancies

    async def write_to_file(text):
        with open(path_post_request_file, 'a', encoding='utf-8') as file:
            file.write(f"{str(text)}\n-----------\n")

    async def get_export_pattern_dict():
        dict_pattern = {}
        for profession in export_pattern['professions']:
            dict_pattern[profession] = {}
            if 'ma' not in dict_pattern[profession]:
                dict_pattern[profession]['ma'] = []

            dict_pattern[profession]['ma'] = list(export_pattern['professions'][profession]['ma'])
            for sub in export_pattern['professions'][profession]['sub']:
                if 'sub' not in dict_pattern[profession]:
                    # dict_pattern[profession] = {}
                    dict_pattern[profession]['sub'] = {}

                if sub not in dict_pattern[profession]['sub']:
                    dict_pattern[profession]['sub'][sub] = {}
                    dict_pattern[profession]['sub'][sub]['ma'] = []

                dict_pattern[profession]['sub'][sub]['ma'] = list(export_pattern['professions'][profession]['sub'][sub]['ma'])
        return dict_pattern

    async def compose_request_to_db(response_data):
        query_profession = ""
        common_query = "WHERE "
        query_job_type = ""
        if response_data['profession']:
            for item in response_data['profession']:
                query_profession += f"OR profession LIKE '%{item}%' "
        if 'junior' in response_data['level']:
            query_profession += f"OR profession LIKE '%junior%'"
        if 'all' in response_data['level']:
            query_profession = ''
            for item in valid_professions:
                query_profession += f"OR profession LIKE '%{item}%' "
        query_profession = f"({query_profession[3:]})"

        common_query += query_profession

        if response_data['city']:
            common_query += f" AND city LIKE '%{response_data['city']}%'"

        # if response_data['job_type']:
        #     for item in response_data['job_type']:
        #         query_job_type += f"OR job_type LIKE '%{item}%' "
        #         query_job_type = query_job_type[3:]
        #     common_query += f"AND {query_job_type}"

        all_vacancies = await get_all_vacancies_from_db(param=common_query)

        return all_vacancies



    app.run(host=localhost, port=int(os.environ.get('PORT', 5000)))


def run_endpoints():
    asyncio.run(main_endpoints())

