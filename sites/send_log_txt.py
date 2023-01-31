from utils.additional_variables.additional_variables import path_log_check_profession

async def send_log_txt(text, write_mode='a'):
    with open(path_log_check_profession, write_mode, encoding='utf-8') as file:
        file.write(f'{text}\n\n')
