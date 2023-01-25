
import configparser
from logs.logs import Logs
from sites.scraping_dev import DevGetInformation
from sites.scraping_geekjob import GeekGetInformation
from sites.scraping_habr import HabrGetInformation
from sites.scraping_hh import HHGetInformation
from sites.scraping_rabota import RabotaGetInformation
from sites.scraping_superjob import SuperJobGetInformation
from sites.scraping_svyazi import SvyaziGetInformation
from sites.scrapping_finder import FinderGetInformation
from multiprocessing import Process, Lock
import asyncio

logs = Logs()

config = configparser.ConfigParser()
config.read("./settings_/config.ini")

class ParseSites:

    def __init__(self, client, bot_dict):
        self.client = client
        self.current_session = ''
        self.bot = bot_dict['bot']
        self.chat_id = bot_dict['chat_id']


    async def call_sites(self):

        logs.write_log(f"scraping_telethon2: function: call_sites")

        bot_dict = {'bot': self.bot, 'chat_id': self.chat_id}
        
        # await DevGetInformation(bot_dict).get_content()
        # await SuperJobGetInformation(bot_dict).get_content()
        # await RabotaGetInformation(bot_dict).get_content()
        # await HabrGetInformation(bot_dict).get_content()
        # await FinderGetInformation(bot_dict).get_content()
        # await GeekGetInformation(bot_dict).get_content()
        # await SvyaziGetInformation(bot_dict).get_content()
        # await HHGetInformation(bot_dict).get_content()

        task1 = asyncio.create_task(DevGetInformation(bot_dict).get_content())
        task2 = asyncio.create_task(SuperJobGetInformation(bot_dict).get_content())
        task3 = asyncio.create_task(RabotaGetInformation(bot_dict).get_content())
        task4 = asyncio.create_task(HabrGetInformation(bot_dict).get_content())
        task5 = asyncio.create_task(FinderGetInformation(bot_dict).get_content())
        task6 = asyncio.create_task(GeekGetInformation(bot_dict).get_content())
        task7 = asyncio.create_task(SvyaziGetInformation(bot_dict).get_content())
        task8 = asyncio.create_task(HHGetInformation(bot_dict).get_content())
        await asyncio.gather(task1, task2, task3, task4, task5, task6, task7, task8)

        # p1 = Process(target=asyncio.run(DevGetInformation(bot_dict).get_content), args=())
        # p2 = Process(target=SuperJobGetInformation(bot_dict).get_content, args=())
        # p3 = Process(target=RabotaGetInformation(bot_dict).get_content, args=())
        # p4 = Process(target=HabrGetInformation(bot_dict).get_content, args=())
        # p5 = Process(target=FinderGetInformation(bot_dict).get_content, args=())
        # p6 = Process(target=GeekGetInformation(bot_dict).get_content, args=())
        # p7 = Process(target=SvyaziGetInformation(bot_dict).get_content, args=())
        # p8 = Process(target=HHGetInformation(bot_dict).get_content, args=())
        #
        # p1.start()
        # p2.start()
        # p3.start()
        # p4.start()
        # p5.start()
        # p6.start()
        # p7.start()
        # p8.start()
        #
        p1.join()
        # p2.join()
        # p3.join()
        # p4.join()
        # p5.join()
        # p6.join()
        # p7.join()
        # p8.join()

        print(' -----------------------FINAL -------------------------------')

