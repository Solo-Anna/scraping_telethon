from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService

options = Options()
# options.headless = True
# options.add_argument('window-size=1920x935')
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# browser = webdriver.Firefox(
#     executable_path=r'./settings_/firefox_driver/geckodriver.exe',
#     options=options
# )

# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
chrome_driver_path = ''
