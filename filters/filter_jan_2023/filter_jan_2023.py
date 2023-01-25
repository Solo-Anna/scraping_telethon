import re
import time

from patterns import pattern_Alex2809
from db_operations.scraping_db import DataBaseOperations
# from patterns.pattern_Alex2809 import search_companies, search_companies2, english_pattern, remote_pattern, \
#     relocate_pattern, middle_pattern, senior_pattern, vacancy_name, vacancy_pattern, contacts_pattern, profession_new_pattern
from patterns._export_pattern import export_pattern as q
from utils.additional_variables import additional_variables as variables

class VacancyFilter:

    def __init__(self):
        self.pattern_alex = pattern_Alex2809.pattern
        self.capitalize = variables.not_lower_professions

        self.result_dict2 = {'vacancy': 0, 'contacts': 0, 'fullstack': 0, 'frontend': 0, 'backend': 0, 'pm': 0,
                             'mobile': 0, 'game': 0, 'designer': 0, 'hr': 0, 'analyst': 0, 'qa': 0, 'ba': 0,
                             'product': 0, 'devops': 0, 'marketing': 0, 'sales_manager': 0, 'junior': 0, 'middle': 0,
                             'senior': 0}

        self.valid_profession_list = variables.valid_professions
        self.export_pattern = q
        self.not_lower_professions = variables.not_lower_professions
        self.excel_dict = {}

    def sort_profession(self, title, body, check_contacts=True, check_profession=True, check_vacancy=True, get_params=True):
        profession = dict()
        profession['tag'] = ''
        profession['anti_tag'] = ''
        profession['profession'] = []
        profession['sub'] = []
        params = {}
        vacancy = f"{title}\n{body}"
        patt = q

        if check_profession:
            # if it is not vacancy, return no_sort
            if check_vacancy:
                result = self.check_parameter(
                    pattern=self.export_pattern['data']['vacancy'],
                    vacancy=vacancy,
                    key='vacancy'
                )
                self.result_dict2['vacancy'] = result['result']
                profession['tag'] += result['tags']
                profession['anti_tag'] += result['anti_tags']

                if not self.result_dict2['vacancy']:
                    profession['profession'] = {'no_sort'}
                    print(f"line84 {profession['profession']}")
                    print("= vacancy not found =")
                    return {'profession': profession, 'params': {}}

            if check_contacts:
                # if it is without contact, return no_sort
                result = self.check_parameter(
                    pattern=self.export_pattern['data']['contacts'],
                    vacancy=vacancy,
                    key='contacts'
                )
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
                if item in self.not_lower_professions:
                    low = False
                else:
                    low = True

                if item == 'product':
                    item = 'pm'

                result = self.check_parameter(
                    pattern=self.export_pattern['professions'][item],
                    vacancy=vacancy,
                    low=low,
                    key=item
                )
                if result['result']:
                    profession['profession'].append(result['result'])
                    # print(f"in loop: {profession['profession']}")
                profession['tag'] += result['tags']
                profession['anti_tag'] += result['anti_tags']

            if 'fullstack' in profession['profession']:
                profession = self.transform_fullstack_to_back_and_front(text=vacancy, profession=profession)

            if not profession['profession']:
                profession['profession'] = {'no_sort'}
                # print(f"line100 {profession['profession']}")

            profession['profession'] = set(profession['profession'])

            # -------------- get subprofessions -------------------------
            if 'no_sort' not in profession['profession']:
                print(f"FINALLY: {profession['profession']}")
                self.get_sub_profession(profession, text=vacancy)
            else:
                profession['sub'] = []

            if profession['sub']:
                profession = self.compose_junior_sub(
                    profession=profession,
                    key_word='junior'
                )
        # --------------------- end -------------------------
        if get_params:
            params = self.get_params(text=vacancy, profession=profession)

        print(f"\nFound next professions:\n{profession['profession']}\n")

        return {'profession': profession, 'params': params}

    def get_sub_profession(self, profession, text):
        profession['sub'] = {}

        # print(text)
        # print(profession['profession'])
        for prof in profession['profession']:
            prof = prof.strip()

            union_sub = {}
            if prof in self.valid_profession_list:
                profession['sub'][prof] = []
                current_profession_sub_list = self.export_pattern['professions'][prof]['sub']
                for sub in current_profession_sub_list:
                    pattern = self.export_pattern['professions'][prof]['sub'][sub]

                    result = self.check_parameter(
                        pattern=pattern,
                        vacancy=text,
                        key=sub,
                        low=False
                    )
                    if result['result']:
                        profession['sub'][prof].append(result['result'])

        for i in profession['sub']:
            print(i, profession['sub'][i])
        pass
        return profession

    def check_parameter(self, pattern, vacancy, key, low=True):
        result = 0
        tags = ''
        anti_tags = ''

        # if low:
        #     vacancy = vacancy.lower()
        for word in pattern['ma']:
            if len(word) == 1:
                pass
            # if low:
            #     word = word.lower()
            match = []
            try:
                match = set(re.findall(rf"{word}", vacancy))
            except Exception as e:
                with open('./excel/filter_jan_errors.txt', 'a+', encoding='utf-8') as f:
                    f.write(f"word = {word}\nvacancy = {vacancy}\nerror = {e}\n------------\n\n")

            if match:
                result += len(match)
                tags += f'MA {key}={match}\n'

        if result:
            for anti_word in pattern['mex']:
                # if low:
                #     anti_word = anti_word.lower()
                if len(anti_word) == 1:
                    pass

                match = []
                try:
                    match = set(re.findall(rf"{anti_word}", vacancy))
                except Exception as e:
                    with open('./excel/filter_jan_errors.txt', 'a+', encoding='utf-8') as f:
                        f.write(f"word = {anti_word}\nvacancy = {vacancy}\nerror = {e}\n------------\n\n")

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
        params['relocation'] = self.get_relocation_new(text)
        params['english'] = self.english_requirements_new(text)
        params['vacancy'] = self.get_vacancy_name(text, profession['profession'])
        return params

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

    def get_company_new(self, text):
        companies_from_db = DataBaseOperations(None).get_all_from_db(
            table_name='companies',
            without_sort=True,
            field='company'
        )
        for company in companies_from_db:
            company = company[0]
            if company and company in text:
                # print(company)
                return company

        match = re.findall(rf"{self.export_pattern['others']['company']['ma']}", text)
        if match:
            return self.clean_company_new(match[0])

        match = re.findall(rf"{self.export_pattern['others']['company2']['ma']}", text)
        if match:
            return match[0]
        return ''

    def english_requirements_new(self, text):
        english_pattern = "|".join(self.export_pattern['others']['english']['ma'])
        match = re.findall(english_pattern, text)
        if match:
            match = match[0].replace('\n', '').replace('"', '').replace('#', '').replace('.', '')
            match = match.strip()
            if match[-1:] == '(':
                match = match[:-1]
        else:
            match = ''
        return match

    def get_relocation_new(self, text):
        relocate_pattern = "|".join(self.export_pattern['others']['relocate']['ma'])
        match = re.findall(rf"{relocate_pattern}", text)
        if match:
            return match[0]
        else:
            return ''

    def get_remote_new(self, text):
        remote_pattern = "|".join(self.export_pattern['others']['remote']['ma'])
        match = re.findall(rf"{remote_pattern}", text)
        if match:
            return match[0]
            # return 'remote'
        else:
            return ''

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

    def get_vacancy_name(self, text, profession_list, sub=None):
        vacancy = ''
        match = []

        if not vacancy:
            for pro in variables.valid_professions:
                if pro == 'no_sort':
                    pass
                    # pattern = self.export_pattern['others']['vacancy']['sub']['backend_vacancy']
                # else:
                pattern = self.export_pattern['others']['vacancy']['sub'][f'{pro}_vacancy']
                if pattern:
                    match = re.findall(rf"{pattern}", text)
                    print('pro = ', pro)
                    print('match = ', match)
                    print("type(match) = ", type(match))
                    try:
                        match_str = ''.join(match)
                        print("''.join(match) = ", match_str)
                        if len(''.join(match)) > 0:
                            vacancy = match[0]
                            break
                    except Exception as e:
                        print('Error: ', e)

        if not vacancy:
            vacancy_pattern = self.export_pattern['others']['vacancy']['sub']['common_vacancy']
            if vacancy_pattern:
                match = re.findall(rf"{vacancy_pattern}", text)
                print('pro = common')
                print('match = ', match)
                print("type(match) = ", type(match))
                try:
                    match_str = ''.join(match)
                    print("''.join(match) = ", match_str)
                    if len(''.join(match)) > 0:
                        vacancy = match[0]
                except Exception as e:
                    print('Error: ', e)

            # if not vacancy:
            #     pattern = self.export_pattern['others']['vacancy']['sub']['backend_vacancy']
            #     match = re.findall(rf"{pattern}", text)
            #     print('match = ', match)
            #     print("''.join(match) = ", ''.join(match))
            #     if len(''.join(match))>0:
            #         vacancy = match[0]

        if sub and not vacancy:
            for key in sub:
                if sub[key]:
                    vacancy = f"{sub[key].capitaloze()} {key}"
                    break
        if vacancy:
            vacancy = self.clean_vacancy_from_get_vacancy_name(vacancy)

            print('++++++++++++++++++++\nvacancy = ', vacancy, '\n++++++++++++++++++++')
            # time.sleep(10)
        return vacancy

    def clean_vacancy_from_get_vacancy_name(self, vacancy):
        vacancy = re.findall(r"[a-zA-Zа-яА-Я0-9:;-_\\/\s]+", vacancy)[0]
        # trash_list = ["[Ии]щем в команду[:]?", "[Тт]ребуется[:]?", "[Ии]щем[:]?", "[Вв]акансия[:]?", "[Пп]озиция[:]?",
        #               "[Дд]олжность[:]?", "в поиске[:]?", "[Нн]азвание вакансии[:]?", "[VACANCYvacancy]{7}[:]?"]
        # for i in trash_list:
        #     if i in vacancy:
        vacancy = re.sub(rf"{variables.clear_vacancy_trash_pattern}", "", vacancy)
        print("vacancy_final = ", vacancy.strip())
        return vacancy.strip()

    def compose_junior_sub(self, profession, key_word):
        print("profession['sub'] ", profession['sub'])
        if key_word in profession['sub'].keys():
            for key in profession['sub'].keys():
                if key != key_word:
                    profession['sub'][key_word].append(key)
        return profession

