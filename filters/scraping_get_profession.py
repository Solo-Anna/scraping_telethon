import re
import time

# from test_text import t_text_body, t_text_title

class Professions:

    def sort_by_profession(self, title, body):

        self.rus_tag = ''

        profession_dict = {
            'tags': {'backend': 0,
                    'frontend': 0,
                    'qa': 0,
                    'fullstack': 0,
                    'designer': 0,
                    'mobile': 0,
                    'pm': 0,
                    'product': 0,
                    'game': 0,
                    'ba': 0,
                    'devops': 0,
                    'marketing': 0,
                    'hr': 0,
                    'ad': 0,
                    'junior': 0,
                     },
            'body': {'backend': 0,
                    'frontend': 0,
                    'qa': 0,
                    'fullstack': 0,
                    'designer': 0,
                    'mobile': 0,
                    'pm': 0,
                    'product': 0,
                    'game': 0,
                    'ba': 0,
                    'devops': 0,
                    'marketing': 0,
                    'hr': 0,
                    'ad': 0,
                    'junior': 0,
                     },
        }

        params = {
            'block': False,
            'profession': '',
            'junior': 0,
            'middle': 0,
            'senior': 0,
        }

        # pattern_contacts = r'http[s]{0,1}:\/\/|\W{1}@[a-z0-9_]{3,}|\+[0-9]{1,13}[(\s-]{0,2}[0-9]{1,10}[)\s-]{0,2}[0-9]{1,7}' \
        #                    r'[\s`-]{0,2}[0-9]{1,5}[\s-]{0,2}[0-9]{1,3}|http[s]{0,1}:\\\\|[a-z\/\\]*\.[a-z]{2,5}|[a-z._-]' \
        #                    r'{3,}@[a-z]{3,10}.[a-z]{2,5}'

        pattern_contacts = r'https://t.me/|\W{0,1}@[a-z0-9_]{3,}|\+[0-9]{1,13}[(\s-]{0,2}[0-9]{1,10}[)\s-]{0,2}[0-9]{1,7}[\s`-]{0,2}[0-9]{1,5}[\s-]{0,2}[0-9]{1,3}|[a-z._-]{3,}@[a-z]{3,10}.[a-z]{2,5}'

        pattern = {
            'backend': ('backend', 'back end', 'back-end', 'бэкэнд', 'бэкенд', 'бэк-энд', 'бэк-енд', 'бекенд',
                           'python', 'scala', 'linux', 'c\+\+', 'php', 'java', 'django', 'docker', 'linux', 'websocket',
                           'pandas', 'flask', r'\Wrust', 'goland', 'golang', 'go developer', 'symfony', 'c#', 'ruby', 'elixir', 'rest api',
                        'restapi', 'kotlin', 'ruby on rails', 'ror', 'c#', 'с#', '.net', 'rails', 'numpy', 'redis',
                        'веб-разработчик', 'веб разработчик', 'веб разработка', 'laravel', 'node.js', 'nodejs', 'node', 'aws'),
            'frontend': ('frontend', 'front end', 'front-end', 'фронтэнд', 'фронтенд', 'фронт-энд', 'фронт-енд',
                            'фронт энд', 'фронт енд', 'javascript', 'html', 'react', 'firebase', 'vue.js', 'vuejs', 'vue',
                            'ether.js', 'etherjs', 'web3.js', 'web3js', 'angular', 'css', '.js', 'jquery', 'ajax'),
            'qa': (' qa', 'qa ', ' aqa ', 'qa-', 'qa/', 'qaauto', 'qa fullstack', 'manual', 'qaengineer', 'qa engineer', 'тестировщик', 'test ',
                   'automation', 'automatic testing', 'автоматизация процессов тестирования', 'тестировщика',
                   'тестированию', 'автоматизация тестирования', 'автотестировании', 'ручном тестировании', 'тестировании', 'auto',
                   'автоматизатора', 'автоматизатор', 'автоматизации тестирования', 'test automation', 'инженер ручного тестирования', 'тестирования'),
            'fullstack': ('fullstack', 'full stack', 'full-stack', 'фуллстэк', 'фуллстек', 'фулстэк', 'фулстек'),
            'designer': ('designer', 'дизайнер', 'ui/ux', 'ui ', 'uikit', 'гейм-дизайнер', 'геймдизайнер'),
            'mobile': ('android', 'ios ', 'flutter', 'kotlin', 'mobile', 'swift', 'андроид'),
            'pm': ('project manager', 'project-manager', 'projectmanager', 'project/manager', 'pm ', 'проджект менеджер', 'проджект-менеджер', 'менеджерпроекта'),
            'product': ('product manager', 'product-manager', 'productmanager', 'продакт менеджер', 'продукт менеджер',
                        'подакт-менеджер', 'продукт-менеджер', 'продактменеджер', 'продуктменеджер', 'business development manager', 'business development'),
            'game': ('game ', r'\Wunity', 'unreal', 'match-3', 'match3', 'pipeline', 'unreal engine'),
            'ba': ('business analyst', 'бизнес аналитик', 'ba ', 'бизнес аналитика', 'бизнесаналитик', 'analyst', ' domo'),
            'devops': ('devops', 'dev ops', 'девопс', 'дев опс', 'sre', 'database reliability engineer', 'site reliability engineer'),
            'marketing': ('smm', 'copyrighter', 'seo', 'marketing', 'sas marketing automation'),
            'hr': ('hr', 'recruiter', 'human'),
            'ad': ('резюме', 'cv ', 'ищу работу', 'ищуработу', 'opentowork', 'фильм на вечер', 'рекомендую', 'хотим рассказать о новых каналах',
                    'skillbox', 'зарабатывать на крипте', 'секретар', 'делопроизводител',
                    'онлайн курс', 'образовательная платформа', 'со скидкой',
                   'бесплатном марафоне', 'это помогает нам стать лучше для вас', 'получайте больше откликов', '3dartist', '3d artist',
                   'бесплатном интенсиве', 'бесплатный интенсив', 'админвещает', 'в онлайн-интенсиве', 'обо мне', 'ish joyi kerak',
                   'geekjob.ru', 'мы не ищем сотрудников', 'поиске работы', 'sales manager', 'salesmanager',
                   'sales_manager', '‼️Как работает этот канал:', 'outstaff'),  #'блоге', 'блог', 'колл-центра',
        }

        level_job = {
            'junior': ('junior', 'джуниор', 'jr', 'стажировка', 'стажировки', 'стажровке'),
            'middle': ('middle', 'миддл'),
            'senior': ('senior', 'сеньор')
        }

        exclude_fullstack = ('position: senior fullstack', 'position: fullstack', 'position: full-stack', 'вакансия: fullstack',
                    'вакансия: full-stack',
                    'senior full-stack developer', 'senior fullstack developer')

        text = str(title) + str(body)
        text = text.lower()
        profession = []

 # ------------------------ check for swear words ------------------------------
        with open('mat2.txt', 'r') as file:
            for line in file:
                line = line.strip()
                match = re.findall(f' {line} ', text)
                if match:
                    print(f'МАТЕРНЫЕ СЛОВА!! {match} in\n{text}')
                    params['block'] = True
                    print(f'\n', params, '107')
                    time.sleep(20)

                    params['tag'] = self.rus_tag

                    return params

