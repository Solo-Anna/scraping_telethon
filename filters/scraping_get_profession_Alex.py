import re

class AlexSort:

    def __init__(self):
        self.result_dict = {
            'title': {'vacancy': 0, 'contacts': 0, 'fullstack': 0, 'frontend': 0, 'backend': 0, 'pm': 0, 'mobile': 0, 'game': 0, 'designer': 0,
                      'hr': 0, 'data_analyst': 0, 'qa': 0, 'ba': 0, 'prdm': 0, 'devops': 0, 'marketer': 0, 'sales_manager': 0},
            'body': {'vacancy': 0, 'contacts': 0, 'fullstack': 0, 'frontend': 0, 'backend': 0, 'pm': 0, 'mobile': 0, 'game': 0, 'designer': 0,
                      'hr': 0, 'data_analyst': 0, 'qa': 0, 'ba': 0, 'prdm': 0, 'devops': 0, 'marketer': 0, 'sales_manager': 0}
        }


    def sort_by_profession_by_Alex(self, title, body):

        profession = []
        profession_dict = {}

        self.tag_alex = ''
        self.tag_alex_anti = ''

        self.pattern_dict = {

            'vacancy': {
                'ma': ('вакансия', "job", "work", "работа", "Компания"),
                'mex': (" готовим IT-специалистов", "ответы с собеседований", "Подготовим к любой понравившейся вакансии", "Подготовим к вакансии", "онлайн-курс", "Geekhub", "Ищу работу", "Дайджест", "Xodim", "#резюме", "аутстафф", "outstaff", "opentowork", "ищуработу", "преподаватель", "apply", "Resume", "#CV", "lookingforajob")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'contacts': {
                'ma': ("@", "www", "http"),
                'mex': ()
                # Call analyze(st, a, b, ma, mex, col) 'поиск без учета регистра'
            },

            'fullstack': {
                'ma': ("FullStack", "Full-stack", "Full stack", "Java ", "Java-", "Chief Technical Officer", " CTO", "Golang"),
                'mex': ("Golang собеседований", "QA Full", "stack QA", "Kotlin")
                # Call analyze(st, a, b, ma, mex, col) 'поиск без учета регистра'
            },

            'frontend': {
                'ma': ("Frontend", "Front-end", "front end", " React ", " Vue ", "Angular", "Team Lead Web"),
                'mex': ("understanding of front-end", "взаимодействие с отделом frontend", "QA Automation", "Test Automation Engineer", "C\+\+")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'backend': {
                'ma': ("#ML ", "машинному обучению", "MLOps", "ML engineer", "Python Developer", "#Backend", "node.js", "Backend", "Back-end", "back end", "Scala", "Java", "C\+\+", "С\+\+", "C#", " PHP", "PHP разработчик", " РНР", "Laravel", "Golang"),
                'mex': ("@python_job_interview", "Data Engineer", "Kotlin", "backend разработчиками", "Backend QA Engineer", "Javascript", "java script", "тестирования backend", "тестирование backend", "QA Automation", "QA Auto", "Test Automation Engineer", "опыт работы с Backend", "Manual testing", "backend ecosystem", "автоматизируем только backend")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'pm': {
                'ma': (" PM", "Project manager", "Project Manager", "project manager", " РМ", "Project-manager", "Менеджер IT проектов", "Руководитель ИТ-проект"),
                'mex': ()
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'mobile': {
                'ma': ("Kotlin", "Swift", "Mobile", "ios", "android"),
                'mex': ("T-Mobile", "Swift, is a nice to have skill", "QA Automation", "QA Auto", "Test Automation Engineer", "Manual testing", "заказного mobile")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'game': {
                'ma': ("Game ", "game ", "Unity", "Unreal"),
                'mex': ("Gamedev", "gamedev")
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'designer': {
                'ma': ("2D", "3D", "Motion", "motion", "Designer", "designer", "Дизайнер", "дизайнер", "UX", "UI", "UX/UI", "UI/UX", "Product designer"),
                'mex': ("Artec 3D", "3D scanners", "DevOps", "Web UI", "Product manager", "Product owner", "из дизайнера", "из Дизайнера", "designers", "3D Unity", "3D unity", "Unity 3D", "Understanding UI state", "Material UI", "до UI", "Python", "Java", "Kotlin", "Swift", " C ", "C\+\+", "C#", "ObjectiveC", "React", "SoapUI", "Postman")
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'hr': {
                'ma': ("Human Resources Officer", " HR", "recruter", "кадр", "human r", "head hunter", "Кадр", "HR BP", "HR Бизнес-партнер", "IT Recruiter", "Recruiter"),
                'mex': ("я HR", "представляю кадровое агенство", "Общение с HR", "общение с HR", "HR_", "HRTech", "HR департамент", "SEO HR", "HR@", "Кадровое агенство", "звонок с HR ", "Пишите нашему HR-менеджеру", "HR-Link", "HR-Prime")
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'analyst': {
                'ma': ("Dats scientist", "BI Engineer", "Data Engineer", "#SA", "SOC Analyst", "Performance аналитик", "Маркетинг аналитик", "Старший аналитик", "Тимлид аналитики", "Data analyst", "Data Scientist", "Data Science", "DataScientist", "data analyst", "data scientist", "datascientist", "аналитик данных", "Machine Learning", "Product Analyst", "Системный аналитик", "системный аналитик", "Системный Аналитик"),
                'mex': ("Business Analyst", "/BA", "BA", "бизнес аналитик", "ВА", "business analyst", "Бизнес аналитик")
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'qa': {
                'ma': ("QA Lead", "QAA", " QA", "по качеству", "тестировщик", "quality assurence", "тестер", "Test Automation Engineer", "QA Automation", "QA Auto", "Manual testing", "mobile applications testing"),
                'mex': ("тестировщиков", "тестировщиками", "проводить QA")
                # Call ANALIZEP(st, a, b, ma, mex, col)
            },

            'ba': {
                'ma': ("BI Engineer", "Бизнес-Аналитик", "#BA", " BA,", " BA ", " BA.", "Business analyst", "Business Analyst", "бизнес аналитик", " ВА ", "business analyst", "Бизнес аналитик", "Бизнес-аналитик"),
                'mex': ()
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'product': {
                'ma': ("PrdM", "product manager", "product owner", "Head of Core Product", " CPO", "Head of Product", "Product Lead", "Директор по продукту", "/CPO", " CPO"),
                'mex': ("вместе с product owner", "product designer", "Взаимодействие с Product Manager")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'devops': {
                'ma': ("инженера по информационной безопасности", "DevOps", "SRE", "Site Reliability Engineer"),
                'mex': ("DevOps командой", "участвовать в DevOps", "Опыт DevOps", "участвуют в DevOps", "DevOps practices", "devops навыки", "DevOps tools")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'marketing': {
                'ma': ("SMM", "Copyrighter", "SEO", "Marketer", "Маркетолог", "Marketing manager", "Менеджер по маркетингу", "Video Tutorial Creator", "Producer", "Lead Generation Specialist", "#leadgeneration"),
                'mex': ("SEO HR", "Product manager")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'sales_manager': {
                'ma': ("Sales manager", "sales manager", "Sales Manager", "Менеджера по продажам", "Менеджер холодных продаж", "Менеджер по продажам", "менеджер_отдела_продаж"),
                'mex': ()
                # Call analyze(st, a, b, ma, mex, col)
            },

            'junior': {
                'ma': ('trainee', 'junior', 'джуниор'),
                'mex': ()
            },

            'middle': {
                'ma': ('Middle', 'middle'),
                'mex': ()
            },

            'senior': {
                'ma': ('Senior', 'Team lead', 'CTO'),
                'mex': ()
            }
        }

        for i in self.pattern_dict:
            if self.pattern_dict[i] in ['pm', 'game', 'designer', 'hr', 'data_analyst', 'qa', 'ba']:
                capitalize = True
            else:
                capitalize = False

            self.get_profession(title, body, capitalize, i)
            if i == 'contacts':
                if (self.result_dict['title']['contacts'] + self.result_dict['body']['contacts'] == 0) or (self.result_dict['title']['vacancy'] + self.result_dict['body']['vacancy'] == 0):
                    print('*****************NO CONTACTS OR IT IS NOT VACANCY!!!!!!!!!')
                    profession = ['no_sort']
                    break

# -------------------- записать все профессии, которые встретились --------
        for i in self.result_dict:
            for j in self.result_dict[i]:
                if self.result_dict[i][j]:
                    profession.append(j)

#------------------- вывести в консоль result_dict ----------------------
        # for key in self.result_dict:
        #     for j in self.result_dict[key]:
        #         print(f'{key}: {j} = {self.result_dict[key][j]}')

        k=0
        while k<len(profession):
            if profession[k] in ['vacancy', 'contacts']:
                profession.pop(k)
            else:
                k += 1

        profession_dict['profession'] = set(profession)
        profession_dict['tag'] = self.tag_alex
        profession_dict['anti_tag'] = self.tag_alex_anti

        profession_dict['block'] = False  # заглушки для кода, который вызывает этот класс
        profession_dict['junior'] = 0
        profession_dict['middle'] = 0
        profession_dict['senior'] = 0

        if not profession_dict['profession']:
            profession_dict['profession'] = 'no_sort'

        return profession_dict


    def get_profession(self, title, body, capitalize, i):

        for key in ['title', 'body']:
            for word in self.pattern_dict[i]['ma']:

                if not capitalize:
                    word = word.lower()
                    title = title.lower()
                    body = body.lower()

                if key == 'title':
                    match = re.findall(word, title)
                else:
                    match = re.findall(word, body)
                # print('word = ', word)
                if match:
                    self.tag_alex += f'TAG {i}={match}\n'
                    print(f'TAG {i} = {match}')
                    self.result_dict[key][i] = len(match)

            for exclude_word in self.pattern_dict[i]['mex']:

                if not capitalize:
                    exclude_word = exclude_word.lower()
                    title = title.lower()
                    body = body.lower()

                if key == 'title':
                    match = re.findall(exclude_word, title)
                else:
                    match = re.findall(exclude_word, title)
                # print('exclude_word = ', exclude_word)
                if match:
                    self.tag_alex_anti += f'TAG ANTI {i}={match}\n'
                    print(f'TAG ANTI {i} = {match}')
                    self.result_dict[key][i] = 0

#  -------------- it reads from file for testing ------------------
# with open('text.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#
# text = text.split(f'\n', 1)
# title = text[0]
# body = text[1]
#
# print(title)
# print(body)
#
# profession = AlexSort().sort_by_profession_by_Alex(title, body)
# print('total profession = ', profession)


