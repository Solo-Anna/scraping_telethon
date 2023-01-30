import re
import time
from datetime import datetime

from db_operations.scraping_db import DataBaseOperations
from patterns._export_pattern import export_pattern
from patterns.pseudo_pattern.pseudo_export_pattern import export_pattern as pseudo_export_pattern
from utils.additional_variables.additional_variables import flood_control_logs_path

def compose_to_str_from_list(data_list):
    sub_str = ''
    for key in data_list:
        sub_str += f"{key}: {', '.join(data_list[key])}; "
    sub_str = sub_str[:-2]
    pass
    return sub_str

def decompose_from_str_to_list(data_str):
    data_dict = {}
    data_list = data_str.split('; ')
    for i in data_list:
        i = i.split(': ')
        key = i[0]
        sub_items = i[1]
        if sub_items:
            data_dict[key] = sub_items.split(', ')
        else:
            data_dict[key] = []
    return data_dict

def compose_simple_list_to_str(data_list, separator):
    return f'{separator}'.join(data_list)

def string_to_list(text, separator):
    return text.split(separator)

def list_to_string(raw_list, separator):
    return separator.join(raw_list)

async def to_dict_from_admin_response(response, fields):
    response_dict = {}
    fields = fields.split(', ')
    for i in range(0, len(fields)):
        response_dict[fields[i]] = response[i]
    return response_dict

def to_dict_from_admin_response_sync(response, fields):
    response_dict = {}
    fields = fields.split(', ')
    for i in range(0, len(fields)):
        response_dict[fields[i]] = response[i]
    return response_dict

async def to_dict_from_temporary_response(response, fields):
    response_dict = {}
    fields = fields.split(', ')
    for i in range(0, len(fields)):
        response_dict[fields[i]] = response[i]
    return response_dict

async def get_pattern(path, pseudo=False):
    print('\n\n---------------------------------------\n\n')
    message = ''
    if pseudo:
        pattern = pseudo_export_pattern
    else:
        pattern = export_pattern
    for key in pattern:
        message += f"{key}:\n"

        if type(pattern[key]) is dict:
            for key2 in pattern[key]:
                message += f"\t{key2}:\n"

                if type(pattern[key][key2]) is dict:
                    for key3 in pattern[key][key2]:
                        message += f"\t\t{key3}:\n"

                        if type(pattern[key][key2][key3]) is dict and pattern[key][key2][key3]:
                            for key4 in pattern[key][key2][key3]:
                                message += f"\t\t\t{key4}:\n"

                                if type(pattern[key][key2][key3][key4]) is dict:
                                    for key5 in pattern[key][key2][key3][key4]:
                                        message += f"\t\t\t\t{key5}:\n"

                                        if type(pattern[key][key2][key3][key4][key5]) is dict:
                                            for key6 in pattern[key][key2][key3][key4][key5]:
                                                message += f"\t\t\t\t\t{key6}:\n"
                                        else:
                                            message += f"\t\t\t\t\t\t{pattern[key][key2][key3][key4][key5]}\n"
                                else:
                                    message += f"\t\t\t\t\t{pattern[key][key2][key3][key4]}\n"
                        else:
                            message += f"\t\t\t{pattern[key][key2][key3]}\n"
                else:
                    message += f"\t\t{pattern[key][key2]}\n"
        else:
            message += f"\t{pattern[key]}\n"

    print(message)
    with open(path, "w", encoding='utf-8') as file:
        file.write(message)
        print('Done')

async def transformTitleBodyBeforeDb(text=None, title=None, body=None):
    if text:
        title = text.partition(f'\n')[0]
        body = text.replace(title, '').replace(f'\n\n', f'\n')
    elif title+body:
        if title:
            title = title
        if body:
            body = body.replace(f'\n\n', f'\n')
    return {'title': title, 'body': body}

async def get_field_for_shorts(presearch_results: list, pattern: str, return_value='match'):
    element_is_not_empty = False
    for element in presearch_results:
        if element:
            element_is_not_empty = True
            for pattern_item in pattern:
                match = re.findall(rf"{pattern_item}", element)
                if match:
                    return {'return_value': return_value, 'element_is_not_empty': element_is_not_empty, 'match': match[0]}
    return {'return_value': '', 'element_is_not_empty': element_is_not_empty, 'match': ''}

async def get_city_vacancy_for_shorts(presearch_results: list, pattern: str, return_value='match'):
    key = ''
    element_is_not_empty = False
    for element in presearch_results:
        if element:
            element_is_not_empty = True
            for key in pattern:
                if type(pattern[key]) is not str:
                    for value in pattern[key]:
                        match = re.findall(rf"{value}", element)
                        if match:
                            return {'return_value': f"{key}, {value}", 'element_is_not_empty': element_is_not_empty, 'match': match[0]}
                else:
                    match = re.findall(rf"{pattern[key]}", element)
                    if match:
                        return {'return_value': f"{key}, {key}", 'element_is_not_empty': element_is_not_empty,
                                'match': match[0]}

    return {'return_value': '', 'element_is_not_empty': element_is_not_empty, 'match': ''}

async def send_message(bot, chat_id, text, parse_mode='html', disable_web_page_preview=True):
    msg = None
    ex = "Flood control"
    while ex.lower() == 'flood control':
        try:
            msg = await bot.send_message(chat_id, text, parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview)
            ex = ''
        except Exception as e:
            ex = e.args[0]

            with open(flood_control_logs_path, "a") as file:
                file.write(f"{datetime.now().strftime('%d-%m-%y %H:%M%S')} Exception {ex}")

            if 'flood control' in ex.lower():
                print("\n--------------\nFlood control\n--------------\n")
                match = re.findall(r"[0-9]{1,4} seconds", ex)
                if match:
                    seconds = match[0].split(' ')[0]
                    time.sleep(int(seconds) + 5)
    return msg

async def edit_message(bot, text, msg, parse_mode='html', disable_web_page_preview=True):
    ex = "Flood control"
    while ex.lower() == 'flood control':
        try:
            msg = await bot.edit_message_text(f"{msg.text}{text}", msg.chat.id, msg.message_id, parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview)
            ex = ''
        except Exception as e:
            ex = e.args[0]

            with open(flood_control_logs_path, "a") as file:
                file.write(f"{datetime.now().strftime('%d-%m-%y %H:%M%S')} Exception {ex}")

            if 'flood control' in ex.lower():
                print("\n--------------\nFlood control\n--------------\n")
                match = re.findall(r"[0-9]{1,4} seconds", ex)
                if match:
                    seconds = match[0].split(' ')[0]
                    time.sleep(int(seconds) + 5)
    return msg

async def get_name_session():
    current_session = DataBaseOperations(None).get_all_from_db(
        table_name='current_session',
        param='ORDER BY id DESC LIMIT 1',
        without_sort=True,
        order=None,
        field='session',
        curs=None
    )
    for value in current_session:
        current_session = value[0]
    return  current_session