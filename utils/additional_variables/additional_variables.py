# for add in vacancy search in db tables
import pandas

admin_database = 'admin_last_session'
archive_database = 'archive'
admin_table_fields = "id, chat_name, title, body, profession, vacancy, vacancy_url, company, english, relocation, " \
                             "job_type, city, salary, experience, contacts, time_of_public, created_at, agregator_link, " \
                             "session, sended_to_agregator, sub"
fields_admin_temporary = "id_admin_channel, id_admin_last_session_table, sended_to_agregator"

additional_elements = {'admin_last_session', 'archive'}

valid_professions = ['designer', 'game', 'product', 'mobile', 'pm', 'sales_manager', 'analyst', 'frontend',
                     'marketing', 'devops', 'hr', 'backend', 'qa', 'junior']
valid_professions_extended = []
valid_professions_extended.extend(valid_professions)
valid_professions_extended.extend(['fullstack'])
tables_for_search_vacancy_existing = [admin_database, 'archive']
all_tables_for_vacancy_search = valid_professions_extended.extend(tables_for_search_vacancy_existing)

not_lower_professions = ['pm', 'game', 'designer', 'hr', 'analyst', 'qa', 'ba' 'devops', 'product']

white_admin_list = [1763672666, 556128576, 758905227, 945718420, 5755261667, 5884559465]

id_owner = 1763672666

#admin database name
channel_id_for_shorts = -1001671844820

# message_for_send = f'<i>Функционал дайджеста находится в состоянии альфа-тестирования, приносим свои ' \
#                                    f'извинения, мы работаем над тем чтобы вы получали информацию максимально ' \
#                                    f'качественную и в сжатые сроки</i>\n\n'

dict_for_title_shorts = {
    '': 'Системных аналитиков',
}

flood_control_logs_path = "./excel/flood_control.txt"
pattern_path = "./excel/pattern.txt"
admin_check_file_path = './logs/check_file.txt'
sites_search_words = ['designer', 'ui', 'junior', 'без опыта', 'стажер', 'product manager', 'project manager', 'python', 'php']

table_list_for_checking_message_in_db = ['admin_last_session', 'archive']

pre_message_for_shorts = '<i>Функционал дайджеста находится в состоянии альфа-тестирования, приносим свои ' \
                                   f'извинения, мы работаем над тем чтобы вы получали информацию максимально ' \
                                   f'качественную и в сжатые сроки</i>\n\n'

message_not_access = "Sorry, you have not the permissions"
path_last_pattern = "./patterns/last_changes/pattern_Alex2809 (6).py"
path_data_pattern = "./patterns/data_pattern/_data_pattern.py"

path_filter_error_file = "./excel/filter_jan_errors.txt"


cities_file_path = './utils/additional_data/data.xlsx'
# cities_file_path = './../utils/additional_data/data.xlsx' # for tests


excel_data_df = pandas.read_excel(f'{cities_file_path}', sheet_name='Cities')
excel_dict = {
    'city': excel_data_df['city'].tolist(),
    'country': excel_data_df['country'].tolist(),
}
result_excel_dict = {}
for i in range(0, len(excel_dict['city'])):
    if excel_dict['country'][i] in result_excel_dict:
        result_excel_dict[excel_dict['country'][i]].append(excel_dict['city'][i])
    else:
        result_excel_dict[excel_dict['country'][i]] = [excel_dict['city'][i]]

clear_vacancy_trash_pattern = "[Ии]щем в команду[:]?|[Тт]ребуется[:]?|[Ии]щем[:]?|[Вв]акансия[:]?|[Пп]озиция[:]?|" \
                              "[Дд]олжность[:]|в поиске[:]|[Нн]азвание вакансии[:]|[VACANCYvacancy]{7}[:]?|[Pp]osition[:]?"

how_much_pages = 7

