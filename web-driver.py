import logging
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import bs4


#後で設定化
TARGET_URL = 'https://www.happyon.jp/index.html'
CHROME_DRIVER = 'C:/devs/chromedriver_win32/chromedriver'
LOG_HOME = 'C:/0_work/python/web-scraping/log'
SCREENSHOT_PATH = 'C:/0_work/python/web-scraping/dump/screenshot'
INIT_WINDOW_H = 500
INIT_WINDOW_W = 1000


##Init##
dt = datetime.datetime.now()
today = str(dt.year) + '-' + str(dt.month) + '-' + str(dt.day)

logging.basicConfig(
        level = logging.DEBUG
        , format = '%(asctime)s - %(levelname)s - %(message)s'
        , filename = LOG_HOME + '/log-' + today + '.log'
    )

##Init終わり##
logging.info('START: web-scraping')

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(
    executable_path = CHROME_DRIVER
    ,service_log_path = LOG_HOME + '/driver-log-' + today + '.log'
    ,chrome_options = options
    )
driver.set_window_size(INIT_WINDOW_W, INIT_WINDOW_H )
driver.get(TARGET_URL)

dh = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(INIT_WINDOW_W, dh )
time.sleep(20)

driver.save_screenshot(SCREENSHOT_PATH + '/shot-' + str(round(time.time())) + '.png')

#logging.debug(
#    driver.page_source
#    )

soup = bs4.BeautifulSoup( driver.page_source, "lxml" )
elems = soup.select("section img")

logging.debug(
    "\n elements count : " + str(len(elems))
    )

for i in range(len(elems)) :
    print(str(elems[i]))

driver.quit()

logging.info('END: web-scraping')
