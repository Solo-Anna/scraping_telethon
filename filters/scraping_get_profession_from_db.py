import re
from datetime import datetime
import pandas as pd
import psycopg2

from settings.database_settings import database, user, password, host, port

def sort_by_profession(title, body):
    check_dictionary = {
        'title': {
            'backend': 0,
            'frontend': 0,
            'devops': 0,
            'developer': 0,
            'fullstack': 0,
            'mobile': 0,
            'pm': 0,
            'ba': 0,
            'designer': 0,
            'qa': 0,
            'analyst': 0,
            'mobile_developer': 0,
            'hr': 0,
            'ad': 0,
            'backend_language': 0,
            'frontend_language': 0,
        },
        'body': {
            'backend': 0,
            'frontend': 0,
            'devops': 0,
            'developer': 0,
            'fullstack': 0,
            'mobile': 0,
            'pm': 0,
            'ba': 0,
            'designer': 0,
            'qa': 0,
            'analyst': 0,
            'mobile_developer': 0,
            'hr': 0,
            'ad': 0,
            'backend_language': 0,
            'frontend_language': 0,
        }
    }

    counter = 1
    counter2 = 1
    pattern_ad = r'ищу\s{0,1}работу|opentowork|\bsmm\b|\bcopyright\w{0,3}\b|\btarget\w{0,3}\b|фильм на вечер|\w{0,2}рекоменд\w{2,5}' \
                 r'хотим рассказать о новых каналах|#резюме|кадровое\s{0,1}агентство|skillbox|' \
                 r'зарабатывать на крипте|\bсекретар\w{0,2}|делопроизводител\w{0,2}'
    pattern_backend = r'back\s{0,1}end|б[е,э]к\s{0,1}[е,э]нд[а-я]{0,2}|backend.{0,1}developer|datascientist|datascience'
    pattern_frontend = r'front.*end|фронт.*[е,э]нд[а-я]{0,2}\B|vue\.{0,1}js\b|\bangular\b'
    pattern_devops = r'dev\s*ops|sde|sre|Site\s{0,1}reliability\s{0,1}engineering'
    # pattern_developer = r'^(frontend|backend)\s{0,1}developer|разработчик[а-я]{0,2}\B|site\s*reliability|typescript'
    pattern_backend_mobile = r'android|ios|flutter'
    pattern_fullstack = r'full.{0,1}stack'
    pattern_pm = r'product\s*manager|прод[а,у]кт\s*м[е,а]н[е,а]джер|project\s*manager|marketing\s*manager|marketing'
    pattern_designer = r'дизайнер[а-я]{0,2}\B|designer|\bui\s'
    pattern_analitic = r'analyst|аналитик[а-я]{0,2}'
    pattern_qa = r'qa\b|тестировщик[а-я]{0,2}|qaauto\b|тестирован[а-я]{0,2}'
    pattern_hr = r'\bhr\b|рекрутер[а-я]{0,2}\B'
    pattern_project_m = r'project[\W,\s]{0,1}manager|проджект[\W,\s]{0,1}менеджер\w{0,2}|marketing[\W,\s]{0,1}manager'
    pattern_product_m = r'product[\W,\s]{0,1}manager|прод[а,у]кт[\W,\s]{0,1}м[е,а]н[е,а]джер\w{0,2}|marketing[\W,\s]{0,1}manager'
# ---------------languages--------------------------------
    pattern_backend_languages = r'python[\s,#]|scala[\s,#]|java[\s,#]|linux[\s,#]|haskell[\s,#]|php[\s,#]|server|' \
                                r'\bсервер\w{0,3}\b|c\+\+|\bml\b|\bnode.{0,1}js\b|docker|java\/{0,1}|scala\/{0,1}|cdn|docker|websocket\w{0,1}'
    pattern_frontend_languages = r'javascript|html|css|react\s*js|firebase|\bnode.{0,1}js\b|vue\.{0,1}js|aws|amazon\s{0,1}ws|ether\.{0,1}js|web3\.{0,1}js|angular'
