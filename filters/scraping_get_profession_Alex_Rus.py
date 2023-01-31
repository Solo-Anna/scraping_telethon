"""
28/09/2022 I think that a better version of algorithm
"""

import re
from patterns import pattern_Ruslan
from __backup__ import pattern_Alex


class AlexRusSort:

    def __init__(self):

        self.result_dict2 = {'vacancy': 0, 'contacts': 0, 'fullstack': 0, 'frontend': 0, 'backend': 0, 'pm': 0, 'mobile': 0, 'game': 0, 'designer': 0,
                      'hr': 0, 'analyst': 0, 'qa': 0, 'ba': 0, 'product': 0, 'devops': 0, 'marketing': 0, 'sales_manager': 0, 'junior': 0, 'middle': 0, 'senior': 0}
        # self.result_dict = {
        #     'title': {'vacancy': 0, 'contacts': 0, 'fullstack': 0, 'frontend': 0, 'backend': 0, 'pm': 0, 'mobile': 0, 'game': 0, 'designer': 0,
        #               'hr': 0, 'analyst': 0, 'qa': 0, 'ba': 0, 'product': 0, 'devops': 0, 'marketing': 0, 'sales_manager': 0},
        #     'body': {'vacancy': 0, 'contacts': 0, 'fullstack': 0, 'frontend': 0, 'backend': 0, 'pm': 0, 'mobile': 0, 'game': 0, 'designer': 0,
        #               'hr': 0, 'analyst': 0, 'qa': 0, 'ba': 0, 'product': 0, 'devops': 0, 'marketing': 0, 'sales_manager': 0}
        # }
        self.keys_result_dict = ['fullstack', 'frontend', 'qa', 'ba', 'backend', 'pm', 'mobile', 'game', 'designer', 'hr', 'analyst', 'product', 'devops', 'marketing', 'sales_manager']
        self.pattern_ruslan = pattern_Ruslan.pattern
        self.pattern_alex = pattern_Alex.pattern

    def sort_by_profession_by_AlexRus(self, title, body):

        profession = []
        profession_dict = {}

        self.tag_alex = ''
        self.tag_alex_anti = ''

#------------ add old pattern to pattern Alex -----------------
        for i in self.keys_result_dict:
            self.pattern_alex[i]['ma'] = set(self.pattern_alex[i]['ma']) | set(self.pattern_ruslan[i])
        for i in self.pattern_alex:
            print(i, self.pattern_alex[i]['ma'])


# ----------------- Check for used capitalize or don't ------------------
        for i in self.pattern_alex:

            capitalize = False

            message = f'{title}\n{body}'

            self.get_profession(message, capitalize, key=i)

            if i == 'contacts' and self.result_dict2['contacts'] == 0:
                print('*****************NO CONTACTS!!!!!!!!!')
                profession = ['no_sort']
                break
            if i == 'vacancy' and self.result_dict2['vacancy'] == 0:
                print('*****************NO VACANCY!!!!!!!!!')
                profession = ['no_sort']
                break


# -------------------- записать все профессии, которые встретились --------
#         for i in self.result_dict:
#             temporary = self.result_dict['title'][i] + self.result_dict['body'][i]
#             self.result_dict[i] = temporary

        for i in self.result_dict2:
            if self.result_dict2[i]:
                profession.append(i)
        pass

#------------------- вывести в консоль result_dict ----------------------

        for i in self.result_dict2:
            print(f'{i}: {self.result_dict2[i]}')

# ---------------- delete not used keys and values as contact and vacancy -------------------
        k=0
        while k<len(profession):
            if profession[k] in ['vacancy', 'contacts']:
                profession.pop(k)
            else:
                k += 1

        profession = set(profession)
        prof2 = list(self.separate_profession(profession))
        for i in ['junior', 'middle', 'senior']:
            if i in profession:
                prof2.append(i)


# -------------- collect dict for return it to main code ----------------
        profession_dict['profession'] = set(prof2)
        profession_dict['tag'] = self.tag_alex
        profession_dict['anti_tag'] = self.tag_alex_anti
        profession_dict['block'] = False  # заглушки для кода, который вызывает этот класс
        profession_dict['junior'] = 0
        profession_dict['middle'] = 0
        profession_dict['senior'] = 0

        if not profession_dict['profession']:
            profession_dict['profession'] = 'no_sort'

        return profession_dict

    def separate_profession(self, profession):
        max_dict = {}
        max_prof = ''
        prof2 = []
        new_result_dict = {}

        #get bigger values for title and body
        max_value = 0

# ---------------- search max value and append it to prof2 -------------
        for key in self.keys_result_dict:
            if self.result_dict2[key] > max_value:
                max_dict = {key: self.result_dict2[key]}
                max_value = self.result_dict2[key]
        if not max_value:
            max_prof = 'no_sort'
            return [max_prof]
        else:
            max_prof = list(max_dict)[0]

