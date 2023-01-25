pattern = {
'vacancy': {
            'ma': {'вакансия', "job", "work ", "работа", "Компания"},
            'mex': {'#резюме', '#cv ', 'ищу работу', 'ищуработу', 'opentowork', 'фильм на вечер', 'рекомендую', 'хотим рассказать о новых каналах',
                    'skillbox', 'зарабатывать на крипте', 'секретар', 'делопроизводител',
                    'онлайн курс', 'образовательная платформа', 'со скидкой',
                   'бесплатном марафоне', 'это помогает нам стать лучше для вас', 'получайте больше откликов', '3dartist', '3d artist',
                   'бесплатном интенсиве', 'бесплатный интенсив', 'админвещает', 'в онлайн-интенсиве', 'обо мне', 'ish joyi kerak',
                   'geekjob.ru', 'мы не ищем сотрудников', 'поиске работы', 'sales manager', 'salesmanager',
                   'sales_manager', '‼️Как работает этот канал:', 'outstaff', 'На занятии рассмотрим'}
            # 'mex': (" готовим IT-специалистов", "ответы с собеседований", "Подготовим к любой понравившейся вакансии",
            #         "Подготовим к вакансии", "онлайн-курс", "Geekhub", "Ищу работу", "Дайджест", "Xodim", "#резюме",
            #         "аутстафф", "outstaff", "opentowork", "ищуработу", "преподаватель", "Resume", "#CV",
            #         "lookingforajob") #"apply"
            # Call analyze(st, a, b, ma, mex, col)
            },

            'contacts': {
                'ma': {"@", "www", "http", "https://telegra.ph/"},
                'mex': ()
                # Call analyze(st, a, b, ma, mex, col) 'поиск без учета регистра'
            },

            # 'fullstack': {
            #     'ma': {
            #     "FullStack", "Full-stack", "Full stack", "Java ", "Java-", "Chief Technical Officer", " CTO", "Golang"},
            #     'mex': ("Golang собеседований", "QA Full", "stack QA", "Kotlin")
            #     # Call analyze(st, a, b, ma, mex, col) 'поиск без учета регистра'
            # },
            'fullstack': {
                'ma': {
                "FullStack", "Full-stack", "Full stack", "Chief Technical Officer", " CTO"},
                'mex': ("Golang собеседований", "QA Full", "stack QA", "Kotlin")
                # Call analyze(st, a, b, ma, mex, col) 'поиск без учета регистра'
            },

            'frontend': {
                'ma': {"Frontend", "Front-end", "front end", " React ", " Vue ", "Angular", "Team Lead Web"},
                'mex': ("understanding of front-end", "взаимодействие с отделом frontend", "QA Automation",
                        "Test Automation Engineer", "C\+\+")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'backend': {
                'ma': {
                "#ML ", "машинному обучению", "MLOps", "ML engineer", "Python Developer", "#Backend", "node.js", "Backend",
                "Back-end", "back end", "Scala", "Java", "C\+\+", "С\+\+", "C#", " PHP", "PHP разработчик", " РНР",
                "Laravel", "Golang", "Drupal"},
                'mex': ("@python_job_interview", "Data Engineer", "Kotlin", "backend разработчиками", "Backend QA Engineer",
                        "Javascript", "java script", "тестирования backend", "тестирование backend", "QA Automation",
                        "QA Auto", "Test Automation Engineer", "опыт работы с Backend", "Manual testing",
                        "backend ecosystem", "автоматизируем только backend")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'pm': {
                'ma': {"* PM", "Project manager", "Project Manager", "project manager", "Project-manager",
                       "Менеджер IT проектов", "Руководитель ИТ-проект"},
                'mex': ()
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'mobile': {
                'ma': {"Kotlin", "Swift", "Mobile", "ios", "android", "Flutter"},
                'mex': ("T-Mobile", "Swift, is a nice to have skill", "QA Automation", "QA Auto", "Test Automation Engineer",
                "Manual testing", "заказного mobile")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'game': {
                'ma': {"*Game ", "game ", "*Unity", "Unreal"},
                'mex': ("Gamedev", "gamedev")
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'designer': {
                'ma': {"2D", "3D", "Motion", "motion", "Designer", "designer", "Дизайнер", "дизайнер", "*UX", "*UI", "UX/UI",
                       "UI/UX", "Product designer"},
                'mex': ("Artec 3D", "3D scanners", "DevOps", "Web UI", "Product manager", "Product owner", "из дизайнера",
                        "из Дизайнера", "designers", "3D Unity", "3D unity", "Unity 3D", "Understanding UI state",
                        "Material UI", "до UI", "Python", "Java", "Kotlin", "Swift", " C ", "C\+\+", "C#", "ObjectiveC",
                        "React", "SoapUI", "Postman")
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'hr': {
                'ma': {"Human Resources Officer", "* HR", "recruter", "кадр", "human r", "head hunter", "Кадр", "HR BP",
                       "HR Бизнес-партнер", "IT Recruiter", "Recruiter"},
                'mex': ("я HR", "представляю кадровое агенство", "Общение с HR", "общение с HR", "HR_", "HRTech", "HR департамент",
                        "SEO HR", "HR@", "Кадровое агенство", "звонок с HR ", "Пишите нашему HR-менеджеру", "HR-Link", "HR-Prime")
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'analyst': {
                'ma': {"Dats scientist", "BI Engineer", "Data Engineer", "#SA", "SOC Analyst", "Performance аналитик",
                       "Маркетинг аналитик", "Старший аналитик", "Тимлид аналитики", "Data analyst", "Data Scientist",
                       "Data Science", "DataScientist", "data analyst", "data scientist", "datascientist",
                       "аналитик данных", "Machine Learning", "Product Analyst", "Системный аналитик", "системный аналитик",
                       "Системный Аналитик"},
                'mex': ("Business Analyst", "/BA", "BA", "бизнес аналитик", "ВА", "business analyst", "Бизнес аналитик")
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'qa': {
                'ma': {"*QA Lead", "*QAA", "* QA", "по качеству", "тестировщик", "quality assurence", "тестер",
                       "Test Automation Engineer", "QA Automation", "QA Auto", "Manual testing", "AQA ",
                       "mobile applications testing"},
                'mex': ("тестировщиков", "тестировщиками", "проводить QA")
                # Call ANALIZEP(st, a, b, ma, mex, col)
            },

            'ba': {
                'ma': {
                "BI Engineer", "Бизнес-Аналитик", "*#BA", "* BA,", "* BA ", "* BA.", "Business analyst", "Business Analyst",
                "бизнес аналитик", "* ВА ", "business analyst", "Бизнес аналитик", "Бизнес-аналитик"},
                'mex': ()
                # Call ANALIZEP(st, a, b, ma, mex, col) 'поиск с учетом регистра'
            },

            'product': {
                'ma': {"PrdM", "product manager", "product owner", "Head of Core Product", "* CPO", "Head of Product",
                       "Product Lead", "Директор по продукту", "/CPO", " CPO"},
                'mex': ("вместе с product owner", "product designer", "Взаимодействие с Product Manager")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'devops': {
                'ma': {"инженера по информационной безопасности", "DevOps", "*SRE", "Site Reliability Engineer"},
                'mex': ("DevOps командой", "участвовать в DevOps", "Опыт DevOps", "участвуют в DevOps", "DevOps practices",
                        "devops навыки", "DevOps tools")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'marketing': {
                'ma': {"SMM", "Copyrighter", "SEO", "Marketer", "Маркетолог", "Marketing manager", "Менеджер по маркетингу",
                       "Video Tutorial Creator", "Producer", "Lead Generation Specialist", "#leadgeneration"},
                'mex': ("SEO HR", "Product manager")
                # Call analyze(st, a, b, ma, mex, col)
            },

            'sales_manager': {
                'ma': {
                "Sales manager", "sales manager", "Sales Manager", "Менеджера по продажам", "Менеджер холодных продаж",
                "Менеджер по продажам", "менеджер_отдела_продаж"},
                'mex': ()
                # Call analyze(st, a, b, ma, mex, col)
            },

            'junior': {
                'ma': {'trainee', 'junior', 'джуниор'},
                'mex': ()
            },

            'middle': {
                'ma': {'Middle', 'middle'},
                'mex': ()
            },

            'senior': {
                'ma': {'Senior', 'Team lead', 'CTO'},
                'mex': ()
            }
}