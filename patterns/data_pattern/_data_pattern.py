"""
This pattern was made at night at 28/09/2022 with ALexander (online).
"""
from utils.additional_variables.additional_variables import result_excel_dict as cities_dict

pattern = {

    'vacancy': {
        'ma': ("вакансия", "job", "work", "работа", "Компания", 'vacancy', 'https://telegra.ph/', "itjob",
               "Ищем разработчика", "ищу junior", "ищу middle", "ищу senior", "Откликнуться", "ищем"),
        'ma2': (),
        'mdef': (),

        'mex': ("ФИО", "my name", " готовим IT-специалистов", "ответы с собеседований",
                "Подготовим к любой понравившейся вакансии", "Подготовим к вакансии",
                "онлайн-курс", "Geekhub", "Ищу работу", "Дайджест", "Xodim", "#резюме", "аутстафф",
                "outstaff", "opentowork", "ищуработу", "преподаватель", "#apply", "#Resume", "#CV", "CV",
                "lookingforajob", "вебинар", "правила чата", "онлайн-школе", "количество мест ограничено",
                "@foranalysts", "free training courses", "Ищу Работу", "Как это сделать", "@jobforjunior",
                "Шукаю работу", "xodim", "Шукаю віддалену роботу", "Каналы для", "Канал для", "ВАКАНСИЯ ЗАКРЫТА",
                "в поиске новых карьерных возможностей", "Очікування зп", "Шукаю роботу", "Открыт к новым предложениям",
                "в поиске новых карьерных", "в поиске работы", "Шукаю віддалену роботу", "Шукаю роботу","Шукаю працу","у пошуках працы",
                "Шукаю свою першу роботу", "Я соискатель", "Моё резюме", "Мое резюме", "My CV", "I am looking for a job", 
                "Шукаю свою першу роботу","#resume", " Ділимося з вами дружніми Telegram каналами", "делимся резюме", 
                "проводим эфир","я оказываю","медицинская сестра", "медицинский брат", "дефектолог","патриотическ",
                "юрист","менеджер по бизнес-процессам","Logistics Partner Manager","Оператор колл-центра","[Пп]рораб[\s,:;]",
                "Telecom Onboarding","Support Operations Manager", "FarPost", "Бизнес-ассистент", "Операционный менеджер",
                "Координатор Тайных Покупателей","Руководитель онлайн казино","Менеджер по работе с поставщиками",
                "Руководитель направления проектных продаж","Оператор ПК","видеомониторинг", " Заказ канцелярии",
                "Контроль за работой курьеров","Поиск подрядчиков","инженер-конструктор","Менеджер по работе с маркетплейсами",
                "Finance Specialist","Видеограф","чат менеджер","друг по телефону","редактор", "YouTube-канала","#Юмор",
                "developer is available","специалист службы поддержки","Специалист по допечатной подготовке","PCB design engineer",
                "печатных плат","Creative screenwriter","Дизайнер фотокниг","[Жж]урналист","оптовым продажам","Онлайн-менчендайзер",
                "[Кк]онсультант","[Чч]ерт[ёе]жник","Инженер-конструктор","администрирования выплат"," accountant"," #financier",
                "проектировщик сетей связи","юрист", "Сметчик", "[Рр]едактор сайта", "[Зз]амерщик", "встроенные кухни",
                "[Пп]родавец-консультант", "менеджер-дизайнер", "[Фф]лорист", "[Аа]ссистент [Не]аучного отдела",
                "[Мм]астер [Нн]огтевого сервиса", "[Кк]онструктор", "[Бб]армен", "[Оо]фициант", "КАМ", "KAM",
                "[Kk]ey [Aa]ccount [Mm]anager", "[Фф]инансовый [Аа]налитик", "[Вв]оспитатель", "[Пп]едагог",
                "[Мм]едицинский [Пп]редставитель", "[Пп]овар", "[Ии]нженер-проектировщик", "[Дд]изайнер-архитектор",
                "Вакансия в архиве", "[Чч]ерт[ёе]ж", "[Мм]енеджер-дизайнер", "[Аа]рхитектор-проектировщик",
                "[Оо]формитель", "выставочных", "стендов", "кухонная мебель", "[Тт]ехнолог[\s,:;]",
                "[Мм]енеджер по работе с дизайнерами", "Design Studio 3D","' Chef '", "продюсер", "консультант",
                "Дизайнер-фотограф", "специалист по работе с фотографиями", "медицинский представитель",
                "[Дд]изайнер-строитель", "[Лл]огопед", "дефектолог", "ресниц", "маникюр", "педикюр", "архитектура зданий",
                "[Дд]изайнер-архитектор", "кухни на заказ", "[Ll]ogistics manager", "[Оо]фис-менеджер",
                "[Мм]енеджер по логистике", "[Вв]одитель-международ", "[Ээ]кспедитор", "[Сс]таж[её]р финансового отдела",
                "[Пп]омощник [Пп]рораба", "[Сс]таж[её]р юриста", "[Сс]таж[её]р в отдел бухгалтерии", "[Сс]таж[её]р на производство",
                "[Уу]ченик [Рр]и[еэ]лтор", "[Бб]ухгалтер [Сс]таж[её]р", "[Рр]и[еэ]лтор-[Сс]таж[её]р", "[Сс]таж[её]р по недвижимости",
                "[Рр]есепшн", "[Рр]и[еэ]лтор \([Сс]таж[её]р\)", "[Пп]родаже [Нн]едвижимости", "[Оо]твозить заказы",
                "[Оо]бслуживани[ея] кофемашины", "[бБ]ройлер", "по ремонту", "по охране труда", "[Оо]хранник", "[Пп]родавец-[Кк]онсультант",
                "по недвижимости", "по продаже недвижимости", "[Дд]елопроизводитель", "[Бб]ухгалтер-[Сс]таж[её]р",
                "по товарному уч[её]т", "[Мм]аникюр", "[Гг]альваник", "[Дд]изайнер[а]? одежды", "Дизайнер женского нижнего белья",
                "[Ии]нженер-схемотехник", "[Сс]увенирной", "[Сс]увенирных", "[Нн]аградной", "[Оо]бработка фотографий",
                "[Д]изайнер - печатник", "[Фф]лорист-декоратор", "[Фф]лорист-декоратор", "[Ии]нженер-конструктор",
                "[Ee]nglish [Tt]eacher", "[Рр]евизор", "физическому труду", "[Уу]паковщи", "[Мм]аркировщ", "[Оо]ператор [Дд]оставки",
                "[Рр]етуш[её]р", "[Ээ]лектронщик", "[Ии]нженер-схемотехник", "[Дд]изайнер-фотограф", "[Оо]формитель торгового"),
        'mex2': (),
        'mincl': (),
    },

    'contacts': {
        'ma': ("@", "www.", "http:"),
        'ma2': (),
        'mdef': (),

        'mex': (),
        'mex2': (),
        'mincl': (),
    },

    'fullstack': {
        'ma': ("фулл-стек", "Rust", "FullStack", "Full-stack", "Full stack", "Java ", "Java-",
               "Chief Technical Officer", " CTO", "Golang","fullstack Web Developer","Full Stack",),
        'ma2': (),
        'mdef': (),

        'mex': (" UI/UX designer", "контакт до CTO", "Golang собеседований", "QA Full", "stack QA", "Kotlin",
                "Position:Backend Engineer", "Вакансия: Разработчик Android", "Вакансия : Android Developer",
                "Release Engineer", "Middle QA", "Вакансия: QA Engineer"),
        'mex2': (),
        'mincl': (),
    },

    'frontend': {
        'ma': (),
        'ma2': ("[Вв]еб-разработчик", "[Ff]ront[Ee]nd",  "[Ff]ront [Ee]nd",  "Team Lead Web","[Вв]ерстальщик","[Вв]еб-мастер",
               "[Ww]eb-Developer","[Jj]ava[Ss]cript","[Ff]ront-end [Рр]азработчик","[Рр]азработчик [Jj]ava[Ss]cript"
               "[Фф]ронтенд-[Рр]азработчик","[Дд]изайнер сайтов на [Tt]ilda","[Ff]rontend [Ee]ngineer","[Ww]eb-[Dd]eveloper", "[Вв]еб-[Пп]рограммист",
               "менторов по JS"),
        'mdef': ("[Ff]rontend-разработчик", "[Ff]rontend developer", "[Jj]ava[Ss]cript разработчик",
                 "[Ff]rontend разработчик"),
               # pattern['frontend']['ma']=set(pattern['Vue']['ma']).union(set(pattern['frontend']['ma2'])).union(set(pattern['React']['ma'])).union(set(pattern['Angular']['ma'])).union(set(pattern['Django']['ma'])).union(set(pattern['Wordpress']['ma'])).union(set(pattern['Bitrix']['ma'])).union(set(pattern['Joomla']['ma'])).union(set(pattern['Drupal']['ma']))

        'mex': (),
        'mex2': ("Security Developer","React as a plus", "understanding of front-end", "взаимодействие с отделом frontend",
                "Инженер по развитию","AWS","по работе с клиентами","Retention Spesialist",
                 "Elixir", "продюсер", "исследователь", "исследователя", "бизнес-ассистент",
                "мебели","Producer"),
        'mincl': (),
                
        # pattern['frontend']['mex']=set(pattern['Vue']['mex2']).union(set(pattern['frontend']['mex2']))

        'sub': {

            'vue': {

                'ma': ("Vue", "[Vv]ueJS","Vue developer", "VUE JS", " Vue 3"),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()

                # pattern['Vue']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Vue']['mex2']))
            },

            'react': {
                'ma': (" React ", "React+" ),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()

                # pattern['React']['mex']=set(pattern['frontend']['mex']).union(set(pattern['React']['mex2']))
            },

            'angular': {

                'ma': ("Angular", ),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()

                # pattern['Angular']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Angular']['mex2']))
            },

            'django': {

                'ma': ("Django", ),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()
                # pattern['Django']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Django']['mex2']))
            },

            'wordpress': {

                'ma': ("Wordpress", ),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()

                # pattern['Wordpress']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Wordpress']['mex2']))
            },

            'bitrix': {

                'ma': ("Bitrix","Битрикс", ),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()
                # pattern['Bitrix']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Bitrix']['mex2']))
            },

            'joomla': {

                'ma': ("Joomla", ),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()

                # pattern['Joomla']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Joomla']['mex2']))
            },

            'drupal': {

                'ma': ("Drupal", ),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()

                # pattern['Drupal']['mex']=set(pattern['frontend']['mex']).union(set(pattern['Drupal']['mex2']))
            },
        }
    },
                
    'backend': {

        'ma': (),
        'ma2': ("#[Bb]ackend", "[Bb]ackend", "[Bb]ack-end", "[Bb]ack end","Вакансия: [Bb]ackend  [Ee]ngineer","[Bb]ackend разработчик", "Senior Backend Developer","Backend engineer","Position:Backend Engineer","Junior Backend Developer","Senior backend",
               "Backend-разработчик", "#backend","Position:Backend Engineer","backend developer","Blockchain Developer","IT [Aa]rchitect","приглашает в штат бэкенд-разработчиков","разработчик ML",),
        # pattern['backend']['ma']=set(pattern['python']['ma']).union(set(pattern['C']['ma'])).union(set(pattern['PHP']['ma'])).union(set(pattern['Java']['ma'])).union(set(pattern['Ruby']['ma'])).union(set(pattern['Scala']['ma'])).union(set(pattern['.NET']['ma'])).union(set(pattern['NodeJS']['ma'])).union(set(pattern['Laravel']['ma'])).union(set(pattern['Golang']['ma'])).union(set(pattern['Delphi']['ma'])).union(set(pattern['ABAP']['ma'])).union(set(pattern['ML']['ma'])).union(set(pattern['DataEngineer']['ma']))
        'mdef': ('[Bb]ackend-разработчик', '[Pp]ython разработчик', '[Пп]рограммист 1С-Битрикс', '[Cc]hief [Tt]echnical [Oo]fficer',
                 'CTO'),
        'mex': (),
        'mex2': ("DevSecOps", " UI/UX designer", "@python_job_interview", "Data Engineer", "backend разработчиками",
                "Backend QA Engineer", "тестирования backend", "тестирование backend", "QA Automation", "QA Auto",
                "Test Automation Engineer", "опыт работы с Backend", "Manual testing", "backend ecosystem",
                "автоматизируем только backend", "SOC Analyst", "Trading Support Engineer", "Android разработчик",
                "Frontend-разработчик", "Android developer", "Вакансия: Senior QA Engineer", "JavaScript разработчика",
                "Vue-разработчика", "МОБИЛЬНЫХ РАЗРАБОТЧИКОВ", "Frontend разработчика", "ios developer",
                "Head of DevOps", "Position:IT Recruiter", "Flutter Developer", "Cloud Engineer",
                "специалиста Data Science", "Azure DevOps Engineer", "Senior DevOps", "Linux System Administrator",
                "Ищем верстальщика", "Middle qa", "Angular developer", "Vue developer", "Lead devops",
                "Devops engineer", "Middle front-end", "Middle frontend", "Middle+ front-end", "Middle+ frontend",
                "#devops", "product lead", "Ищем Frontend developer", "#resume", "UI Designer", "Designer", "UI designer",
                "Technical writer ","Senior Frontend Developer", "Разработчик JS", "React Frontend developer", "Вакансия: Frontend engineer",
                "разработчик на React Native", "Ведущий тестировщик", "AQA", "Senior Devops","Администратор баз данных","Javascript developer",
                "консультант техподдержки","Вакансия: Frontend ","Вакансия:  Frontend Developer","Senior Frontend Developer",
                "Front-end разработчик"," Frontend Software Engineer","#QA", "Test Automation Engineer", "QA Auto",
                "Junior JavaScript разработчик","Network Engineer", "#kotlin", "Network administration", "Network architect","React Native",
                "Junior Manual QA", "Lead Frontend Developer", "Node.js", "Mobile Development",),
        'mincl': (),

        'sub': {

                'python': {

                    'ma': ("Senior [Pp]ython [Dd]eveloper", "[Pp]ython [Ee]ngineer", "#ML ", "машинному обучению", "MLOps", "ML engineer",
                          "[Pp]ython","[Рр]азработчик [Pp]ython","[Pp]ython [Рр]азработчик","[Pp]ython [Dd]eveloper","[Рр]ython (Mıddle)",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2': (),
                    'mincl': ()
                    # pattern['python']['mex']=set(pattern['backend']['mex']).union(set(pattern['python']['mex2']))
                },

                'c': {

                    'ma': ("C\+\+", "С\+\+", "C#"," C ","ObjectiveC","C\+\+","C\+\+ Qt Developer",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2': (),
                    'mincl': ()
                    # pattern['С']['mex']=set(pattern['backend']['mex']).union(set(pattern['С']['mex2']))
                },

                'php': {

                    'ma': ("PHP"," PHP", "PHP разработчик", "PHP-разработчик","PHP [Dd]eveloper","[Ll]aravel",
                           "PHP backend-разработчик","Team Lead PHP","PHP-программист","[Pp]hp [Dd]eveloper"),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2': (),
                    'mincl': ()

                    # pattern['PHP']['mex']=set(pattern['PHP']['mex']).union(set(pattern['PHP']['mex2']))
                },

                'java': {

                    'ma': ("Java ", "Java,","Java.","#Java ","[Jj]ava [Dd]eveloper","[Jj]ava [Ee]ngineer","[Jj]ava [Рр]азработчик",
                           "JAVA разработчик", "Java Team Lead", "Team Lead(Java)", "[Jj]ava [Ss]oftware [Dd]eveloper",
                           "JAVA backend","[Jj]ava-[Рр]азработчик","JAVA Liferay","[Рр]азработчик [Jj]ava",
                           "Java Tech Lead", "BackEnd Java-разработчик","Spring"),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2': (),
                    'mincl': ()
                    # pattern['Java']['mex']=set(pattern['backend']['mex']).union(set(pattern['Java']['mex2']))
                },

                'ruby': {

                    'ma': ("[Rr]uby", "[Rr]uby on [Rr]ails", "[Rr]uby full-stack [Dd]eveloper","[Rr]uby [Dd]eveloper"),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2': (),
                    'mincl': ()

                    # pattern['Ruby']['mex']=set(pattern['backend']['mex']).union(set(pattern['Ruby']['mex2']))
                },

                'scala': {
                    'ma': ("Scala", ),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2': (),
                    'mincl': ()
                    # pattern['Scala']['mex']=set(pattern['backend']['mex']).union(set(pattern['Scala']['mex2']))
                },

                 'net': {
                     'ma': (" .NET", "Spring.NET"),
                     'ma2': (),
                     'mdef': ("Разработчик .N[Ee][Tt]", "N[Ee][Tt] developer"),
                     'mex': (),
                     'mex2': (),
                     'mincl': ()
                     # pattern[' .NET']['mex']=set(pattern['backend']['mex']).union(set(pattern[' .NET']['mex2']))
                },

                 'nodejs': {
                     'ma': ("NodeJS", "[Nn]ode.js","NodeJS Developer","Разработчик Node.js",),
                     'ma2': (),
                     'mdef': (),
                     'mex': (),
                     'mex2': (),
                     'mincl': ()
                     # pattern['NodeJS']['mex']=set(pattern['backend']['mex']).union(set(pattern['NodeJS']['mex2']))
                },

                 'laravel': {
                     'ma': ("Laravel", ),
                     'ma2': (),
                     'mdef': (),
                     'mex': (),
                     'mex2': (),
                     'mincl': ()
                     # pattern['Laravel']['mex']=set(pattern['backend']['mex']).union(set(pattern['Laravel']['mex2']))
                },

                 'golang': {
                     'ma': ("Golang", " Go ","Go developer",),
                     'ma2': (),
                     'mdef': (),
                     'mex': (),
                     'mex2': (),
                     'mincl': ()
                     # pattern['Golang']['mex']=set(pattern['backend']['mex']).union(set(pattern['Golang']['mex2']))
                },

                 'delphi': {
                     'ma': ("Delphi", ),
                     'ma2': (),
                     'mdef': (),
                     'mex': (),
                     'mex2': (),
                     'mincl': ()
                     # pattern['Delphi']['mex']=set(pattern['backend']['mex']).union(set(pattern['Delphi']['mex2']))
                },

                 'abap': {
                     'ma': ("ABAP","ABAP developer",),
                     'ma2': (),
                     'mdef': (),
                     'mex': (),
                     'mex2': (),
                     'mincl': ()
                     # pattern['ABAP']['mex']=set(pattern['backend']['mex']).union(set(pattern['ABAP']['mex2']))
                },

                 'ml': {
                     'ma': ("#ML ", "машинному обучению", "MLOps", "ML engineer",),
                     'ma2': (),
                     'mdef': (),
                     'mex': (),
                     'mex2': (),
                     'mincl': ()
                     # pattern['ML']['mex']=set(pattern['backend']['mex']).union(set(pattern['ML']['mex2']))
                },

                'data_engineer':{
                    'ma': ("[Dd]ata [Ee]ngineer","ETL","[Ii]nformatica ETL", "Pentaho ETL", "Talend","[Дд]ата-[Ии]нженер",
                          "[Ss]enior [Dd]ata [Ee]ngineer","специалист по обработке данных","[Jj]unior [Dd]ata [Ee]ngineer",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()

                    # pattern['DataEngineer']['mex']=set(pattern['backend']['mex']).union(set(pattern['DataEngineer']['mex2']))
                },

                'unity':{
                    'ma':("Unity developer",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['Unity']['mex']=set(pattern['backend']['mex']).union(set(pattern['Unity']['mex2']))
                },

                'one_c':{
                    'ma':("1С","Программист 1С",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['1C']['mex']=set(pattern['backend']['mex']).union(set(pattern['1C']['mex2']))
                },

                'embedded':{
                    'ma':("Embedded developer",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['Embedded']['mex']=set(pattern['backend']['mex']).union(set(pattern['Embedded']['mex2']))
                }
        }
    },

#     pattern['DEV']['mex']=set(pattern['backend']['ma']).union(set(pattern['python']['ma'])).union(set(pattern['C']['ma'])).union(set(pattern['PHP']['ma'])).union(set(pattern['fullstack']['ma'])).union(set(pattern['frontend']['ma'])).union(set(pattern['Admins']['ma']))
#
    'admins': {
        'ma':(),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2':(),
        'mincl': (),
        'sub': {},
    },

    'mobile': {
       'ma': (),
       'ma2':  ("Mobile","Мобильный разработчик",),
       'mdef':("[Aa]ndroid developer", "[Aa]ndroid-разработчик", "Flutter-разработчик", "Flutter-developer"),
       'mex': (),
       'mex2': ("Python", "T-Mobile", "Senior Product Designer (UX/UI)", "Product Designer","UI/UX Designer",
                 "Release Engineer", "share_ios","Content Designer", "Linux Embedded Developer", "Business Intelligence"),
       'mincl': (),

       'sub': {

     # pattern['mobile']['ma']=set(pattern['mobile']['ma2']).union(set(pattern['mobile']['mdef']))
     #!! pattern['mobile']['mex']=set(pattern['mobile']['mex2']).union(set(pattern['designer']['ma']))

            'ios':{
                'ma':("ios","Swift","Senior ios разработчик","iOS разработчик","IOS Developer","iOS Developer",),
                'ma2': (),
                'mdef': ("[Рр]азработчик под [Ii]O[Ss]", "[Ii]O[Ss][ -]разработчик", "[Ii]O[Ss][ -][Dd]eveloper"),
                'mex': (),
                'mex2':("Swift, is a nice to have skill",),
                'mincl': ()
                # pattern['iOs']['mex']=set(pattern['mobile']['mex']).union(set(pattern['iOs']['mex2']))
            },

            'android':{
                'ma':("Android","Kotlin", "android","Senior Android  developer","[Aa]ndroid-разработчик",
                      "[Aa]ndroid разработчик","middle Android developer","Android Developer","Android Middle разработчик",),
                'mex2':("Swift, is a nice to have skill",),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mincl': ()
                # pattern['Android']['mex']=set(pattern['mobile']['mex']).union(set(pattern['Android']['mex2']))
            },

            'cross_mobile':{
                'ma': (),
                'ma2':(),
                'mdef': (),
                'mex': (),
                'mex2':(),
                'mincl': ()
                # pattern['CrossMobile']['mex']=set(pattern['mobile']['mex']).union(set(pattern['CrossMobile']['mex2']))
                # pattern['CrossMobile']['ma']=set(pattern['CrossMobile']['ma2']).union(set(pattern['Flutter']['ma'])).union(set(pattern['ReactNative']['ma']))
            },

            'flutter':{
                'ma':("Flutter","[Ff]lutter [Dd]eveloper",),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2':(),
                'mincl': ()
            # pattern['Flutter']['mex']=set(pattern['mobile']['mex']).union(set(pattern['Flutter']['mex2']))
            },

            'react_native':{
                'ma':("[Rr]eact [Nn]ative", "[Rr]eact[Nn]ative","разработчика React Native","React Native Developer",
                  "React developer","Senior React Native","React Native разработчик", "приложений React Native",),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2':(),
                'mincl': ()
            # pattern['ReactNative']['mex']=set(pattern['mobile']['mex']).union(set(pattern['ReactNative']['mex2']))
            }
       }
   },
#     #capitalize
    'pm': {
        'ma': (),
        'ma2': (),
        'mdef': ("продукт менеджер", '[Pp]roduct manager', '[Мм]енеджер проектов', "[Пп]омощник менеджера проектов",
                 "[Пп]род[ау]кт-менеджер", "[Dd]elivery [Mm]anager"),
        'mex2': (),
        'mex': ("собеседование с РМ", "Вакансия: Senior PHP Developer", "product lead", "Менеджер В2В", "Manager B2B",
                "Senior Front-End Developer", "Senior Software Testing Engineer", "Sales manager", "Tech Lead",
                "Android Developer", "QA Automation (Python)", "JS developer", "Senior python", "Middle UX/UI Designer",
                "Senior .NET", "C# Engineer", "Senior QA", "QA Automation", "Senior IT Recruiter", "Senior backend",
                "WordPress developer", "Azure DevOps", "Head of Digital", "вместе с product owner", "product designer",
                "Взаимодействие с Product Manager", "UI Designer", "UI designer", "Frontend Developer", "верстальщик",
                "Front-end разработчик", "Веб-мастер", "Web-Developer", "Game Developer", " Web-дизайнер", "Full-Stack",
                "Web-Analyst", "Wordpress developer", "PHP-developer", "Web Developer", "Web-аналитик",
                "Python developer",
                "Web мастер", "PHP-разработчик", "Инженер-программист", "Content Manager", " Web designer",
                "UI/UX Designer",
                "PHP программист", "Веб-разработчик", "инженер", "Инженер", "разработчик", "Разработчик", "developer",
                "Developer",
                "designer", "Designer", "специалист по маркетингу", "Специалист по маркетингу", "программист",
                "Программист",
                "Sales", "sales", "консультант", "Консультант", "Lead Generation", "запуск производства",
                "запуску производства",
                "Верстальщик", "Сисадмин", "Junior веб-разработчик", "разработчик PHP", "Воспитатель", "дефектолог",
                "Руководитель контентной команды", "Руководитель по военно-патриотическому воспитанию",
                "Junior Backend Developer",
                "Junior Frontend Developer", "Дизайнер упаковки", "графический дизайнер", "UX/UI Дизайнер",
                "Fullstack developer",
                "Customer Support Specialist", "Frontend developer", "Дизайнер компьютерной графики",
                "Дизайнер выездной",
                "Frontend Engineer (React)", "Аккаунт-менеджер", "Руководитель отдела маркетинга", "ассистент",
                "Ассистент",
                "помощник руководителя", "Virtual Assistant", "assistant", " Android developer", "IT Architect",
                "iOS-Developer",
                "консультант", "Консультант", "бильдредактор", "квартир", "SMM-менеджер", "Таргетолог", "таргетолог",
                "контенту",
                "Помощник", "marketing manager", "менеджер по продажам", "sales manager", "контекстной рекламе",
                "CRM-аналитик",
                "керамист", "технолог", "Java Developer", "Load Test Engineer", "UI/UX designer",
                "Менеджер по маркетплейсам",
                "Менеджер по работе с маркетплейсами", "Гейм-дизайнер", "Game designer", "Game Producer", "Копирайтер",
                "Sales Researcher", "Team Lead", "Junior front-end", "iOS Developer", "Full-stack",
                "Environment artist",
                "Android разработчик", "Бизнес-ассистент", "Руководитель в отдел трафика", "Android developer",
                "Sales Manager", "Куратор студентов", "Linkbuilder", "маркетолог", "IT рекрутер", "Junior Analyst",
                "Программист С#", "Младший аналитик", "Middle Developer", "E-mail маркетолог",
                "Mobile Marketing Manager",
                "по оптовым продажам", "Producer", "Контент-менеджер", "Администратор сайта", "мебели", "редактор в IT",
                "Android Middle", "Маркетолог", "PR IT", "PHP-программист", "Programmer",
                "Менеджер по работе с маркетплейсами",
                "Аналитик фулстек", "специалист технической поддержки", "Младший разработчик",
                "Менеджер по работе с клиентами",
                "Специалист по внедрению", "spine animator", "Virtual Assistant", "Junior PHP разработчик",
                "Retention Spesialist",
                "Senior Java", "Kotlin developer", "Ведущий инженер", "System Analyst", "Data Analyst",
                "инженер-проектировщик",
                "JavaScript developer", "Бэкенд разработчик", "юрист", "помощник патентного", "SEO-специалист",
                "Ruby developer",
                "Специалист контроля качества", "Педагогический дизайнер", "Разработчик .NET", "Android-разработчик",
                "Программист C#", "Golang developer", "CRM маркетолог", "Email маркетолог", "Директолог",
                "Контекстолог",
                "(React) developer", "Python developer", "Customer Care", "Technical Support", "Системный аналитик",
                "full stack developer", "DevOps engineer", "Backend разработчик", "Трафик-менеджер",
                "контекстная реклама",
                "Outreach Specialist", "Геймдизайнер", "game designer", "Web-дизайнер", "иллюстратор", "SMM-маркетолог",
                "Менеджер по продажам", "менеджер маркетплейсов", "отдела продаж", "Менеджер Wildberries",
                "Главный редактор",
                "Арбитражник", "директора по маркетингу", "Mediabuyer", "Медиабайер", "Продюсер", "Frontend Engineer",
                "Customer Support Specialist", "Artist", "Event-менеджер", "Оператор call-центра",
                "интернет-маркетолог",
                "Senior Javascript", "Manual QA", "Yead of Engineering", "Support Agent", "QA Engineer", " Node.js",
                "продуктовый аналитик", "по подбору персонала", "Quality Control Management", "Head of Product Support",
                "Системный Администратор", " CX/UX исследователь", "Web-разработчик", "Middle PHP", "Laravel developer",
                "Email-маркетолог", "ассистент руководителя", "Преподаватель IT дисциплин для детей и подростков",
                "Рекрутер it", " Social Media Specialist", "SMM специалист", "SMM-проектов", "Data Engineer",
                ),

        'mincl': (" PM"," РМ"),
        # pattern['pm']['ma']=set(pattern['project']['mdef']).union(set(pattern['pm']['mincl'])).union(set(pattern['product']['mdef']))


        'sub': {
            'project':{
                'ma': (),
                'ma2': (),
                'mdef': ("Руководитель интернет-проект","Руководитель IT-проект","Руководитель IT проект","Скрам мастер",
                        "Scrum Master","Менеджер IT проектов","Менеджер IT-проекта","[Рр]уководител[ья] проект",
                        "Agile coach","Руководитель интернет-проектов","Руководитель ИТ-проект","Проджект менеджер",
                        "Проектный Менеджер","Управляющий проект","Project-manager","project manager","Project Manager",
                        " PM.", " PM,", " PM ", "Project manager","Руководитель программы проектов","Менеджер проект",
                        "Руководитель проектов","Менеджер проектов","Project Manager","[Jj]unior [Pp]roject [Mm]anager",
                        "Менеджер по продукту","Менеджер по запуску производства","Инженер сопровождения контрактных разработок",
                         "[Мм]енеджер [Пп]роект", "[Рр]уководитель [Пп]роект", "[Сс]пециалист по [Аа]дминистрированию [Пп]роект",
                         "[Рр]уководитель [Нн]аправления"),

                'mex': ("Руководитель проектов по бюджетированию ФОТ","Marketing Project Manager","Менеджер маркетинговых проектов"),
                'mex2': (),
                'mincl': ()
            },

            'product':{
                'ma': (),
                'ma2': (),
                'mdef': ("Senior Product-Manager","[Pp]roduct [Mm]anager","Продакт-менеджер","[Pp]roduct [Oo]wner",
                         "PrdM", "Head of Core Product","продуктолог","Growth Hacker", " CPO", "Head of Product",
                         "Product Lead", "Директор по продукту", "/CPO", " CPO","ProductManager","Growth Product Manager",
                         "Руководитель отдела продукта",
                    ),
                'mex': (),
                'mex2': (),
                'mincl': ()
            }
        }
    },

#     #capitalize
    'game': {
        'ma': ("Game ", "game ", "games", "[/ ][Uu]nity", "[Uu]nreal","[Cc]ry[Ee]ngine","[Uu]nitry", "[Gg]odot",
               "character artist","Senior Gameplay Engineer", "background artist", "environment artist", "concept artist",
               "layout 3d artist", "Game Designer", "Программиста игровой логики", "RPG","Геймдизайнер",
               "UE4 Developer","Разработчик на Unity",),
        'mex': ("UI/UX Designer",),
        'ma2': (),
        'mdef': ("Unity разработчик", ),
        'mex2': (),
        'mincl': ()
        },

#     # capitalize
    'designer': {
        'ma': (),
        'ma2': ("[Dd]esigner", "[Дд]изайнер", "[Pp]roduct [Dd]esigner", "[Pp]hotoshop [Mm]anager", "[Cc]oncept [Aa]rtist",
                "[Aa]rtist","[Аа]рт-[Дд]иректор", "[Dd]igital [Dd]esigner","[Pp]roduct [Dd]esigner","[Hh]ead of [Dd]esign",
                "[Dd]igital [Aa]rt [Dd]irector", "[Кк]реативный дизайнер"),
        'mdef': ("[Тт]ехнический дизайнер", "[Пп]родуктовый дизайнер", "Арт-директор"),
        'mex': (),
        'mex2': ("дизайнеры", "Artec 3D", "3D scanners", "Web UI", "Product manager", "Product owner",
                 "из дизайнера", "из Дизайнера", "designers", "3D Unity", "3D unity", "Unity 3D",
                 "Understanding UI state", "Material UI", "до UI",
                 "PostgreSQL", "MySQL", "Senior Dealer", "Инженер-электронщик", "VueRouter", "Vuex",
                 "Unity Dev",  "Rest Api", "SQLite", "Оператор call-центра","Инженер-программист",
                 "Angular", "bitrix", "битрикс","Специалист по работе с клиентами","Retention Spesialist",
                 "json", "JSON",  "HRD","Консультант SAP","ремонтов квартир","Специалист по контенту",
                 "запуск производства","керамист","мебели","мебельного","мужской одежды",
                 "детской одежды","Business Development","Data acquisition manager","футболки","кофров", "чехлов",
                 "Проектировщик","интерьеров","Менеджер по продажам","квартир","СММ Менеджер",
                 "интерьера","ремонта квартир","Менеджер по маркетплейсам","специалист по подбору персонала",
                 "Менеджер по продажам",
                 "отдела продаж","PR IT", "женской одежды",
                 "Нужен менеджер",
                 "Ассистент руководителя","Главный редактор","ассистент руководителя",
                 "Консультант","Продюсер","Аккаунт-менеджер","Creative screenwriter","Менеджер по рекламе"
                 "подбора персонала","видеограф","копирайтер","Менеджер по развитию интернет проектов",
                 "Аналитик","JoomShopping","в команде с дизайнером","Unity developer", "контентмейкер","видеоконтентмейкер",
                 "блоггер","с командой дизайнеров","Ресечер","Аналитик DWH","Авитолог","#ProductManager"
                 "Специалист по контекстной рекламе","Веб-мастер","Product Owner","Менеджер YouTube-канала","Аккаунт-менеджер",
                 "[Дд]изайнер интерьер", "[Дд]изайнер упаковки", "[Дд]изайнер-консультант", "Разработчик-программист"),
        'mincl': (),
        # pattern['designer']['mex']=set(pattern['DEV']['mex']).union(set(pattern['mobile']['ma'])).union(set(pattern['designer']['mex2'])).union(set(pattern['qa']['mdef'])).union(set(pattern['sales_manager']['ma'])).union(set(pattern['marketing']['ma'])).union(set(pattern['ba']['ma'])).union(set(pattern['pm']['ma'])).union(set(pattern['devops']['ma'])).union(set(pattern['analyst']['ma'])).union(set(pattern['hr']['mdef']))
        # pattern['designer']['mexfinal']=set(pattern['designer']['mex']).union(set(pattern['DetailedDesigners']['ma']))
        'sub': {
                'ui_ux':{
                    'ma':("[Uu][Xx]/[Uu][Ii]","[Uu][Ii]/[Uu][Xx]","UX", "UI", " CX исследователь"," UI/UX designer",
                        "UI Designer","UI designer","CRO manager","Mobile Designer","Веб-дизайнер","UX-писатель",),
                    'ma2': (),
                    'mdef': ("[Дд]изайнер [Ии]нтерфейсов", ),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['UX/UI']['mex']=set(pattern['designer']['mex']).union(set(pattern['UX/UI']['mex2'])),
                }   ,

                'motion':{
                    'ma':("[Mm]otion",),
                    'ma2': (),
                    'mdef': ("[Mm]otion [Dd]esigner",),
                    'mex': (),
                    'mex2': ("[Mm]otion [Dd]esign", "3D будет преимуществом"),
                    'mincl': ()
                    # pattern['Motion']['mex']=set(pattern['designer']['mex']).union(set(pattern['Motion']['mex2'])),
                },

                'dd':{
                    'ma':("2D", "2D Designer","2D дизайнер"),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['2D']['mex']=set(pattern['designer']['mex']).union(set(pattern['2D']['mex2'])),
                }   ,

                'ddd':{
                    'ma':("3D", ),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':("[Mm]otion [Dd]esign, 3D будет преимуществом","3D lead"),
                    'mincl': ()
                    # pattern['3D']['mex']=set(pattern['designer']['mex']).union(set(pattern['3D']['mex2'])),
                }   ,

                'game_designer':{
                    'ma':("[Cc]haracter [Aa]rtist", "[Bb]ackground [Aa]rtist", "[Ee]nvironment [Aa]rtist",
                        "[Ll]ayout 3[Dd] [Aa]rtist","Дизайнер Квестов","[Gg]ame [Dd]esigner","[Гг]еймдизайнер",
                        "[Ll]evel [Aa]rtist","[Ии]гровое","риггер","риггинг","скиннинг","spine animator", "[Гг]ейм-[Дд]изайнер"),
                    'ma2': (),
                    'mdef': ("2д лвл дизайнер", "VFX Animator"),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()

                    # pattern['GameDesigner']['mex']=set(pattern['designer']['mex']).union(set(pattern['GameDesigner']['mex2'])),
                } ,

                'illustrator':{
                    'ma':("[Ии]ллюстратор",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['illustrator']['mex']=set(pattern['designer']['mex']).union(set(pattern['illustrator']['mex2'])),
                } ,

                'graphic':{
                    'ma':("[Гг]рафический дизайнер","[Гг]рафическому дизайн","фирменным стилем", "брендбука", "полиграфической продукции", "полиграфическая продукция",
                        "рекламных визуальных концепций","презентаций", "визиток", "буклетов", "каталогов", "открыток", "упаковки",
                        "графическим дизайнером", "баннеры","Веб-дизайнер","Web-дизайнер","WEB дизайнер","Graphic Designer","Художник - дизайнер",
                        "Web-дизайнер", "Дизайнер маркетплейс","Дизайнер сайтов на Tilda","наружная реклама","Дизайнер макетов","Дизайнер-верстальщик"),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['Graphic']['mex']=set(pattern['designer']['mex']).union(set(pattern['Graphic']['mex2'])),
                } ,

                'uxre_searcher':{
                    'ma': (" CX исследователь","CX/UX исследователь",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['UXREsearcher']['mex']=set(pattern['designer']['mex']).union(set(pattern['UXREsearcher']['mex2'])),
                }
        }
        # pattern['DetailedDesigners']['ma']=set(pattern['UX/UI']['ma']).union(set(pattern['Motion']['ma']))
        # .union(set(pattern['2D']['ma'])).union(set(pattern['3D']['ma'])).union(set(pattern['GameDesigner']['ma']))
        # .union(set(pattern['illustrator']['ma'])).union(set(pattern['Graphic']['ma']))
        # .union(set(pattern['UXREsearcher']['ma']))

    },
#     # capitalize
    'hr': {
        'ma': ("Human Resources Officer", " HR", "recruter", "кадр", "human r", "head hunter", "Кадр", "HR BP",
               "HR Бизнес-партнер", "IT Recruiter", "Recruiter", "HRD", "IT рекрутер","менеджер по подбору персонала",
               "подбора персонала","IT Recruiter","Position:IT Recruiter","Junior IT рекрутер",
               "специалист по подбору персонала","HCM","ресерчер",),
        'ma2': (),
        'mdef': ("Специалист по подбору персонала", "менеджер по подбору персонал", "младший специалист HR"),
        'mex': ("Скрининг с HR", "я HR", "представляю кадровое агентство", "Общение с HR", "общение с HR", "HR_",
                "HRTech", "HR департамент", "SEO HR", "HR@", "Кадровое агенство", "звонок с HR ",
                "Пишите нашему HR-менеджеру", "HR-Link", "HR-Prime", "HR-у", "Контакт HR", "Связаться с HR",
                "Вакансия: Android  developer", "встреча с HRD", "HR-специалистом", "Android  developer", "Созвон с HR",
                "Frontent developer", "TeamLead Python", "Senior DevOps", "Middle devops", "Java Developer",
                "Раскадровщик", "@Recruiter", "@IraRecruiter", "разработчика BackEnd", "3D художников",
                "Вакансия: DevOps", "Data engineer", "Senior Android", "Разработчик Bitrix24", "Devops",
                "Менеджер по продажам", "Data entry", "Senior PHP Developer", "DevOps Engineer", "Я Саша, ИТ-рекрутер",
                "пишите в телеграмм нашему HR", "пишите нашему HR", "Mobile QA", "Front-end инженер", "Программиста игровой логики",
                "я - HR", "Business Development Specialist", "Вакансия: Project Manager", "UI/UX Designer","Арт-директор",
                "в HR-платформу"),
        'mex2': (),
        'mincl': ()
    },
#     # capitalize
    'analyst': {
        'ma': (
            "[Аа]налитик", "[Aa]nalyst ","[Ww]eb-аналитик"
             "SOC Analyst", "Performance аналитик", "Маркетинг аналитик", "Старший аналитик", "Тимлид аналитики",
            "Machine Learning", "Ведущий аналитик", "Младший аналитик",),
        'ma2': (),
        'mdef':("[Aa]nalyst", "[Аа]налитик\)", "[Аа]налитик трафика", "[Аа]нти-фрод", "[Аа]ссистент консультанта BI",
                "[Mm]arketing [Aa]nalyst", "[Аа]налитик данных", "Core Gameplay Designer", "аналитик 1С"),

        'mex': ("Senior Product Designer (UX/UI)", "Product manager", "Senior Dealer", "Консультант",
                "backend engineer", "Product Manager", "QA Engineer", "Product Manager", "BACKEND", "AQA",
                "Вакансия: Менеджер по продукту", "Backend Engineer", "Frontend Engineer", "Manual QA", "Вакансия: Project Manager",
                "Проект-менеджер","Product Owner","Data Scientist","JoomShopping","в команде с дизайнером","Unity developer",
                "подбора персонала","видеограф","копирайтер","журналист","Менеджер по развитию интернет проектов",
                "Email маркетолог","CRM маркетолог","Email-маркетолог","CRM-маркетолог","видеоконтентмейкер",
                "Директолог","Контекстолог","Специалист по рекламе","Оператор call-центра","Инженер-программист",
                "Консультант","Трафик-менеджер","Продюсер","Аккаунт-менеджер","контекстной рекламе","Creative screenwriter",
                "контентмейкер","Проджект менеджер","project manager","интерьера","ремонта квартир","Менеджер по маркетплейсам"
                "SMM-специалист","Интернет-маркетолог","Менеджер по продажам","SMM-маркетолог","SMM-менеджер",
                "Таргетолог","Менеджер маркетплейсов","Маркетолог","SMM-маркетолог","Копирайтер-редактор",
                "отдела продаж","Копирайтер","SEO консультант","Менеджер Wildberries","PR IT", "женской одежды",
                "Менеджер по оптовым продажам","по работе с маркетплейсами","front-end разработчик","Нужен менеджер",
                "Руководитель контентной команды","по работе с клиентами","Retention Spesialist",
                "Ассистент руководителя","SMMдизайнер","Главный редактор","SEO-специалист","ассистент руководителя",
                "Media Buyer","Product Manager","Арбитражник","Медиабайер","Заместитель директора по маркетингу",
                "блоггер","SMM","с командой дизайнеров","Tech Writer","Product Owner","Ресечер",
                "специалист по подбору персонала","Продакт-менеджер", "Delphi", "рекрутера","ищем HR",
                "контентной","Верстальщик","Арт-директор","Full-Stack Developer","Team Lead","Senior Backend разработчик",
                "Frontend engineer","Senior Android developer","PHP-программист","Разработчик PHP","Developer PHP",
                "Python-разработчик","маркетолог","QA","по продажам","архитектор","по продаже мебели",
                "kotlin developer","Load Test Engineer","Scrum Master","помощник руководителя","квартир",
                "Team Lead PHP","front-end developer","Проектный менеджер","PR-менеджер","Product Officer",
                "Программист 1С", "Android разработчик","Unreal Gameplay Programmer","Инженер по развитию",
                "Sales Assistant","Embedded Developer","Product Designer","sysadmin","Frontend React",
                "VueJS developer","Психолог","Full Stack Developer","Web-разработчик","Vue-разработчик",
                "Frontend-разработчик","Agile coach","Инженер-программист","DevOps engineer","Node.js",
                ".Net ","C\+\+ developer","Support Engineer","Разработчик Python","IT Architect","Virtual Assistant",
                "Sales Researcher","Ruby developer","Game designer","отдела продаж","Разработчик Bitrix24",
                "Go developer","Computer Vision Engineer","SRE","DevOps специалист","C\+\+ разработчик",
                "E-mail маркетолог"," Java developer","Scala разработчик","UX-редактор","iOS Developer",
                "unity программист","Руководитель интернет-проектов","Руководитель IT-проектов","CX исследователь",
                "Flutter developer","Бизнес-ассистент","Визуализатор","Product Support","Специалист по трафику",
                "курса Web-разработка","Руководитель CRM маркетинга","Менеджер по развитию интернет проектов",
                "Information Security Specialist","по настройке контекстной рекламы","Fullstack разработчик",
                "специалист отдела сопровождения слушателей","QA Automation","Куратор по маркетингу","финансист",
                "Системный Администратор", "Frontend Developer","Скрам мастер","spine animator","менеджер WB",
                ),
        'mex2': (),
        'mincl': (),

        'sub': {
                'sys_analyst':{
                    'ma':( "[Ss]ystem [Aa]nalyst","[Сс]истемного [Aа]налитика","#SA",  "[Сс]истемный [Аа]налитик",),
                    'mex2':(),
                    'ma2': (),
                    'mdef': ("[Сс]истемный аналитик", ),
                    'mex': (),
                    'mincl': ()
                    # pattern['SysAnal']['mex']=set(pattern['marketing']['mex']).union(set(pattern['SysAnal']['mex2'])),
                    },

                'data_analyst':{
                    'ma':("[Dd]ata [Aa]nalyst", "[Аа]налитик [Дд]анных", "[Dd]ata [Mm]odeler","[Пп]родуктовый [Аа]налитик","[Pp]roduct [Aa]nalyst","[Dd][Ww][Hh]","[Мм]ладший [Аа]налитик","[Дд]ата-[Аа]налитик",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['DataAnal']['mex']=set(pattern['marketing']['mex']).union(set(pattern['DataAnal']['mex2'])),
                },

                'data_scientist':{
                    'ma':( "[Dd]ata [Ss]cientist","[Dd]ata [Ss]cience", "[Dd]ata[Ss]cientist","[Dd]ats [Ss]cientist", ),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['DataScientist']['mex']=set(pattern['marketing']['mex']).union(set(pattern['DataScientist']['mex2'])),
                },

                'ba':{
                    'ma':("[Bb]usiness [Aa]nalyst","[Bb]usiness-[Aa]nalyst","BI [Ee]ngineer", "[Бб]изнес-[Аа]налитик", "#BA", " BA,",
                        " BA ", " BA.", "[Бб]изнес [Аа]налитик","BI [Аа]рхитектор","Аналитик бизнес-процессов"),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['BA']['mex']=set(pattern['marketing']['mex']).union(set(pattern['BA']['mex2'])),
                },
        }
    },
#     # capitalize
    'qa': {
        'ma': (),
        'ma2': ( "по качеству", "[Тт]естировщик", "quality assurence", "тестер",
                "cucumber","SoapUI", "Postman", "POSTMAN","Soap", "postman"
               "#automation", "#selenium", "автотесты", "автотестов", "специалист по тестированию",
                ),
        'mdef':("заказного mobile", "Junior [Qq][Aa] [Ee]ngineer","mobile applications testing","[Qq][Aa] Lead",
                " [Qq][Aa] ","Quality Control Management", "Middle Тестировщик", "[Qq][Aa] [Ee]ngineer",
                "[Qq][Aa]-[Ee]ngineer","[Qq][Aa]-инженер","Вакансия: QA Инженер","#QA", "Фулл-стек тестировщик"),
        'mex': (),
        'mex2': ("тестировщиков", "тестировщиками", "проводить QA", " и QA", "to junior", "PHP Developer",
                "Senior Product Designer (UX/UI)", "Администратор баз данных", "DBA", "Ios developer middle",
                "Менеджер В2В", "Manager B2B", "Senior front-end developer", "Frontend разработчик", "#react",
                "C\+\+ Gameplay Developer", "Front-end developer", "Frontend developer", "Grooming artist",
                "Backend-разработчик", "Back-end-разработчик", "Tech lead", "Go developer", "Middle ux/ui",
                "#nodejs", "Senior it recruiter", "Вакансия: iOS developer", "Vue разработчик", "Вакансия: Менеджер проектов",
                "Вакансия: Project Manager", " Go Developer", "Android-разработчик","Android разработчик"),
        'mincl': (),

        'sub': {
            'manual_qa':{
                'ma':("[Mm]anual [Tt]esting","[Mm]anual [Qq][Aa]", "[Qq][Aa] [Mm]anual","[Jj]unior [Mm]anual [Qq][Aa]",),
                'ma2': (),
                'mdef': ("[Mm]anual-QA", "[Рр]учной тестировщика"),
                'mex': (),
                'mex2':(),
                'mincl': ()
                # pattern['ManualQA']['mex']=set(pattern['marketing']['mex']).union(set(pattern['ManualQA']['mex2'])),
            },

            'aqa':{
                'ma':("[Qq][Aa] [Aa]utomation", "[Qq][Aa] [Aa]uto", "[Tt]est [Aa]utomation [Ee]ngineer","QA [Aa]utomation","[Aa][Qq][Aa]", "[Qq][Aa][Aa]","Вакансия: [Aa]utomation QA","#AutomationQA",),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2':(),
                'mincl': ()
                # pattern['AQA']['mex']=set(pattern['marketing']['mex']).union(set(pattern['AQA']['mex2'])),
            },


            'support': {
                'ma':("Head of Product Support", "специалист технической поддержки","Customer Support Specialist","Оператор call-центра",),
                'ma2': (),
                'mdef': (),
                'mex': (),
                'mex2': (),
                'mincl': ()
            }
        }
    },
#     # capitize
    'devops': {
        'ma': ("DevSecOps", "инженера по информационной безопасности", "DevOps", "SRE", "Site Reliability Engineer",
               "Cloud Engineer", "DBA", "Администратор баз данных", "Linux System Administrator", "Network administration",
               "Network architect","Systems Engineer","Системного администратора","[Сс]истемный [Аа]дминистратор", "Инженер-системотехник",
               "Core Engineer","Администратор", "администратор", "[Бб]аз данных","[Бб]азы данных",
               "Системный Администратор Linux","SRE-инженер","Senior Devops","на позицию DevOps","эникей",
               "[Dd][Ee][Vv][Oo][Pp][Ss]"),

        'ma2': (),
        'mdef': ("[Jj]unior [Dd]ev[Oo]ps", "[Dd]ev[O]ps-инженер", "[Dd]ev[Oo]ps [Ии]нженер,"),
        'mex': (" и SRE", ", DevOps,", "DevOps командой", "участвовать в DevOps", "Опыт DevOps", "участвуют в DevOps",
                "DevOps practices", "devops навыки", "DevOps tools", "Java Developer", "PHP разработчик",
                "Go разработчик", "Backend .NET Developer", "product lead", "Flutter разработчик", "Graphic designer",
                "Automation QA engineer", "Senior Java", "Sales manager", "QA  инженер", "Backend engineer", "Flutter",
                "React developer", "Системный аналитик", "Senior react developer", "Middle react developer",
                "Django", "Middle QA", "Mobile manual QA", "SeniorQA", "QA Automation (Python)", "По тестированию", "Участвуют в devops",
                "Участвовать в devops", "Участие в devops", "Copywriter", "Senior ux/ui", "Senior ui/ui", "Ruby разработчик",
                "Системный аналитик", "Senior python", "Ios разработчик", "Ios developer", "Middle ios", "Junior ios", "Senior ios",
                "QA Automation", "Sales Enablement Specialist", "Backend-разработчика", "Project manager","тестовые окружения",
                "ручное тестирование", "специалистов по тестированию","Менеджер проектов","Проект-менеджер","Artist","Scala Developer",
                "MLOps","autoML", "Business Intelligence","AQA","Machine learning developer","Тех.лид","Xamarin Developer","IT рекрутер",
                "Middle BackEnd"),
        'mex2': (),
        'mincl': ()
    },

    'marketing': {
        'ma': ("Marketer", "[Мм]аркетолог", "Marketing", "Менеджер по маркетингу",
               "Video Tutorial Creator", "Producer","Архитектор воронок","руководитель CRM",
               "User Acquisition", "CRO","ASO","CRM маркетолог","CRM-маркетолог","CRM Manager","CRM-аналитик",
               "контент","Таргетолог","Руководитель контентной команды",
               "Арбитражник","Заместитель директора по маркетингу","Senior Researcher","Research Teamlead","Market Research",
               "Специалист по рекламе","Digital маркетолог","контент-маркетинг","[Аа]витолог",
               "Трафик-менеджер","Marketing Specialist","Community Discord Manager",
               "Интернет-маркетолог","Marketing Manager", "Руководитель отдела маркетинга",
               "Менеджер маркетплейсов","Аккаунт-менеджер","Marketing Lead",
               "Креативный продюсер", "Креативный менеджер","Авитолог"," Менеджер по рекламе",
               "ТЗ-мейкер", "Специалист по маркетингу","PR IT","Интернет-маркетолог","редактор""Менеджер по развитию интернет проектов",
               "Маркетолог по воронкам", "куратор по маркетингу","Медиапланер","marketing manager", "маркетинга"),
        'ma2': (),
        'mdef': ("медиабайер", "Digital Planner", "менеджер по медиапланированию", "Media Planner",
                 "Редактор телеграм-канала", "Content Manager", "PR-менеджер", "[Aa]ccount [Mm]eneger",
                 "Аффилиатный Менеджер", "Affiliate manager", "[Tt]echnical [Ww]riter", "[Aa]dvertising manager"),
        'mex': ("SEO HR", "Product manager", "SEO HR", "HRBP", "Sales Manager", "Manual QA", "Product Manager", "Back-end", "Kotlin Developer",
                "Middle Business Analyst", "PHP Developer","DevOps","C# Developer","Lead Business Analyst", "Data Scientist", "System Administrator",
                "Project manager", "ищет веб-дизайнер", "ищем веб-дизайнер","Product Owner","CEO", "Lead Generation", "IT-specialist",
                "Front-end", "Product designer", "Менеджер проектов","Проект-менеджер","Full stack", "Level Designer", "Artist", "Креативный продюсер",
                "Менеджер по продажам", "Fullstack","SRE", "Head of Digital",),
        'mex2': (),
        'mincl': (),

        'sub': {
                'smm': {
                    'ma':("SMM","SMMдизайнер","SMM-маркетолог","SMM-менеджер","SMM-специалист","SMM Specialist","SMM менеджер","SMM - specialist",
                        "Руководитель отдела SMM","SMM manager"),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['SMM']['mex']=set(pattern['smm']['mex']).union(set(pattern['SMM']['mex2'])),
                },

                'copyrighter': {
                    'ma':("[Cc]opyrighter","[Кк]опирайтер","Копирайтер-редактор",),
                    'ma2': (),
                    'mdef': ('[Кк]опирайтер',),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()

                    # pattern['Copyrighter']['mex']=set(pattern['marketing']['mex']).union(set(pattern['Copyrighter']['mex2'])),
                },

                'seo':{
                    'ma':("SEO","SEO-специалист","SEO специалист","SEO консультант",),
                    'ma2': (),
                    'mdef': ("SEO-специалист",),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['SEO']['mex']=set(pattern['marketing']['mex']).union(set(pattern['SEO']['mex2'])),
                },

                'link_builder':{
                    'ma':("[Ll]ink[Bb]uilder","Link Builder","линкбилдинг",),
                    'ma2': (),
                    'mdef': ('SEO-специалист',),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['LinkBuilder']['mex']=set(pattern['marketing']['mex']).union(set(pattern['LinkBuilder']['mex2'])),
                },

                'media_buyer':{
                    'ma':("[Mm]edia [Bb]uyer","Медиабайер",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['MediaBuyer']['mex']=set(pattern['marketing']['mex']).union(set(pattern['MediaBuyer']['mex2'])),
                },

                'email_marketer':{
                    'ma':("Email маркетолог","Email-маркетолог","Email- маркетолог",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['EmailMarketer']['mex']=set(pattern['marketing']['mex']).union(set(pattern['EmailMarketer']['mex2'])),
                },

                'LeadGenerationMarketing':{
                    'ma':("Lead Generation Specialist", "#leadgeneration",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['LeadGenerationMarketing']['mex']=set(pattern['marketing']['mex']).union(set(pattern['LeadGenerationMarketing']['mex2'])),
                },

                'context':{
                    'ma':("Директолог","Контекстолог","контекстной реклам[еы]","контекстная реклама",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['Kontekst']['mex']=set(pattern['marketing']['mex']).union(set(pattern['Kontekst']['mex2'])),
                },

                'content_manager':{
                    'ma':("[Кк]онтент-менеджер","Менеджер по контенту","Web Content Manager", "Content Manager",),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['ContentManager']['mex']=set(pattern['marketing']['mex']).union(set(pattern['ContentManager']['mex2'])),
                },

                'tech_writer':{
                    'ma':("[Tt]ech [Ww]riter","[Тт]ехнический [Пп]исатель"),
                    'ma2': (),
                    'mdef': (),
                    'mex': (),
                    'mex2':(),
                    'mincl': ()
                    # pattern['TechWriter']['mex']=set(pattern['marketing']['mex']).union(set(pattern['TechWriter']['mex2'])),
                }
        }
    },

    'sales_manager': {
        'ma': ("Sales manager", "sales manager", "Sales Manager", "[Мм]енеджера по продаж", "[Мм]енеджер холодных продаж",
               "[Мм]енеджер по продаж", "менеджер_отдела_продаж", "Lead Generation", "IT Sales Researcher", "#leadgeneration","User Acquisition",
               "CRO", "Sales Researcher","Менеджер по оптовым продажам",
               "Pre-sale manager","Руководитель отдела продаж","Business Development Manager","Sales Assistant", "sales manager","Business Development","Lead Generation",),
        'ma2': (),
        'mdef': ("Специалист по продажам", "Менеджер по развитию бизнеса", "менеджер по развитию", "менеджер по работе с клиентами",
                 "[Hh]ead of [Ss]ales"),
        'mex': ("Python-разработчика","Системного администратора","NodeJS Developer","Project Manager"," DevOps Engineer"),
        'mex2': (),
        'mincl': ()
    },

    'non_code_manager':{
        'ma':("Менеджер по ведению телеграмм канала","Менеджер Вайлдберис","Менеджер WB","Менеджер по маркетплейсам",
              "Менеджер Wildberries","Менеджер маркетплейсов","по работе с маркетплейсами",),
        'ma2': (),
        'mdef': (),
        'mex':(),
        'mex2': (),
        'mincl': ()
    },

    'junior': {
        'ma': ("[Tt]rainee", "[Jj]unior", "[Дд]жун", "Начинающий программист","Начинающего программист", "[Сс]таж[ёе]р", "[Ii]nternship","от 1 года"),
        'ma2': (),
        'mdef': (),
        'mex': ("не готовы рассматривать", "джуниоров пока не рассматриваем","Junior не рассматриваем",
                "джуниоров к сожалению пока не рассматриваем", "джуниоров, к сожалению, пока не рассматриваем",
                "Работать с junior", "Senior Sales Manager", "не рассматриваем Junior", "Required 5 to 7 Years",
                "джуниоров к сожалению пока не смотрим!", "QA Lead", "Senior QA", "Supervise junior","Senior",
                "We do not plan to hire Junior", "middle","позиции Junior специалистов пока не актуальны", "джуниоров не смотрим",
                "от 2-х лет","от двух лет","от 2х лет","от 2 лет", "3+ years of experience","2+ years of experience",
                "Не менее 2-3 лет работы", " от 3 лет", "от 3-х лет", "не менее 3 лет","3+ years ","Senior product", "Senior Product", "senior product",
                "2 года","Менторить младших разработчиков", "Senior Javascript","3+ years of experience","Senior Gameplay",
                "3 years of professional","Опыт работы от трёх лет","3+ years of Product Management experience",
                "Senior Go","Senior Front-End","Senior Front-End", "не менее трех лет"," Старший программист","Senior Software Developer",
                "Senior php developer","Team Lead","Senior Game Designer","senior developer","Senior Android Developer",
                "Руководитель отдела","for 5+ years","for 4+ years","не менее 2-х лет","не менее 3 х лет","менторство над 1-2 джунами",
                "готовим интернов и джунов","Easy(JS) сообществ","Senior IT Recruiter","Senior Google Media Buyer","Senior IT Recruiter",
                "развить его от джуна", "[Пп]реподаватель", "Арт-директор", "без опыта", "интерн", "трэйни"),
        'mex2': (),
        'mincl': ()
    },

    'middle': {
        'ma': ("Middle", "midle", "мидл"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'senior': {
        'ma': ("Senior", "Team lead", " CTO", "сеньер", "сеньор","Sr."),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'remote': {
        'ma': ("[Уу]дал[её]н|remote", "remote", "удаленка", "удаленная", "удаленную работу", "удалённую работу", "удаленно", "удалённо"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'relocate': {
        'ma': ("relocate", "relocation", "релокация"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'country': {
        'ma': (
            "Тайланд", "Латвия", "Israel", "Израиль", "Moldova", "Молдова", "Dubai", "Дубаи", "РБ", "Беларусь",
            "Белорусь", "Belarus", "Грузия", "Georgia", "Россия", "Russia", "Kazakhstan", "Казахстан", "Украина",
            "Ukraine", "Армения", "РФ", "Poland", "Польша", "Spain", "Испания", "Germany", "Германия", "Romania",
            "США", "USA", "Финляндия", "Serbia", "Lithuania", "Кипр", "Турция"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'city': {
        'ma': ("Томск", "Рига", "Москва", "Ярославль", "Хельсинки", "Стамбул", "Санкт-Петербург", "Волгоград",
               "Екатеринбург", "Самара", "Киев", "Kyiv"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },

    'internship': {
        'ma': ("internship", "стажировка", "trainee"),
        'ma2': (),
        'mdef': (),
        'mex': (),
        'mex2': (),
        'mincl': ()
    },
}

params = {
    'company_hiring': ('[К,к]омпан[и,i][я,и,й][^\,"\n]{1,3}[#А-ЯA-Z][a-zA-Zа-яА-Я0-9]{2,20}[^\,"\n]{1}«{0,1}[А-ЯA-Z]{0,20}[A-ZА-Яa-zа-я]{0,20}',
                       '[C,c]ompany[^\,"\n]{1,3}[#А-ЯA-Z][a-zA-Zа-яА-Я0-9]{2,20}[^\,"\n]{1}«{0,1}[А-ЯA-Z]{0,20}[A-ZА-Яa-zа-я]{0,20}',
                       '[Р,р]аботодатель[^\,"\n]{1,3}[#А-ЯA-Z][a-zA-Zа-яА-Я0-9]{2,20}[^\,"\n]{1}«{0,1}[А-ЯA-Z]{0,20}[A-ZА-Яa-zа-я]{0,20}'),
    'country': (),
    'remote': ('[Rr]emote', '[Уу]дал[ёе][н]{1,2}[кыйоая]{0,2}', '[вВ]iддален[ийка]{0,2}', '[Гг]ибридн[ыйоеая]{0,2}',
               '[Оо]фис[\W]{1,3}[Гг\.]{0,3}[\W]{0,1}[A-ZА-Я]{1}[a-zа-я]{2,}'),
    'jobs_type': ('[Ff]ull[\W]{0,1}[Tt]ime', '[Зз]анятость[\W]{0,3}[Пп]олная', '[Пп]олная[\W]{1,3}[Зз]анятость',
                  'из офиса'),
    'english_level': ('[Ee]nglish[\W]{0,2}[A-Za-zА-Яа-я][\W]{0,3}[\d]', '[Uu]pper[\W]{0,1}intermediate', '[Ii]ntermediate', '[Pp]re[\W]{0,1}[Ii]ntermediate', '[Uu]pper'),
    'relocation': ('[Рр]елокация', 'relocation', 'relocate'),
    'country_relocation': (),
    'possibility_relocaton': (),
    'experience': {"[0-9] лет|[0-9] год|[0-9] year", },
    'english_for_shorts': {'[Bb][^\na-zA-Zа-яА-Я0-9]?1|[Bb][^\na-zA-Zа-яА-Я0-9]?0|[Bb][^\na-zA-Zа-яА-Я0-9]?2|'
                           '[Aa][^\na-zA-Zа-яА-Я0-9]?1|[Aa][^\na-zA-Zа-яА-Я0-9]?0|[Aa][^\na-zA-Zа-яА-Я0-9]?2|'
                           '[Pp]re[^\na-zA-Zа-яА-Я][Ii]ntermediate|[Ii]ntermediate|[Uu]pper|[Aa]dvance|[Рр]азговорный',},
    'salary_for_shorts': {'[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*₽|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*\$|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*€|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*руб|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*млн|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*KZT|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*USD|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*EUR',},
    'city_for_shorts': cities_dict,
}

cities_pattern = {
    'Russia': (
        'Moscow', 'Москва', 'St.Petersburg', '[Сс][\W]{0,1}[Пп]етербург', '[Сс]анкт[\W]{0,1}[Пп]етербург',
        '[Ее]катеринбург', '[рР]оссия', '[Тт]омск', 'РФ', '[Уу]льяновск', 'Казань', '[Оо]мск[е]{0,1}',
        '[Тт]юмен[и]{0,1}', 'СПб'
    ),
    'Germany': ('[Гг]ермания', '[Фф]ранкфурт'),
    'others': ('г\.[^\n][\W]{0,2}[A-Za-zА-Яа-я_\-\s]{3,20}', ),
    'Estonia': ('[Tt]alli[n]{1,2}', '[Ээ]стонск[уюая]{2,3}'),
    'Latvia': ('[Rr]iga', '[Лл]атвия', ),
    'Poland': ('[Pp]oland', '[Пп]ольш[ае]{1}', '[Вв]роцлав'),
    'Bulgaria': ('[Bb]ulgaria', '[Бб]олгари[ия]{1}'),
    'Portugal': ('[Pp]ortugal', '[Пп]ортугали[ия]{1}'),
    'Spain': ('[Ss]pain', '[Ии]спани[яи]{1}'),
    'Ukraine': ('[Uu]kraine', '[Уу]краин[ае]{1}'),
    'Serbia': ('[Ss]erbia', '[Сс]ерби[ия]{1}'),
    'Armenia': ('[Aa]rmenia', '[Аа]рмени[яи]{1}'),
    'Georgia': ('[Gg]eorgia', '[Гг]рузи[ия]{1}'),
    'Kazakhstan': ('[Kk]azakhstan', '[Кк]азахстан[а]{0,1}', '[Нн]ур[\W]{0,1}[Сс]ултан'),
    'Argentina': ('[Aa]rgentina', '[Аа]ргентин[ае]{1}'),
    'Uruguay': ('[Uu]ruguay', '[Уу]ругва[йе]{1}'),
    'Colombia': ('[Cc]olombia', '[Кк]олумби[яи]{1}'),
    'Узбекистан': ('Ташкент', )
}

companies_list = [
    'Prof IT',
    'Русьтелетех',
    'Foreshko',
    'Distate',
    'Рт Мис',
    'Рт Мис',
    'Geniusto International',
    '3Keys',
    'Amarkets',
    'AppMagic',
    'Банк Урбир',
    'Konomic',
    'Excelsior',
    'Аукционный Дом',
    'GlobalTruck IT',
    'Gameram',
    'Bell Integrator',
    'Combridge itc',
    'GS Group',
    'Series Eight',
    'Pictureworks Group',
    'NewsCatcher',
    'MonetizeMore',
    'Juni',
    'Saber Interactive',
    'RapDev.io',
    'Mudflap',
    'Shaker',
    'Shake',
    'ReUp Education',
    'Higher Logic',
    'Bellroy',
    'Meraki',
    'Bluethumb',
    'Zeektek',
    'Professional Search Group',
    'Nova Credit',
    'AssemblyAI',
    'Weigandt Consulting',
    'HRlink',
    'Адалиск',
    'Сбер',
    'Север Авто',
    'Открытый Код',
    'Evercode Lab',
    'My Games',
    'ASH',
    'Домклик',
    'Excelsior',
    'Dcloud',
    'Perfomance',
    'Bolt',
    'Crypton Studio',
    'ProfUA',
    'DataArt dataart',
    'AGIMA',
    'PurrWeb',
    'Lockular',
    'Bloomex',
    'Waves',
    'DataArt',
    'Tinkoff',
    'Task Agency',
    'Syberry',
    'Andersen',
    'Ester Digital',
    'Selecty IT',
    'Selecty',
    'Winline',
    'ServiceNow',
    'Selecty IT',
    'Dekimo',
    'Парсек Лаб',
    'Advascale',
    'OTUS',
    'Taxes For',
    'CactusSoft',
    'Robokassa',
    'GitNation',
    'Sheverev',
    'TISS',
    'Синимекс',
    'Элоконт',
    'SpurIT',
    'SoftJet',
    'Wildberries',
    'Geomotiv',
    'ShareSpace',
    'Rebrandium web',
    'Styledna.ai',
    'Bell Integrator',
    'FundCount',
    'СОРСО-СТР',
    'Яндекс',
    'Robokassa',
    'Ennabl',
    'Selecty IT',
    'Cetra',
    'SoftTeco',
    'Atomichronica',
    'TechReactGroup',
    'Amazon',
    'Rocketech.it',
    'Selecty IT',
    'Remoby',
    'Очень Интересно',
    'Блокчейн',
    'Азбука знаний',
    'RiACT',
    'DataGo!',
    'Ailet',
    'Смарт Юнит',
    'CactusSoft',
    'SoftTeco',
    'Delta Solutions',
    'Кредит Европа Банк',
    'Gazprom-Media',
    'OTUS',
    'Pixellu',
    'NGRS',
    'SoftTeco',
    'WifiMap',
    'ORTALEX',
    'Improvado',
    'CactusSoft',
    'TopSelection',
    'TopSelection',
    'TaskAgency',
    'МТС Digital',
    'Embacy',
    'TopSelection',
    'AtsAero',
    'Финтех индустрия',
    'Систематика',
    'Task Agency',
    'IBA Group',
    'Helmes',
    'Geomotiv',
    'GloboGames',
    'Credix',
    'MMD Smart',
    'Ингосстрах',
    'AppFox',
    'Meta',
    'Виэйинтеллидженс',
    'UTORG',
    'Почта банк',
    'Brainway',
    'Antilatency',
    'СВД ВС',
    'Society of Programmers Agency',
    'CloudX',
    'SimpleSales',
    'Альфа Банк',
    'Meta',
    'IBS',
    'Тим Кук',
    'Синхро',
    'ТетраСофт',
    'Mad Devs',
    'Positive Technologies',
    'Webinar',
    'Мирадор',
    'Darwin Tech Labs',
    'MMD Smart',
    'Remoby',
    'Ртим',
    'Meta',
    'Интерсвязь',
    'Evolution',
    'Mimesis Inc',
    'ITFB Group',
    'BufferGrou',
    'РСХБ Интех',
    'URSiP',
    'Exness',
    'СберМаркет',
    'Soft Jet',
    'Soft Jet',
    'Super Protocol',
    'OZON',
    'Forest Valley',
    'Society of Programmers Agency',
    'DZSystems',
    'Mir Plat.Form',
    'Codex Optimus',
    'Scout24',
    'Meta',
    'Феникс-Групп',
    'Click',
    '3KNET',
    'Star-staff',
    'Soft Jet',
    'Creative',
    'AppFox',
    'Meta',
    'EnjoyPRO',
    'Profua',
    'Agoda',
    'Meta',
    'IBS',
    'TORIBIO TECH SRL',
    'КСК эксперт',
    'Meta',
    'Meta',
    'Center-Game',
    'Tax Free',
    'FNTASTIC',
    'Bell Integrator',
    'PlayFlock',
    'Конфитрейд',
    'Transition Technologies',
    'Rho AI',
    'Transition Technologies',
    'Transition Technologies',
    'Meta',
    'Интерсвязь',
    'Aldo | Austin, TX',
    'Maxilect',
    'Meta',
    'Geomotiv',
    'KEMBERTON HEALTHCARE SERVICES LLC',
    'Washington Technology Industry Association',
    'Mission Cloud Services',
    'Center Pixel',
    'Iron Forge Development',
    'Exness',
    'Конфитрейд',
    'ДОМ.РФ',
    'Демедиа',
    'Benefactory',
    'AppFox',
    'AppFox',
    'Ртим',
    'Ртим',
    'Aston',
    'Limavi',
    'Nox',
    'Rush Agency',
    'Garpix',
    'Superdao.co',
    'Геном.Эксперт',
    'ZenBit',
    'Greenmesh',
    'Payme',
    'СенамаСофт',
    'Pivotics',
    'Pivotics',
    'ЗащитаИнфо Транс',
    'КСК эксперт',
    'SmartBrain.io',
    'ORCA.codes',
    'Bracket',
    'Zazmic Inc',
    'Polygant',
    'Meta',
    'Yucca.digital',
    'Группа Компаний Черкизово',
    'Yucca.digital',
    'BSL',
    'ПартКом',
    'BSL',
    'Mindall',
    'BetBoom',
    'Gcompany',
    'Оrmatek',
    'MarketPapa',
    'SNDGroup',
    'Softmedialab',
    'Виэйинтеллидженс',
    'SoftTeco',
    'Payme',
    'Meta',
    'CV Recruitment',
    'TalkBank',
    'Game Industry',
    'Next Games',
    'Hello, Doc!',
    'Global Career',
    'Bitlica inc',
    'Society of Programmers Agency',
    'Leidos',
    'Transition Technologies',
    'Transition Technologies',
    'Neybox Digital',
    'Marketing for Change Co',
    'CircleLink Health',
    'Leidos',
    'ProShop',
    'Webbee',
    'SAPRUN',
    'Gcompany',
    'МТС BigData',
    'PlayFlock',
    'Синхро',
    'Sheverev',
    'Синхро',
    'ЗащитаИнфо Транс',
    'Selecty',
    'Bell Integrator',
    'DynamicSun',
    'Техно Диасофт',
    'Task Agency',
    'Bell Integrator',
    'Medical Licencing',
    'Medical Licencing',
    'Centicore',
    'Программные решения плюс',
    'Toimi',
    'Task Agency',
    'Neon EVM',
    'Star-Staff',
    'Videoseed',
    'Emerging Travel Group',
    'Antilatency',
    'Task Agency',
    'Ethplorer.io',
    'Nitka Technologies',
    'DocsInBox',
    'Selecty IT',
    'Selecty IT',
    'PITBel Group',
    'DevHunt',
    'Wisercat',
    'ColorNew',
    'SenamaSoft',
    'Artezio',
    'FinCube',
    'Lea Soft',
    'ЕМС-М',
    'GrowFood',
    'Elinext',
    'ЕМС-М',
    'ORIGINS_DIGITAL',
    'Elinext',
    'HeadFinder',
    'ДНК',
    'Elinext',
    'PMP TECH',
    'Geomotiv',
    'Greenmesh',
    'Zenbit',
    'HelviX GmbH',
    'Profua',
    'OTUS',
    'Super Dispatch',
    'Dayl Group',
    'Читай-Город — Буквоед',
    'Prosper Marketplace',
    'Prosper Marketplace',
    'Keep Calm',
    'Zborka labs',
    'Xenna',
    'Atomichronica',
    'Profua',
    'Zenbit',
    'HashEx',
    'Nexters',
    'SimpleSales',
    'Upstairs',
    'Kaller',
    'Aggregion',
    'Novartis',
    'Maxar Technologies',
    'Laserfiche',
    'Leidos',
    'Amazon Dev Center',
    'Gallium Studios',
    'Sagitec',
    'Wheel',
    'Aha!',
    'Nagarro',
    'Тинькофф',
    'IBS',
    'Devquality',
    'Сервионика',
    'Devquality',
    'NAPA AUTOMOTIVE',
    'Exness',
    'Lea Soft',
    'Agoda',
    'ReTech labs',
    'Zazmic Inc',
    'Мосгортур',
    'Ethplorer.io',
    'ATTRA',
    'Global Career',
    'Global Career',
    'Prosper Marketplace',
    'Access Softek',
    'TechHive',
    'Like Центр',
    'EDSTEIN',
    'Upstairs',
    'SoftTeco',
    'Profua',
    'Citrix',
    'Aegis Foundry',
    'Nationwide IT Services',
    'VSolvit LLC',
    'IBS',
    'IBS',
    'IBS',
    'RUSSPASS',
    'Тинькофф',
    'Крауд' ,
    'Lea Soft',
    'Pixellu',
    'Smartbrain',
    'Smartbrain',
    'Bell Integrator',
    'BullPerks',
    'Carle Health',
    'UtilityAPI',
    'Fordewind',
    'PMP Tech',
    'Ennuviz',
    'Clever Jobs',
    'Hyland Software',
]

companies_set = {
    'Helmes',
    'Открытый Код',
    'Яндекс',
    'Демедиа',
    'Evercode Lab',
    'Zborka labs',
    'ТетраСофт',
    'СВД ВС',
    'Exness',
    'Distate',
    'Ennuviz',
    'Sheverev',
    'ReUp Education',
    'Ртим',
    'Polygant',
    'Keep Calm',
    'Dekimo',
    'Prof IT',
    'OZON',
    'Банк Урбир',
    'Payme',
    'Сбер',
    'Credix',
    'Bitlica inc',
    'Soft Jet',
    'Maxilect',
    'Rocketech.it',
    'Аукционный Дом',
    'Excelsior',
    'Программные решения плюс',
    'Wheel',
    'Север Авто',
    'SoftJet',
    'SNDGroup',
    'Prosper Marketplace',
    'ShareSpace',
    '3Keys',
    'Clever Jobs',
    'AGIMA',
    'Tax Free',
    'Andersen',
    'Shaker',
    'Scout24',
    'Syberry',
    'Оrmatek',
    'Brainway',
    'Финтех индустрия',
    'Zazmic Inc',
    'SenamaSoft',
    'PMP Tech',
    'Bolt',
    'СберМаркет',
    'Robokassa',
    'Tinkoff',
    'My Games',
    'FinCube',
    'MMD Smart',
    'Darwin Tech Labs',
    'Evolution',
    'Очень Интересно',
    'Синхро',
    'Dcloud',
    'Geniusto International',
    'ZenBit',
    'DataGo!',
    'Super Dispatch',
    'ProfUA',
    'MarketPapa',
    'Elinext',
    'МТС Digital',
    'РСХБ Интех',
    'Конфитрейд',
    'Альфа Банк',
    'Positive Technologies',
    'ЗащитаИнфо Транс',
    'Series Eight',
    'Zeektek',
    'Forest Valley',
    'Juni',
    'Geomotiv',
    'Smartbrain',
    'Ингосстрах',
    'ServiceNow',
    'SpurIT',
    'Amazon Dev Center',
    'FundCount',
    'Dayl Group',
    'Antilatency',
    'Maxar Technologies',
    'HeadFinder',
    'PMP TECH',
    'Техно Диасофт',
    'Game Industry',
    'AppMagic',
    'Toimi',
    'Videoseed',
    'TechHive',
    'Profua',
    'NAPA AUTOMOTIVE',
    'Center Pixel',
    'Meraki',
    'NGRS',
    'WifiMap',
    'Leidos',
    'Gallium Studios',
    'Zenbit',
    'Крауд',
    'Neybox Digital',
    'HashEx',
    'Atomichronica',
    'BullPerks',
    'Блокчейн',
    'DZSystems',
    'BSL',
    'Nova Credit',
    'Aha!',
    'Task Agency',
    'Agoda',
    'Waves',
    'Ailet',
    'Artezio',
    'Konomic',
    'КСК эксперт',
    'Bell Integrator',
    'MonetizeMore',
    'СенамаСофт',
    'HelviX GmbH',
    'PurrWeb',
    'Lea Soft',
    'ProShop',
    'Aegis Foundry',
    'ITFB Group',
    'Кредит Европа Банк',
    'Смарт Юнит',
    'Embacy',
    'ORTALEX',
    'Rush Agency',
    'Bellroy',
    'FNTASTIC',
    'Ethplorer.io',
    'Bluethumb',
    'DevHunt',
    'Nitka Technologies',
    'Азбука знаний',
    'Mudflap',
    'Professional Search Group',
    'Gazprom-Media',
    'ORCA.codes',
    'Creative',
    'Centicore',
    'Pixellu',
    'Webinar',
    'Delta Solutions',
    'GrowFood',
    'AtsAero',
    'URSiP',
    'Nexters',
    'СОРСО-СТР',
    'Amazon',
    'CV Recruitment',
    'OTUS',
    'TechReactGroup',
    'CloudX',
    'AppFox',
    'EnjoyPRO',
    'Amarkets',
    'DataArt',
    'Softmedialab',
    'IBS',
    'Star-staff',
    'Gameram',
    'Домклик',
    'Yucca.digital',
    'Advascale',
    'CircleLink Health',
    'Upstairs',
    'Xenna',
    'Winline',
    'Читай-Город — Буквоед',
    'Emerging Travel Group',
    'Taxes For',
    'Aston',
    'Higher Logic',
    'МТС BigData',
    'Access Softek',
    'ColorNew',
    'Limavi',
    'Codex Optimus',
    'CactusSoft',
    'Rho AI',
    'Crypton Studio',
    'Global Career',
    'Novartis',
    'Pivotics',
    'DocsInBox',
    'Fordewind',
    'SimpleSales',
    'Рт Мис',
    'TopSelection',
    'Society of Programmers Agency',
    'UTORG',
    'Тим Кук',
    'Combridge itc',
    'Webbee',
    'Foreshko',
    'Адалиск',
    'Styledna.ai',
    '3KNET',
    'Hyland Software',
    'Mimesis Inc',
    'PlayFlock',
    'TISS',
    'SoftTeco',
    'Lockular',
    'Carle Health',
    'DataArt dataart',
    'Sagitec',
    'Laserfiche',
    'BetBoom',
    'Ester Digital',
    'Синимекс',
    'Garpix',
    'Super Protocol',
    'Тинькофф',
    'Meta',
    'TalkBank',
    'Mission Cloud Services',
    'Mindall',
    'RapDev.io',
    'VSolvit LLC',
    'Интерсвязь',
    'Selecty IT',
    'UtilityAPI',
    'ПартКом',
    'GS Group',
    'Bloomex',
    'Систематика',
    'Mir Plat.Form',
    'GloboGames',
    'Superdao.co',
    'Bracket',
    'Nagarro',
    'Феникс-Групп',
    'Kaller',
    'Сервионика',
    'Элоконт',
    'NewsCatcher',
    'Wisercat',
    'Star-Staff',
    'AssemblyAI',
    'ATTRA',
    'Виэйинтеллидженс',
    'Selecty',
    'Nationwide IT Services',
    'GlobalTruck IT',
    'Like Центр',
    'TORIBIO TECH SRL',
    'Washington Technology Industry Association',
    'Perfomance',
    'Ennabl',
    'Почта банк',
    'Мосгортур',
    'Iron Forge Development',
    'Benefactory',
    'Группа Компаний Черкизово',
    'Center-Game',
    'Devquality',
    'RUSSPASS',
    'ReTech labs',
    'BufferGrou',
    'Greenmesh',
    'Shake',
    'Геном.Эксперт',
    'Mad Devs',
    'Pictureworks Group',
    'SAPRUN',
    'ORIGINS_DIGITAL',
    'KEMBERTON HEALTHCARE SERVICES LLC',
    'Improvado',
    'Medical Licencing',
    'Rebrandium web',
    'GitNation',
    'Click',
    'Wildberries',
    'RiACT',
    'HRlink',
    'ДНК',
    'Transition Technologies',
    'ДОМ.РФ',
    'Next Games',
    'EDSTEIN',
    'Nox',
    'SmartBrain.io',
    'Мирадор',
    'Gcompany',
    'Remoby',
    'Aldo | Austin, TX',
    'Weigandt Consulting',
    'ASH',
    'Aggregion',
    'PITBel Group',
    'TaskAgency',
    'Cetra',
    'Hello, Doc!',
    'Парсек Лаб',
    'Neon EVM',
    'Marketing for Change Co',
    'DynamicSun',
    'ЕМС-М',
    'Citrix',
    'IBA Group',
}

search_companies = "[Cc]ompany{1}[:\-\s]{1,3}[A-ZА-Я][A-ZА-Яa-zа-я0-9]{1,}[^\n][A-ZА-Я]{0,}[а-яa-zА-ЯA-Z0-9]{0,}[^\n][A-ZА-Я]{0,}[а-яa-zА-ЯA-Z0-9]{0,}[^\n][A-ZА-Я]{0,}[а-яa-zА-ЯA-Z]{0,}" \
                   "|[A-Z][A-Za-z]{1,}\W{0,}[A-Z][A-Za-z]{0,}\W{0,4}[A-Za-zА-Яа-я]{0,}\W[A-Za-zА-Яа-я]{0,}[\W]{1,4}компания" \
                   "|[кК]омпани[я][^\n\.!][:\-\s]{0,2}[A-ZА-Я][A-ZА-Яа-я0-9a-z]{1,}[^\n()][A-ZА-Я]{0,}[а-яa-zА-ЯA-Z0-9]{0,}[^\n()][A-ZА-Я]{0,}[а-яa-zА-ЯA-Z0-9]{0,}[^\n()][A-ZА-Я]{0,}[а-яa-zА-ЯA-Z]{0,}" \
                   "|[A-Z][A-Za-z]{1,}[\s\-]{0,}[a-z]{1,}\s{0,}IT company"

english_pattern = "[^\n.,\-\−;:]+английского[^\n.,;:]+|[^\n\-\—;:]+английский[\n.,]|[Аа]нглийский[^\n\.,;]{1,100}|[Аа]нглийский,"

# search_companies2 = "[Cc]ompany[Nname]{0,4}[:]{0,1}[^\n]{1}[A-Z][^\n()\.,а-яА-Я]+|[Кк]омпания[:]{0,1}[^\n]{1}[A-Z][^\n()\.,]+"
search_companies2 = "[Cc]ompany[Nname]{0,4}[:]{0,1}[^\n]{1}[A-Z][^\n()\.,а-яА-Я]+|[Кк]омпания[:]{0,1}[^\n]{1}[“”\"'][А-ЯA-Z][^\n()\.,]+|[Нн]азвание\s{1}компании[^\n\.,;]*|разработчик в [^\n();:]*|[Ккомпания]{7,8}[^\n;\/\\\.,]{1,2}[\"]{1}[A-Za-zА-Яа-я]+[\"]{1}|[\n][^\n]+IT[^\n]компания|IT[^\n]{1,2}компания[^\n]{1,2}[A-Z\s]+"

relocate_pattern = "[^@\/][Rr]elocate[^\n\._\",T()#]*|[Рр]елокация[^\n\"\.r)]*|[Рр]елокационный[^\n;]*|[^\n#a-zA-Z]*[#]{0,1}[Пп]ереезд[а]{0,1}[^\n;]*"

middle_pattern = "[Mm]iddle"

senior_pattern = "[Pp]attern"

vacancy_name = "[^a-zA-ZА-Яа-я][Пп]озиция[^\n]{1,3}[^\n\.;]+|[^#][Вв]акансия[^\n,\.;][^а-яА-Я][^\n,]+|[Дд]олжность[^\n]+|в поиске[^\n][А-ЯA-Z][^\n\.,;]+|[Нн]азвание вакансии[^\n,;]+|[^#\w][VACANCYvacancy]{7}[^\n]+|[^\n.,;!\-]+[Ee]ngineer[^\n.,;]*|[^\n\.,;а-яА-Я#]+[dD]eveloper[^a-z][^\n;а-яА-Я\"]*|[^\n.,;]*[Pp]ro[duje]{2}ct[^\n][Mm]anager[^\n,;\"]+|[^\n.,;]+[Cc]ommunity[^\n][Mm]anager[^\n.,;]+|Программист[а][^\n\.,][CС]#|Position[^\n]+|[Аа]налитик[а] бизнес[^\n]процессов|[^\nа-яА-Я]*Lead[^\n]ML|React разработчик[а]?|[^\nа-яА-Я,]*[Рр]азработчик[а]?[^а-я][^\n\.;\"]*|Middlе Jаvа-рaзрaбoтчик|[a-zA-Z]*[^#\-]QA[^\n\.:;\-\"]|Инженер данных [^\n]+|Machine[\W]Learning[\W]Specialist|[^\nа-яА-Яє]+[Ff]ull[\W][sS]tack[^\nа-яА-Яє]+|[a-zA-Z]+[\W][23][Dd][\W]?[хХ]удожник[а]?|[^\n]+blockchain architect|ищем[^\n\.;]+|[^\n;\.,‼️]+artist[^\n;\.,]+|[MmiddleJjuniorSsenior]{6}[\W][Rr]uby[\W][Dd]eveloper|[a-zA-ZА-Яа-я]+\sтестировщик|Junior QA"

job_format = "[^\n\•]*[Фф]ормат[\W]?[работы]{0,6}[:]?[^\n;]*|[а-я]*\s?[Рр]абота[а-я\s]*в [Оо]фисе[^\n;]*|[^\n\-\—]*[Уу]дал[её][н]{1,2}[каыйоя]{1,2}[^\n;#илп,\.()]{1,8}|[Rr]emote[ly]{0,2}[^\n()\.,;:#а-яА-ЯA-Zfwa\/\"]*|нахождение[\W]{1,2}в[^\n]*"
remote_pattern = "[Уу]дал[её][н]{1,2}[каыйоя]{1,2}[^\n;#илп,\.()]{1,8}|[Rr]emote[ly]{0,2}[^\n()\.,;:#а-яА-ЯA-Zfwa\/\"]*"
#-----------------------------------------
vacancy_pattern = {
    'common_vacancy': "[^a-zA-ZА-Яа-я][Пп]озиция[^\n]{1,3}[^\n\.;]+|[^#][Вв]акансия[^\n,\.;][^а-яА-Я][^\n,]+|[Дд]олжность[^\n]+|в поиске[^\n][А-ЯA-Z][^\n\.,;]+|[Нн]азвание вакансии[^\n,;]+|[^#\w][VACANCYvacancy]{7}[^\n,\.;]+|[Ии]щем[^\n\";.,]+",
    'marketing_vacancy': "[\n][^\n]{0,15}маркетолог|[A-Z]*[a-z]*\s?[A-Z]*[a-z]*\s?[Mm]arketing[\W][Mm]anager",
    'ba_vacancy': "",
    'game_vacancy': "",
    'product_vacancy': "SEO[\W]Specialist[^\n\"\.;]{0,30}|[sS]upport[\W]specialist|[Пп]роектн[ыйого]{2,3}[\W][Мм]енеджер[а]?|[^\nа-яА-Я:\.;,]*[Pp]ro[jedu]{2}ct[\W][Mm]anager[^\n(,\.\"?;]*|[Oo]ffice[\W][mM]anager[^\n\.,;\"]+",
    'mobile_vacancy': "",
    'pm_vacancy': "SEO[\W]Specialist[^\n\"\.;]{0,30}|[sS]upport[\W]specialist|[Пп]роектн[ыйого]{2,3}[\W][Мм]енеджер[а]?|[^\nа-яА-Я:\.;,]*[Pp]ro[jedu]{2}ct[\W][Mm]anager[^\n(,\.\"?;]*|[Oo]ffice[\W][mM]anager[^\n\.,;\"]+",
    'sales_manager_vacancy': "",
    'analyst_vacancy': "",
    'designer_vacancy': "[аАРТрт]{3}-[Дд]иректор[а]?[^ом]|2D[\W]дизайнер[^\n,\.;]*|[^\nа-яА-Я]*[UXUI\/]{2,5}[\W][Dd]esigner[^\n\.,;\"]+|[^\n@:(]+[Dd]esigner[^\n\.,;\"]*|[^\nа-яА-Я]*[UXUI\/\|]{2,5}[\W][Дд]изайнер[^\n)\.,;]*|дизайнеров[\s\-\-]{1,3}[A-Za-z\+\/]+|^[Дд]изайнер$|[^\nа-яА-Я]+2D[\W][Хх]удожник|[^\nа-яА-Я\-]*[Aa]rtist[\W][^\n\"]*|[SMMsmmwebWEB]{3}[\W]?дизайнер",
    'devops_vacancy': "[^\n\"]*CTO[^\n\.,;\"]*|[^\n\"]*technical[\W]officer[^\n\"]*",
    'hr_vacancy': "",
    # 'backend_vacancy': "[Cc]\+\+[\W]?(программист|разработчик)|[^\n.,;!\-]+[Ee]ngineer[^\n.,;]*|[^\n\.,;а-яА-Я#]+[dD]eveloper[^a-z][^\n;а-яА-Я\"]*|[^\n.,;]*[Pp]ro[duje]{2}ct[^\n][Mm]anager[^\n,;\"]+|[^\n.,;]+[Cc]ommunity[^\n][Mm]anager[^\n.,;]+|Программист[а][^\n\.,][CС]#|Position[^\n]+|[Аа]налитик[а] бизнес[^\n]процессов|[^\nа-яА-Я]*Lead[^\n]ML|React разработчик[а]?|[^\nа-яА-Я,]*[Рр]азработчик[а]?[^\n\.;\"]*|Middlе Jаvа-рaзрaбoтчик|[a-zA-Z]*[^#\-]QA[^\n\.:;\-\"]|Инженер данных [^\n]+|Machine[\W]Learning[\W]Specialist|[^\nа-яА-Яє]+[Ff]ull[\W][sS]tack[^\nа-яА-Яє]+|[a-zA-Z]+[\W][23][Dd][\W]?[хХ]удожник[а]?|[^\n]+blockchain architect|ищем[^\n\.;]+|[^\n;\.,‼️]+artist[^\n;\.,]+|[MmiddleJjuniorSsenior]{6}[\W][Rr]uby[\W][Dd]eveloper|[a-zA-ZА-Яа-я]+\sтестировщик|Junior QA|[Bb]ig[\W][Dd]ata[\W][Ee]ngineer|[a-zA-Z]{2,10}.js[^\n]{1,15}([Dd]eveloper|[Рр]азработчик)",
    'frontend_vacancy': "[^\n.,;!\-а-я]+[Ee]ngineer[^\n.,;а-я]*|[^\n\.,;а-яА-Я#]+[dD]eveloper[^a-z][^\n;а-яА-Я\"]*|[^\n.,;]*[Pp]ro[duje]{2}ct[^\n][Mm]anager[^\n,;\"]+|[^\n.,;]+[Cc]ommunity[^\n][Mm]anager[^\n.,;]+|Программист[а][^\n\.,][CС]#|Position[^\n]+|[Аа]налитик[а] бизнес[^\n]процессов|[^\nа-яА-Я]*Lead[^\n]ML|React разработчик[а]?|[^\nа-яА-Я,]*[Рр]азработчик[а]?[^а-я][^\n\.;\"]*|Middlе Jаvа-рaзрaбoтчик|[a-zA-Z]*[^#\-]QA[^\n\.:;\-\"]|Инженер данных [^\n]+|Machine[\W]Learning[\W]Specialist|[^\nа-яА-Яє]+[Ff]ull[\W][sS]tack[^\nа-яА-Яє]+|[a-zA-Z]+[\W][23][Dd][\W]?[хХ]удожник[а]?|[^\n]+blockchain architect|ищем[^\n\.;]+|[^\n;\.,‼️]+artist[^\n;\.,]+|[MmiddleJjuniorSsenior]{6}[\W][Rr]uby[\W][Dd]eveloper|[a-zA-ZА-Яа-я]+\sтестировщик|Junior QA|[Bb]ig[\W][Dd]ata[\W][Ee]ngineer",
    'backend_vacancy': "[Cc]\+\+[\W]?(программист|разработчик)|[^\n.,;!\-]+[Ee]ngineer[^\n.,;]*|[^\n\.,;а-яА-Я#]+[dD]eveloper[^a-z][^\n;а-яА-Я\"]*|[^\n.,;]*[Pp]ro[duje]{2}ct[^\n][Mm]anager[^\n,;\"]+|[^\n.,;]+[Cc]ommunity[^\n][Mm]anager[^\n.,;]+|Программист[а][^\n\.,][CС]#|Position[^\n]+|[Аа]налитик[а] бизнес[^\n]процессов|[^\nа-яА-Я]*Lead[^\n]ML|React разработчик[а]?|[^\nа-яА-Я,]*[Рр]азработчик[а]?[^\n\.;\"]*|Middlе Jаvа-рaзрaбoтчик|[a-zA-Z]*[^#\-]QA[^\n\.:;\-\"]|Инженер данных [^\n]+|Machine[\W]Learning[\W]Specialist|[^\nа-яА-Яє]+[Ff]ull[\W][sS]tack[^\nа-яА-Яє]+|[a-zA-Z]+[\W][23][Dd][\W]?[хХ]удожник[а]?|[^\n]+blockchain architect|[^\n;\.,‼️]+artist[^\n;\.,]+|[MmiddleJjuniorSsenior]{6}[\W][Rr]uby[\W][Dd]eveloper|[a-zA-ZА-Яа-я]+\sтестировщик|Junior QA|[Bb]ig[\W][Dd]ata[\W][Ee]ngineer|[a-zA-Z]{2,10}.js[^\n]{1,15}[Dd]eveloper|[a-zA-Z]{2,10}.js[^\n]{1,15}[Рр]азработчик|Scala[^\n]{1,15}[Ll]ead",
    'qa_vacancy': "[^\n.,;!\-]+[Ee]ngineer[^\n.,;]*|[^\n\.,;а-яА-Я#]+[dD]eveloper[^a-z][^\n;а-яА-Я\"]*|[^\n.,;]*[Pp]ro[duje]{2}ct[^\n][Mm]anager[^\n,;\"]+|[^\n.,;]+[Cc]ommunity[^\n][Mm]anager[^\n.,;]+|Программист[а][^\n\.,][CС]#|Position[^\n]+|[Аа]налитик[а] бизнес[^\n]процессов|[^\nа-яА-Я]*Lead[^\n]ML|React разработчик[а]?|[^\nа-яА-Я,]*[Рр]азработчик[а]?[^а-я][^\n\.;\"]*|Middlе Jаvа-рaзрaбoтчик|[a-zA-Z]*[^#\-]QA[^\n\.:;\-\"]|Инженер данных [^\n]+|Machine[\W]Learning[\W]Specialist|[^\nа-яА-Яє]+[Ff]ull[\W][sS]tack[^\nа-яА-Яє]+|[a-zA-Z]+[\W][23][Dd][\W]?[хХ]удожник[а]?|[^\n]+blockchain architect|ищем[^\n\.;]+|[^\n;\.,‼️]+artist[^\n;\.,]+|[MmiddleJjuniorSsenior]{6}[\W][Rr]uby[\W][Dd]eveloper|[a-zA-ZА-Яа-я]+\sтестировщик|Junior QA|[Bb]ig[\W][Dd]ata[\W][Ee]ngineer",
    'junior_vacancy': "",
    'middle_vacancy': "",
    'senior_vacancy': "",
    'fullstack_vacancy': "",
    'developer_qa_vacancy': "[^\n.,;!\-]+[Ee]ngineer[^\n.,;]*|[^\n\.,;а-яА-Я#]+[dD]eveloper[^a-z][^\n;а-яА-Я\"]*|[^\n.,;]*[Pp]ro[duje]{2}ct[^\n][Mm]anager[^\n,;\"]+|[^\n.,;]+[Cc]ommunity[^\n][Mm]anager[^\n.,;]+|Программист[а][^\n\.,][CС]#|Position[^\n]+|[Аа]налитик[а] бизнес[^\n]процессов|[^\nа-яА-Я]*Lead[^\n]ML|React разработчик[а]?|[^\nа-яА-Я,]*[Рр]азработчик[а]?[^а-я][^\n\.;\"]*|Middlе Jаvа-рaзрaбoтчик|[a-zA-Z]*[^#\-]QA[^\n\.:;\-\"]|Инженер данных [^\n]+|Machine[\W]Learning[\W]Specialist|[^\nа-яА-Яє]+[Ff]ull[\W][sS]tack[^\nа-яА-Яє]+|[a-zA-Z]+[\W][23][Dd][\W]?[хХ]удожник[а]?|[^\n]+blockchain architect|ищем[^\n\.;]+|[^\n;\.,‼️]+artist[^\n;\.,]+|[MmiddleJjuniorSsenior]{6}[\W][Rr]uby[\W][Dd]eveloper|[a-zA-ZА-Яа-я]+\sтестировщик|Junior QA|[Bb]ig[\W][Dd]ata[\W][Ee]ngineer",
}
valid_profession_list = ['marketing', 'ba', 'game', 'product', 'mobile',
                                      'pm', 'sales_manager', 'analyst', 'frontend',
                                      'designer', 'devops', 'hr', 'backend', 'qa', 'junior']
