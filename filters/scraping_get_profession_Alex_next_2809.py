"""
It is the new pattern from Alexander
"""

import re
from __backup__ import pattern_Alex2809
from db_operations.scraping_db import DataBaseOperations
from __backup__.pattern_Alex2809 import search_companies, search_companies2, english_pattern, remote_pattern, \
    relocate_pattern, vacancy_pattern


class AlexSort2809:

    def __init__(self):
        self.pattern_alex = pattern_Alex2809.pattern
        self.capitalize = ['pm', 'game', 'designer', 'hr', 'analyst', 'qa', 'ba', 'product']

        self.result_dict2 = {'vacancy': 0, 'contacts': 0, 'fullstack': 0, 'frontend': 0, 'backend': 0, 'pm': 0,
                             'mobile': 0, 'game': 0, 'designer': 0, 'hr': 0, 'analyst': 0, 'qa': 0, 'ba': 0,
                             'product': 0, 'devops': 0, 'marketing': 0, 'sales_manager': 0, 'junior': 0, 'middle': 0,
                             'senior': 0}

        self.keys_result_dict = ['fullstack', 'frontend', 'qa', 'ba', 'backend', 'pm', 'mobile', 'game', 'designer',
                                 'hr', 'analyst', 'product', 'devops', 'marketing', 'sales_manager']
        self.valid_profession_list = ['marketing', 'ba', 'game', 'product', 'mobile',
                                      'pm', 'sales_manager', 'analyst', 'frontend',
                                      'designer', 'devops', 'hr', 'backend', 'frontend', 'qa', 'junior']



    def sort_by_profession_by_Alex(self, title, body, check_contacts=True, check_profession=True, check_vacancy=True, get_params=True):
        profession = dict()
        profession['tag'] = ''
        profession['anti_tag'] = ''
        profession['profession'] = []
        params = {}
        vacancy = f"{title}\n{body}"

        # if it is not vacancy, return no_sort
        if check_profession:
            if check_vacancy:
                result = self.check_parameter(pattern=pattern_Alex2809.pattern['vacancy'], vacancy=vacancy, key='vacancy')
                self.result_dict2['vacancy'] = result['result']
                profession['tag'] += result['tags']
                profession['anti_tag'] += result['anti_tags']

                if not self.result_dict2['vacancy']:
                    profession['profession'] = {'no_sort'}
                    print(f"line84 {profession['profession']}")
                    print("= vacancy not found =")
                    return {'profession': profession, 'params': {}}

            # if it is without contact, return no_sort
            if check_contacts:
                result = self.check_parameter(pattern=pattern_Alex2809.pattern['contacts'], vacancy=vacancy, key='contacts')
                self.result_dict2['contacts'] = result['result']
                profession['tag'] += result['tags']
                profession['anti_tag'] += result['anti_tags']

                if not self.result_dict2['contacts']:
                    profession['profession'] = {'no_sort'}
                    print(f"not contacts {profession['profession']}")

                    print("= contacts not found =")
                    return {'profession': profession, 'params': {}}

            # ---------------- professions -----------------

            for item in self.valid_profession_list:
                if item in ['pm', 'game', 'designer', 'hr', 'analyst', 'qa', 'ba' 'devops', 'product']:
                    low = False
                else:
                    low = True
                if item == 'product':
                    item = 'pm'
                result = self.check_parameter(pattern=pattern_Alex2809.pattern[item], vacancy=vacancy, low=low, key=item)
                if result['result']:
                    profession['profession'].append(result['result'])
                    print(f"in loop: {profession['profession']}")
                profession['tag'] += result['tags']
                profession['anti_tag'] += result['anti_tags']

            if 'fullstack' in profession['profession']:
                profession = self.transform_fullstack_to_back_and_front(text=vacancy, profession=profession)

            if not profession['profession']:
                profession['profession'] = ['no_sort']
                print(f"line84 {profession['profession']}")

            profession['profession'] = set(profession['profession'])

        if get_params:
            params = self.get_params(text=vacancy, profession=profession)

        print(f"FINALLY: {profession['profession']}")
        return {'profession': profession, 'params': params}


    def check_parameter(self, pattern, vacancy, key, low=True):
        result = 0
        tags = ''
        anti_tags = ''

        if low:
            vacancy = vacancy.lower()

        for word in pattern['ma']:
            if low:
                word = word.lower()

            match = set(re.findall(rf"{word}", vacancy))

            if match:
                result += len(match)
                tags += f'MA {key}={match}\n'

        if result:
            for anti_word in pattern['mex']:
                if low:
                    anti_word = anti_word.lower()

                match = set(re.findall(rf"{anti_word}", vacancy))
                if match:
                    result = 0
                    anti_tags += f'MEX {key}={match}\n'
                    break
        else:
            anti_tags = ''

        return {'result': key if result else '', 'tags': tags, 'anti_tags': anti_tags}


    def get_params(self, text, profession, all_fields_null=False):
        params = {}
        params['company'] = self.get_company_new(text)
        params['job_type'] = self.get_remote_new(text)
        params['job_type'] = self.get_remote_new(text)
        params['relocation'] = self.get_relocation_new(text)
        params['english'] = self.english_requirements_new(text)
        params['vacancy'] = self.get_vacancy_name(text, profession['profession'])

        return params

    def sort_by_profession_by_Alex2(self, title, body, companies=None, get_params=True, only_profession=False):
        params = {}
        new_pattern_has_done = False


        profession = []
        profession_dict = {}

        self.tag_alex = ''
        self.tag_alex_anti = ''

        message = f'{title}\n{body}'
        # match = re.findall(rf"{contacts_pattern}", message)
        # if match:
        #     self.result_dict2['contacts'] = 1
        # else:
        #     pass
        # ----------------- Check for used capitalize or don't ------------------
        for i in self.pattern_alex:
            if i not in ['internship', 'remote', 'relocate', 'country', 'city']:
                # if i in ['backend',]:
                #     match = re.findall(profession_new_pattern[i], message)
                #     if match:
                #         print(f'{i}: сработал новый паттерн')
                #         self.result_dict2[i] = len(match)
                #         new_pattern_has_done = True
                #     else:
                #         new_pattern_has_done = False

                if i in ['pm', 'game', 'designer', 'hr', 'analyst', 'qa', 'ba', 'product']:
                    capitalize = True
                else:
                    capitalize = False

                if not new_pattern_has_done:
                    self.get_profession(message, capitalize, key=i)
                # new_pattern_has_done = False

                if not only_profession:
                    if i == 'contacts' and self.result_dict2['contacts'] == 0:
                        print('*****************NO CONTACTS!!!!!!!!!')
                        profession = ['no_sort']
                        break
                    if i == 'vacancy' and self.result_dict2['vacancy'] == 0:
                        print('*****************NO VACANCY!!!!!!!!!')
                        profession = ['no_sort']
                        break


        for i in self.result_dict2:
            if self.result_dict2[i]:
                profession.append(i)
        pass

