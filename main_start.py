import os
import time
from invite_bot_ver2 import run as run_parser_bot
from _apps.talking_bot.mvp_connect_talking_bot import talking_bot_run
from _apps.endpoints import endpoints
from multiprocessing import Process, Pool
import settings.os_getenv as settings
# ev = Event()

num_processes = os.cpu_count()

def start_bot(double=False, token_in=None):
    # time.sleep(3)
    print('1')
    run_parser_bot(
        double=double,
        token_in=token_in
    )
    print('bot has been stopped')

def start_endpoints():
    print('2')
    endpoints.run_endpoints()

if __name__ == "__main__":

    p1 = Process(target=start_endpoints, args=())
    p2 = Process(target=start_bot, args=())
    p3 = Process(target=start_bot, args=(True, settings.token_red))
    p4 = Process(target=talking_bot_run, args=())

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # p1.join()
    # p2.join()
    # p3.join()