# ----------------------check for contacts---------------------------------
        match = re.findall(pattern_contacts, text)
        match += re.findall(r'contacts: ', text)
        print('|| CONTACTS', match)
        if not match:
            params['profession'] = 'no_sort'

            params['tag'] = self.rus_tag

            print(f'\n', params, '113')
            print(f'\nThere is not contacts in the text:\n\n{text}')
            return params

# ---------------- search junior, middle, senior and other params -----------------
        for item in level_job:
            for i in level_job[item]:
                match = re.findall(i, text)
                if match:
                    print(f'*TAG {match}')
                    self.rus_tag += f"TAG = {match}\n"
                params[item] += len(match)

        if params['junior'] and (params['middle'] or params['senior']):
            if params['junior'] > params['middle'] + params ['senior']:
                params['middle'] = 0
                params['senior'] = 0
            else:
                params['junior'] = 0

# ---------------- end search junior, middle, senior and other params -----------------

        text_without_tags = text
        tags = re.findall(r'#[a-zа-я]*\W', text)  # select all tags in text
        for t in tags:
            text_without_tags = text_without_tags.replace(t, '')  # clear text from tags

 # ------------------search by tags --------------------------
        search_body = []
        for pro in pattern:
            for i in pattern[pro]:
                search_body = []
                search_tags = re.findall(f'#{i.strip()}', text)
                if i == 'резюме' or i.strip() == 'cv':  #если находит слово резюме, то проверяет его расположение в контексте
                    pass
                else:
                    search_body = re.findall(i, text_without_tags)

                if search_tags:
                    profession_dict['tags'][pro] += len(search_tags)  # write to dict to tags number of world encountered
                    self.rus_tag += f"TAG {pro} = {search_tags}\n"

                    print(f'*TAG {search_tags} {pro}')

                if search_body:
                    profession_dict['body'][pro] += len(search_body)
                    self.rus_tag += f"TAG {pro} = {search_body}\n"

                    print(f'*TAG {search_body} {pro}')

        params['tag'] = self.rus_tag

        # ------------------------- end search by tags ---------------------------