#---------------------------------------------------------

    text = [title.lower(), body.lower()]
    text_field = ['title', 'body']

    k = 0
    for item in text:
        looking_for = re.findall(pattern_ad, item)
        if looking_for:
            check_dictionary[text_field[k]]['ad'] += len(looking_for)

        looking_for = re.findall(pattern_backend, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['backend'] += len(looking_for)

        looking_for = re.findall(pattern_frontend, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['frontend'] += len(looking_for)

        looking_for = re.findall(pattern_devops, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['devops'] += len(looking_for)

        looking_for = re.findall(pattern_backend_mobile, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['mobile'] += len(looking_for)

        looking_for = re.findall(pattern_fullstack, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['fullstack'] += len(looking_for)

        # looking_for = re.findall(pattern_developer, item)
        # if looking_for:
        #     counter += 1
        #     check_dictionary[text_field[k]]['developer'] += len(looking_for)

        looking_for = re.findall(pattern_pm, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['pm'] += len(looking_for)

        looking_for = re.findall(pattern_designer, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['designer'] += len(looking_for)

        looking_for = re.findall(pattern_analitic, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['analyst'] += len(looking_for)

        looking_for = re.findall(pattern_qa, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['qa'] += len(looking_for)

        looking_for = re.findall(pattern_hr, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['hr'] += len(looking_for)

#----------------------------langueges-------------------------
        looking_for = re.findall(pattern_backend_languages, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['backend_language'] += len(looking_for)

        looking_for = re.findall(pattern_frontend_languages, item)
        if looking_for:
            counter += 1
            check_dictionary[text_field[k]]['frontend_language'] += len(looking_for)
# ----------------------------------------------------------------
        else:
            counter2 += 1

        k += 1

    profession = analys_profession(check_dictionary)

    return profession

def analys_profession(check_dictionary):
    # max_title_value = 0
    # max_title_key = ''
    #
    # for key in check_dictionary['title']:
    #     if check_dictionary['title'][key] > max_title_value:
    #         max_title_value = check_dictionary['title'][key]
    #         max_title_key = key
    #
    # max_body_value = 0
    # max_body_key = ''
    # for key in check_dictionary['body']:
    #     if check_dictionary['body'][key] > max_body_value:
    #         max_body_value = check_dictionary['body'][key]
    #         max_body_key = key
    #
    # print(check_dictionary)
    #
    # print('title', max_title_key, max_title_value)
    # print('body', max_body_key, max_body_value)
    #
    # profession = ''
    #
    # # if max_title_value == 0 and max_body_value == 0:
    # #     profession = 'ad'
    #
    # if max_title_value == 0 and max_body_value != 0:
    #     profession = max_body_key  # все случаи совпадения значений ключей
    #
    # elif max_title_key in ['frontend', 'backend'] and max_body_key == 'developer':
    #     profession = max_title_key
    #
    # elif max_title_key != max_body_key and max_body_value != 0:
    #     profession = max_body_key
    #
    # elif max_title_key and not max_body_key and max_body_value == 0:
    #     profession = max_title_key
    #
    # elif max_title_key == max_body_key:
    #     profession = max_title_key
    #
    # elif check_dictionary['title']['fullstack'] or check_dictionary['body']['fullstack']:
    #     profession = 'fullstack'
    #
    # if max_title_key == 'qa' and max_body_key in ['backend', 'frontend', 'fullstack']:
    #     profession = 'qa'
    #
    # if check_dictionary['title']['fullstack'] or check_dictionary['body']['fullstack']:
    #     profession = 'fullstack'
    #
    # if max_title_key == 'devops' and (max_body_key == 'backend' or max_body_key == 'frontend'):
    #     profession = max_title_key
    #
    # if check_dictionary['title']['mobile'] or check_dictionary['body']['mobile']:
    #     profession = 'mobile'
    #
    # if check_dictionary['title']['ad']:
    #     profession = 'ad'

    backend = check_dictionary['title']['backend'] + check_dictionary['body']['backend']
    frontend = check_dictionary['title']['frontend'] + check_dictionary['body']['frontend']
    devops = check_dictionary['title']['devops'] + check_dictionary['body']['devops']
    fullstack = check_dictionary['title']['fullstack'] + check_dictionary['body']['fullstack']
    pm = check_dictionary['title']['pm'] + check_dictionary['body']['pm']
    ba = check_dictionary['title']['ba'] + check_dictionary['body']['ba']
    designer = check_dictionary['title']['designer'] + check_dictionary['body']['designer']
    qa = check_dictionary['title']['qa'] + check_dictionary['body']['qa']
    analyst = check_dictionary['title']['analyst'] + check_dictionary['body']['analyst']
    mobile = check_dictionary['title']['mobile'] + check_dictionary['body']['mobile']
    hr = check_dictionary['title']['hr'] + check_dictionary['body']['hr']
    ad = check_dictionary['title']['ad'] + check_dictionary['body']['ad']
    backend_language = check_dictionary['title']['backend_language'] + check_dictionary['body']['backend_language']
    frontend_language = check_dictionary['title']['frontend_language'] + check_dictionary['body']['backend_language']

    profession = []

    pro = ''
    if ((devops and backend and frontend) or (devops and backend and not frontend) or (devops and frontend and not backend)) and (backend_language>5 and backend_language>5):
        profession = ['fullstack']

    if frontend:
        profession.append('frontend')

    if backend:
        profession.append('backend')

    if (frontend and backend) and (frontend_language or backend_language): # and not fullstack:
        if frontend_language/2 > backend_language:
            pro = 'frontend'
        else:
            pro = 'backend'
        profession = [pro]

#--------------------------------------------------------------

    if backend and not frontend: #and not fullstack:
        if backend_language and frontend_language:
            if frontend_language/2>backend_language:
                pro = 'frontend'
            else:
                pro = 'backend'

        elif frontend_language and not backend_language:
            pro = 'frontend'

        else:
            pro= 'backend'
        profession = [pro]

    # --------------------------------------------------------------

    if frontend and not backend: # and not fullstack:
        if backend_language and frontend_language:
            if backend_language / 2 > frontend_language:
                pro = 'backend'
            else:
                pro = 'frontend'

        elif backend_language and not frontend_language:
            pro = 'backend'

        else:
            pro = 'frontend'

        profession = [pro]

    # --------------------------------------------------------------

    if fullstack:
        profession.append('fullstack')

    if qa:
        profession.append('qa')

    if devops and 'fullstack' not in profession:
        profession.append('devops')

    if pm:
        profession.append('pm')

    if mobile:
        profession.append('mobile')

    if ba:
        profession.append('ba')

    if designer:
        profession.append('designer')

    if analyst:
        profession.append('analyst')

    if ad:
        profession = ['ad',]

    return profession


def write_to_db():





    # title = i4.partition(f'\n')[0]
    # body = i4.replace(title, '').replace(f'\n\n', f'\n')
    #
    # d = sort_by_profession(title, body)
    # print(d)
    con = None
    r = None
    try:
        con = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
    except:
        print('No connect with db')

    cur = con.cursor()
    query = f"""SELECT * FROM telegram_channels_professions"""
    with con:
        try:
            cur.execute(query)
            r = cur.fetchall()
        except Exception as e:
            print(e)
    n=1
    for i in r:
        title = i[2]
        body = i[3]
        profession = sort_by_profession(title, body)
        print(f'{title}\n{body}')
        print(f'!!!!!!!!!!!!!!!!!!{n} -- {profession}')
        n += 1
        if not profession:
            pass

        for pro in profession:
            with con:
                cur.execute(f"""CREATE TABLE IF NOT EXISTS {pro} (
                    id SERIAL PRIMARY KEY,
                    chat_name VARCHAR(150),
                    title VARCHAR(1000),
                    body VARCHAR (6000),
                    profession VARCHAR (30),
                    time_of_public TIMESTAMP,
                    created_at TIMESTAMP
                    );"""
                            )
                con.commit()
                new_post = f"""INSERT INTO {pro} (chat_name, title, body, profession, time_of_public, created_at)
                                            VALUES ('{i[1]}', '{title}', '{body}', '{pro}', '{i[5]}', '{datetime.now()}');"""
                cur.execute(new_post)
                con.commit()
                print('Message pushed to db')

def write_to_excel():
    profession = ['backend', 'frontend', 'devops', 'fullstack', 'pm', 'designer', 'qa', 'analyst', 'mobile', 'ad']
    con = None
    try:
        con = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
    except:
        print('No connect with db')
    cur = con.cursor()
    for pro in profession:
        query = f"""SELECT * FROM {pro}"""
        with con:
            try:
                cur.execute(query)
                result = cur.fetchall()
            except Exception as e:
                print(e)

        df = pd.DataFrame(
            {
                'Channel': [channel[1] for channel in result],
                'Title': [title[2] for title in result],
                'Body': [body[3] for body in result],
                'Profession': [p[4] for p in result],
                'Create Date': [c_date[5] for c_date in result],
                'Push Date': [p_date[6] for p_date in result]
            }
        )
        df.to_excel(f'{pro}.xlsx')


write_to_excel()

