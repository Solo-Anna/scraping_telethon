from datetime import datetime


class Logs:

    def write_log(self, text):
        pass
        operation_time = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        # with open(f'./logs/logs.txt', 'a') as f:
        #     f.write(f'{operation_time} | {text}\n')