# ------------------------- search by text without tags ------------------
        for key in profession_dict:
            print(f'profession_dict = {key} = ', profession_dict[key])  # look into dict

        if profession_dict['tags']['ad'] or profession_dict['body']['ad']:  # return ad right away if ad exists
            params['profession'] = 'ad'
            print(f'\n', params, '154')
            return params
            # return 'ad'

        if profession_dict['tags']['backend'] and profession_dict['body']['backend']:
            profession.append('backend')
        if profession_dict['tags']['frontend'] and profession_dict['body']['frontend']:
            profession.append('frontend')
        if profession_dict['tags']['qa'] and profession_dict['body']['qa']:
            profession.append('qa')
        if profession_dict['tags']['fullstack'] and profession_dict['body']['fullstack']:
            profession.append('fullstack')
        if profession_dict['tags']['designer'] and profession_dict['body']['designer']:
            profession.append('designer')
        if profession_dict['tags']['mobile'] and profession_dict['body']['mobile']:
            profession.append('mobile')
        if profession_dict['tags']['pm'] and profession_dict['body']['pm']:
            profession.append('pm')
        if profession_dict['tags']['product'] and profession_dict['body']['product']:
            profession.append('product')
        if profession_dict['tags']['game'] and profession_dict['body']['game']:
            profession.append('game')
        if profession_dict['tags']['ba'] and profession_dict['body']['ba']:
            profession.append('ba')
        if profession_dict['tags']['devops'] and profession_dict['body']['devops']:
            profession.append('devops')
        if profession_dict['tags']['marketing'] and profession_dict['body']['marketing']:
            profession.append('marketing')
        if profession_dict['tags']['hr'] and profession_dict['body']['hr']:
            profession.append('hr')

        print('profession_tags = ', profession)

        t = False

        #----------------------new code ---------------------

        # length = []
        # for i in profession_dict['body']:
        #     if profession_dict['body'][i]>0:
        #         length.append(profession_dict['body'][i])
        # print('length = ', length)
        #
        # profession = []
        # if len(profession) == 1 and len(length) >1:
        #     for i in length:
        #         for key, values in profession_dict['body']:
        #             if values == i:
        #                 profession.append(key)
        #
        #
        #     result_tags = self.find_profession(profession, profession_dict, 'tags')

        if len(profession)>1 or not profession:
            result_tags = self.find_profession(profession, profession_dict, 'tags')
        else:
            if 'backend' in profession:
                for i in exclude_fullstack:
                    if re.findall(i, text):
                        t = True
                        break
                for i in pattern['fullstack']:
                    if re.findall(i, text):
                        t = True
                        break
            if t:
                params['profession'] = 'fullstack'
                print(f'\n', params, '199')
                return params
                # return 'fullstack', junior
            else:
                params['profession'] = profession[0]
                print(f'\n', params, '204')
                return params
                # return profession[0], junior

        if result_tags != 'no_sort':
            params['profession'] = result_tags
            print(f'\n', params, '210')
            return params
            # return result_tags, junior
        else:
            profession = []
            if profession_dict['body']['backend']:
                profession.append('backend')
            if profession_dict['body']['frontend']:
                profession.append('frontend')
            if profession_dict['body']['qa']:
                profession.append('qa')
            if profession_dict['body']['fullstack']:
                profession.append('fullstack')
            if profession_dict['body']['designer']:
                profession.append('designer')
            if profession_dict['body']['mobile']:
                profession.append('mobile')
            if profession_dict['body']['pm']:
                profession.append('pm')
            if profession_dict['body']['product']:
                profession.append('product')
            if profession_dict['body']['game']:
                profession.append('game')
            if profession_dict['body']['ba']:
                profession.append('ba')
            if profession_dict['body']['devops']:
                profession.append('devops')
            if profession_dict['body']['marketing']:
                profession.append('marketing')
            if profession_dict['body']['hr']:
                profession.append('hr')

            print('profession_body = ', profession)

            result_body = self.find_profession(profession, profession_dict, 'body')

            # if result_body == 'backend' and re.findall(r'[^\#]qa', text[0:30]):
            if result_body == 'backend' and re.findall(r'[^#]qa', text[0:30]):
                params['profession'] = 'qa'
                print(f'\n', params, '248')
                return params
                # return 'qa', junior

            # if re.findall(r'[^\#]java|[^\#]python|[^\#]php|[^\#]backend|[^\#]scala', text[0:40]):
            if re.findall(r'[^#]java|[^#]python|[^#]php|[^#]backend|[^#]scala', text[0:40]):
                params['profession'] = 'backend'
                print(f'\n', params, '253')
                return params
                # return 'backend', junior

            max_value = 0
            key = ''
            if result_body == 'no_sort':
                for item in profession_dict['tags']:
                    if profession_dict['tags'][item] > max_value:
                        max_value = profession_dict['tags'][item]
                        key = item
                if key:
                    params['profession'] = key
                    print(f'\n', params, '266')
                    return params
                    # return key, junior
        params['profession'] = result_body
        print(f'\n', params, '270')
        return params
        # return result_body, junior


    def find_profession(self, profession, profession_dict, field):

        profession_final = ''

        if 'fullstack' in profession or profession_dict['body']['fullstack']:
            if 'qa' in profession:
                if 'backend' in profession and (profession_dict['body']['backend'] + profession_dict['tags']['backend']/4 > profession_dict['body']['fullstack'] + profession_dict['tags']['fullstack']) and \
                        (profession_dict['body']['backend'] + profession_dict['tags']['backend']/4 > profession_dict['body']['frontend'] + profession_dict['tags']['frontend']) and \
                        (profession_dict['body']['backend'] + profession_dict['tags']['backend']/4 > profession_dict['body']['qa'] + profession_dict['tags']['qa']):
                    return 'backend'
                elif profession_dict['body']['qa'] + profession_dict['tags']['qa']/2 > profession_dict['body']['frontend'] + profession_dict['tags']['frontend']:
                    return 'qa'
                else:
                    return 'frontend'
            return 'fullstack'

        if 'devops' in profession:
            if 'backend' in profession and 'frontend' in profession:
                if profession_dict[field]['backend']/2 > profession_dict[field]['devops'] and profession_dict[field]['backend']>profession_dict[field]['frontend']:
                    return 'backend'
                elif profession_dict[field]['frontend']>profession_dict[field]['backend']:
                    return 'frontend'

            elif 'backend' in profession and profession_dict[field]['backend']/2 > profession_dict[field]['devops']:
                return 'backend'

            elif 'frontend' in profession and profession_dict[field]['frontend']/2 > profession_dict[field]['devops']:
                return 'frontend'

            elif 'qa' in profession:
                if profession_dict[field]['qa'] / 2 > profession_dict[field]['devops']:
                    return 'qa'

            else:
                return 'devops'
            return 'devops'


        if profession_dict[field]['game']/2 > profession_dict[field]['qa']:
            return 'game'


        if 'qa' in profession:
            if 'backend' in profession and ('frontend' or 'pm' in profession or 'game' in profession or 'ba' in profession):
                if profession_dict[field]['backend'] / 2 > profession_dict[field]['qa'] and profession_dict[field]['backend'] > profession_dict[field]['frontend']:
                    return 'backend'
                elif profession_dict[field]['frontend'] /2 > profession_dict[field]['qa']:
                    return 'frontend'

            elif 'backend' in profession and profession_dict[field]['backend']/2 > profession_dict[field]['qa']:
                return 'backend'

            elif 'frontend' in profession and profession_dict[field]['frontend']/2 > profession_dict[field]['qa']:
                return 'frontend'

            if 'pm' in profession and profession_dict[field]['pm'] >= profession_dict[field]['qa']:
                return 'pm'

            if profession_dict[field]['game']/2 > profession_dict[field]['qa']:
                return 'game'

            if profession_dict[field]['ba']/1.5 > profession_dict[field]['qa']:
                return 'ba'

            else:
                return 'qa'
        # else:
        #     return 'qa'

        if 'mobile' in profession and 'backend' in profession or 'frontend' in profession:
            if profession_dict[field]['backend']/2 > profession_dict[field]['mobile']:
                return 'backend'
            elif profession_dict[field]['frontend']/2 > profession_dict[field]['mobile']:
                return 'frontend'
            return 'mobile'

        if 'game' in profession:
            return 'game'

        if 'backend' in profession and 'frontend' in profession:
            if profession_dict['tags']['backend'] + profession_dict['body']['backend'] > profession_dict['tags']['frontend'] + profession_dict['body']['frontend']:
                return 'backend'
            elif profession_dict['tags']['backend'] + profession_dict['body']['backend'] == profession_dict['tags']['frontend'] + profession_dict['body']['frontend']:
                return 'backend'
            else:
                return 'frontend'

        if 'backend' in profession:
            return 'backend'

        if 'frontend' in profession:
            return 'frontend'

        max_value = 0
        for i in ['pm', 'product', 'ba', 'marketing', 'hr', 'designer']:
            if profession_dict[field][i]>max_value:
                max_value = profession_dict[field][i]
                profession_final = i
        if profession_final:
            return profession_final
        else:
            return 'no_sort'


#
# with open('text.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#
# text = text.split(f'\n', 1)
# t_text_title2 = text[0].lower()
# t_text_body2 = text[1].lower()
#
# print('t_text_title2 = ', t_text_title2)
# print('t_text_body2 = ', t_text_body2)
#
# profession = Professions().sort_by_profession(t_text_title2, t_text_body2)
# print('profession = ', profession)