#------------------- вывести в консоль result_dict ----------------------
        # for i in self.result_dict2:
        #     print(f'{i}: {self.result_dict2[i]}')

# ---------------- delete not used keys and values as contact and vacancy -------------------
        k=0
        while k<len(profession):
            if profession[k] in ['vacancy', 'contacts']:
                profession.pop(k)
            else:
                k += 1

        profession = set(profession)
        skills = {'middle', 'senior', 'junior'}
        names_profession = {'backend', 'frontend', 'devops', 'pm', 'product', 'designer', 'analyst',
                                    'fullstack', 'mobile', 'qa', 'hr', 'game', 'ba', 'marketing',
                                    'sales_manager'}
        if skills.intersection(profession) and not names_profession.intersection(profession):
            profession = {'no_sort'}

# -------------- collect dict for return it to main code ----------------
        profession_dict['profession'] = profession
        profession_dict['tag'] = self.tag_alex
        profession_dict['anti_tag'] = self.tag_alex_anti
        profession_dict['block'] = False  # заглушки для кода, который вызывает этот класс
        profession_dict['junior'] = 0
        profession_dict['middle'] = 0
        profession_dict['senior'] = 0

        if not profession_dict['profession']:
            profession_dict['profession'] = {'no_sort'}

        if get_params:
            text = f"{title}\n{body}"
            params['company'] = []
            # search company
            params['company'] = self.get_company_new(text)
            # if not profession_dict['company']:
            #     profession_dict['company'] = params['company']

            params['job_type'] = self.get_remote_new(text)
            # if not profession_dict['job_type']:
            #     profession_dict['job_type'] = params['job_type']

            # params['city'] = self.get_city(title, body)
            params['relocation'] = self.get_relocation_new(text)
            # if not profession_dict['relocation']:
            #     profession_dict['relocation'] = params['relocation']

            params['english'] = self.english_requirements_new(text)
            # if not profession_dict['english']:
            #     profession_dict['english'] = params['english']

            params['vacancy'] = self.get_vacancy_name(text, profession_dict['profession'])
            # if not profession_dict['vacancy']:
            #     profession_dict['vacancy'] = params['vacancy']

        return {'profession': profession_dict, 'params': params}

    def get_profession(self, message, capitalize, key):
        message_to_check = ''
        link_telegraph = ''