# ------------------in case if there is fullstack with backend and frontend -----------------

        if max_prof in ['backend', 'frontend'] and self.result_dict2['qa'] and (not self.result_dict2['fullstack'] and not self.result_dict2['devops']):
            if self.result_dict2["backend"]*0.5 > self.result_dict2["qa"]:
                prof2.append('backend')
            else:
                prof2.append('qa')
            return prof2

        if max_prof in ['backend', 'frontend'] and (self.result_dict2['fullstack'] or self.result_dict2['devops']):

            # check case if fullstack and devops
            if (self.result_dict2['fullstack'] and self.result_dict2['devops']) and self.result_dict2['fullstack']>self.result_dict2['devops']:

                if (self.result_dict2['backend'] + self.result_dict2['frontend'] > 10 and self.result_dict2['fullstack'] > 2) \
                        or (self.result_dict2['backend'] + self.result_dict2['frontend'] > 5 and self.result_dict2['fullstack'] > 1):
                    prof2.append('fullstack')
                    prof2.append('backend')
                    prof2.append('frontend')
                elif self.result_dict2['backend']*0.7 > self.result_dict2['frontend']:
                    prof2.append('backend')
                else:
                    prof2.append('frontend')

            elif (self.result_dict2['fullstack'] and self.result_dict2['devops']) and self.result_dict2['fullstack']<self.result_dict2['devops']:
                if (self.result_dict2['backend'] + self.result_dict2['frontend'] > 10 and self.result_dict2['devops'] > 2) \
                        or (self.result_dict2['backend'] + self.result_dict2['frontend'] > 5 and self.result_dict2['devops'] > 1):
                    prof2.append('devops')
                elif self.result_dict2['backend']*0.7 > self.result_dict2['frontend']:
                    prof2.append('backend')
                else:
                    prof2.append('frontend')

            elif (self.result_dict2['fullstack'] and not self.result_dict2['devops']):
                if (self.result_dict2['backend'] + self.result_dict2['frontend'] > 10 and self.result_dict2['fullstack'] > 2) \
                        or (self.result_dict2['backend'] + self.result_dict2['frontend'] > 1 and self.result_dict2['fullstack'] > 1):
                    prof2.append('fullstack')
                    prof2.append('backend')
                    prof2.append('frontend')
                elif self.result_dict2['backend']*0.7 > self.result_dict2['frontend']:
                    prof2.append('backend')
                else:
                    prof2.append('frontend')

            elif (not self.result_dict2['fullstack'] and self.result_dict2['devops']):
                if (self.result_dict2['backend'] + self.result_dict2['frontend'] > 10 and self.result_dict2['devops'] > 2) \
                        or (self.result_dict2['backend'] + self.result_dict2['frontend'] > 5 and self.result_dict2['devops'] > 1):
                    prof2.append('devops')
                elif self.result_dict2['backend']*0.7 > self.result_dict2['frontend']:
                    prof2.append('backend')
                else:
                    prof2.append('frontend')
        else:
            prof2.append(max_prof)

        # if max_value<4:
        #     quantity_keys = []
        #     for i in self.keys_result_dict:
        #         if self.result_dict2[i]:
        #             quantity_keys.append(i)
        #     if len(quantity_keys)>2:
        #         for i in quantity_keys:
        #             prof2.append(i)

        return set(prof2)

    def get_profession(self, message, capitalize, key):
        message_to_check = ''
        link_telegraph = ''
    # ---------- for vacansy we need to make value 1 because we will search only excludes-----------
        if key == 'vacancy':
            self.result_dict2[key] = 1
# --------------- collect all matches in 'ma' -----------------------
        for word in self.pattern_alex[key]['ma']:

            if not capitalize:
                if word[0:1] != '*':  # * I mark words not changes
                    word = word.lower()
                    message_to_check = message.lower()
                else:
                    word = word[1:]
                    message_to_check = message



                match = re.findall(word, message_to_check)
                if match:
                    self.tag_alex += f'TAG {key}={match}\n'
                    print(f'TAG {key} = {match}')
                    self.result_dict2[key] += len(match)

# -------------- cancel all matches if it excludes words ------------------
        for exclude_word in self.pattern_alex[key]['mex']:
            match = re.findall(exclude_word, message_to_check)
            if match:
                self.tag_alex_anti += f'TAG ANTI {key}={match}\n'
                print(f'TAG ANTI {key} = {match}')
                self.result_dict2[key] = 0

            pass

    def get_content_from_telegraph(self, link_telegraph):
        print('link_telegraph = ', link_telegraph)
        """
        parsing
        """
        pass

#  -------------- it reads from file for testing ------------------
# with open('file.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#
# text = text.split(f'\n', 1)
# title = text[0]
# body = text[1]
#
# print(title)
# print(body)
#
# profession = AlexSort2().sort_by_profession_by_Alex(title, body)
# print('total profession = ', profession)