# --------------- collect all matches in 'ma' -----------------------
        for word in self.pattern_alex[key]['ma']:

            if not capitalize:
                word = word.lower()
                message_to_check = message.lower()
            else:
                message_to_check = message

            match = re.findall(word, message_to_check)
            if match:
                self.tag_alex += f'TAG {capitalize} {key}={match}\n'
                # print(f'TAG {key} = {match}')

                self.result_dict2[key] += len(match)


# -------------- cancel all matches if it excludes words ------------------
#         print('key = ', key)
        if self.result_dict2[key]:
            for exclude_word in self.pattern_alex[key]['mex']:
                # print('exclude_word = ', exclude_word)
                if not capitalize:
                    exclude_word = exclude_word.lower()
                    message_to_check = message.lower()
                else:
                    message_to_check = message

                # print('exclude_word = ', exclude_word)
                # print('message_to_check = ', message_to_check)

                match = re.findall(rf"{exclude_word}", message_to_check)
                if match:
                    self.tag_alex_anti += f'TAG ANTI {key}={match}\n'
                    # print(f'ANTI TAG {capitalize} {key} = {match}')
                    self.result_dict2[key] = 0


            if self.result_dict2['fullstack']:
                self.transform_fullstack_to_back_and_front(message)

            #     message_to_check = message.lower()
            #     for exclude_word in self.pattern_alex['backend']['mex']:
            #         exclude_word = exclude_word.lower()
            #         match = re.findall(rf"{exclude_word}", message_to_check)
            #         if match:
            #             self.tag_alex_anti += f'TAG ANTI backend={match}\n'
            #             # print(f'ANTI TAG {capitalize} {key} = {match}')
            #             self.result_dict2['fullstack'] = 0
            #         else:
            #             self.result_dict2['backend'] += 1
            #
            #     for exclude_word in self.pattern_alex['frontend']['mex']:
            #         exclude_word = exclude_word.lower()
            #         match = re.findall(rf"{exclude_word}", message_to_check)
            #         if match:
            #             self.tag_alex_anti += f'TAG ANTI frontend={match}\n'
            #             # print(f'ANTI TAG {capitalize} {key} = {match}')
            #             self.result_dict2['fullstack'] = 0
            #         else:
            #             self.result_dict2['frontend'] += 1
            #
            # self.result_dict2['fullstack'] = 0

    def transform_fullstack_to_back_and_front(self, text, profession):

        for anti_word in self.pattern_alex['backend']['mex']:
            match = re.findall(rf"{anti_word.lower()}", text.lower())
            if match:
                profession['anti_tag'] += f'TAG ANTI backend={match}\n'
            else:
                profession['profession'].add('backend')

        for anti_word in self.pattern_alex['frontend']['mex']:
            match = re.findall(rf"{anti_word.lower()}", text.lower())
            if match:
                profession['anti_tag'] += f'TAG ANTI frontend={match}\n'
            else:
                profession['profession'].add('frontend')

        profession['profession'].discard('fullstack')

        return profession

    def transform_fullstack_to_back_and_front2(self, message):

        message_to_check = message.lower()
        for exclude_word in self.pattern_alex['backend']['mex']:
            exclude_word = exclude_word.lower()
            match = re.findall(rf"{exclude_word}", message_to_check)
            if match:
                self.tag_alex_anti += f'TAG ANTI backend={match}\n'
                # print(f'ANTI TAG {capitalize} {key} = {match}')
                self.result_dict2['fullstack'] = 0
            else:
                self.result_dict2['backend'] += 1

        for exclude_word in self.pattern_alex['frontend']['mex']:
            exclude_word = exclude_word.lower()
            match = re.findall(rf"{exclude_word}", message_to_check)
            if match:
                self.tag_alex_anti += f'TAG ANTI frontend={match}\n'
                # print(f'ANTI TAG {capitalize} {key} = {match}')
                self.result_dict2['fullstack'] = 0
            else:
                self.result_dict2['frontend'] += 1

        self.result_dict2['fullstack'] = 0

    def get_company_new(self, text):
        company = ''
        companies_from_db = DataBaseOperations(None).get_all_from_db(
            table_name='companies',
            without_sort=True
        )
        for i in companies_from_db:
            if i[1] in text:
                return i[1]

        match = re.findall(rf"{search_companies}", text)
        if match:
            return self.clean_company_new(match[0])

        match = re.findall(rf"{search_companies2}", text)
        if match:
            return match[0]

        # if company1 and company2 and company1 != company2:
        #     company = company2
        # elif company1 and company3 and company1 != company3:
        #     company = company3

        return ''

    def get_company(self, title, body, companies):  # new code
        text = title+body
        company = []

        # companies = DataBaseOperations(con=None).get_all_from_db('companies', without_sort=True)
        for comp in companies:
            el = comp[1]
            match = re.findall(el, text)
            if match:
                company.append(match)

        if not company:
            for param in pattern_Alex2809.params['company']:
                match = re.findall(rf'{param}', text)
                if match:
                    company.append(match)
        company = self.check_clear_element(company) # transform to string
        return company

    def english_requirements_new(self, text):
        match = re.findall(english_pattern, text)
        if match:
            match = match[0].replace('\n', '').replace('"', '').replace('#', '').replace('.', '')
            match = match.strip()
            if match[-1:] == '(':
                match = match[:-1]
            # print('match = ', match)
        else:
            match = ''

        return match


    def english_requirements(self, title, body):
        text = title + body
        english = []
        for param in pattern_Alex2809.params['english_level']:
            match = re.findall(rf'{param}', text)
            if match:
                english.append(match)
        english = self.check_clear_element(english) # transform to string
        return english

    def get_relocation_new(self, text):
        match = re.findall(relocate_pattern, text)
        if match:
            return match[0]
        else:
            return ''

    def get_remote_new(self, text):
        match = re.findall(remote_pattern, text)
        if match:
            return match[0]
        else:
            return ''

    def work_type_fulltime(self, title, body):
        text = title+body
        fulltime = []
        for param in pattern_Alex2809.params['job_type']:
            match = re.findall(param, text)
            if match:
                fulltime.append(match)
        fulltime = self.check_clear_element(fulltime) # transform to string
        return fulltime

    def get_relocation(self, title, body):
        text = title+body
        relocation = []
        for param in pattern_Alex2809.params['relocation']:
            match = re.findall(param, text)
            if match:
                relocation.append(match)
        relocation = self.check_clear_element(relocation) # transform to string
        return relocation

    def get_city(self, title, body):
        text = title+body
        city = []
        for key in pattern_Alex2809.cities_pattern:
            for param in pattern_Alex2809.cities_pattern[key]:
                match = re.findall(param, text)
                if match:
                    city.append(match)
        city = self.check_clear_element(city) # transform to string
        return city

    def clean_company_new(self, company):
        pattern = "^[Cc]ompany[:]{0,1}|^[Кк]омпания[:]{0,1}" #clear company word
        pattern_russian = "[а-яА-Я\s]{3,}"
        pattern_english = "[a-zA-Z\s]{3,}"

        # -------------- if russian and english, that delete russian and rest english -----------
        if re.findall(pattern_russian, company) and re.findall(pattern_english, company):
            match = re.findall(pattern_english, company)
            company = match[0]

        # -------------- if "company" in english text, replace this word
        match = re.findall(pattern, company)
        if match:
            company = company.replace(match[0], '')

        return company.strip()

    def clean_company(self, company_list):
        elements_list = []
        if type(company_list) in [tuple, list, set]:
            for elements in company_list:
                for element in elements:
                    e = re.sub(r'[Кк]омпан[иi][яий][:\-\s]{0,3}|[Cc]ompany[:\-\s]{0,3}|[Р,р]аботодатель[:\-\s]{0,3}', '', str(element))
                    if e:
                        elements_list.append(e)
        else:
            elements_list = company_list
        return elements_list

    def check_clear_element(self, element):
        if element == []:
            return ''
        for i in range(0, 3):
            if type(element) in [list, tuple, set]:
                element = element[0]
            else:
                return element

    def get_content_from_telegraph(self, link_telegraph):
        # print('link_telegraph = ', link_telegraph)
        """
        parsing
        """
        pass

    def get_vacancy_name(self, text, profession_list):
        vacancy = ''
        match = re.findall(rf"{vacancy_pattern['common_vacancy']}", text)
        if match:
            vacancy = match[0]
        else:
            for pro in profession_list:
                if pro == 'no_sort':
                    pattern = vacancy_pattern['backend_vacancy']
                else:
                    pattern = vacancy_pattern[f'{pro}_vacancy']
                match = re.findall(rf"{pattern}", text)
                if match:
                    vacancy = match[0]
                    break

            if not vacancy:
                pattern = vacancy_pattern['backend_vacancy']
                match = re.findall(rf"{pattern}", text)
                if match:
                    vacancy = match[0]
        if vacancy:
            vacancy = re.sub(r"[Дд]олжность[:\s]{1,2}", '', vacancy)
            vacancy = re.sub(r"[Вв]акансия[:\s]{1,2}", '', vacancy)
            vacancy = vacancy.strip()

            vacancy = self.clean_vacancy_from_get_vacancy_name(vacancy)
        return vacancy

    def clean_vacancy_from_get_vacancy_name(self, vacancy):
        trash_list = ["[Ии]щем в команду[:]?", "[Тт]ребуется[:]?", "[Ии]щем[:]?", "[Вв]акансия[:]?", "[Пп]озиция[:]?",
                      "[Дд]олжность[:]?", "в поиске[:]?", "[Нн]азвание вакансии[:]?", "[VACANCYvacancy]{7}[:]?"]
        for i in trash_list:
            vacancy = re.sub(rf"{i}", "", vacancy)
            # if i in vacancy:
            #     vacancy = vacancy.replace(i, '')
        return vacancy.strip()
#  -------------- it reads from file for testing ------------------
# with open('./../file.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#
# text = text.split(f'\n', 1)
# title = text[0]
# body = text[1]
#
# print(title)
# print(body)
#
# profession = AlexSort2809().sort_by_profession_by_Alex(title, body)
# print('total profession = ', profession)