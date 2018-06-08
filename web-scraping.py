import logging
import requests
import bs4
import datetime

#Init
dt = datetime.datetime.now()
today = str(dt.year) + '-' + str(dt.month) + '-' + str(dt.day)

#後で設定化
TARGET_URL = 'https://www.happyon.jp/index.html'
LOG_HOME = 'C:/0_work/python/web-scraping/log'

logging.basicConfig(
        level = logging.DEBUG
        , format = '%(asctime)s - %(levelname)s - %(message)s'
        , filename = LOG_HOME + '/log-' + today + '.log'
    )
logging.info('START: web-scraping')

logging.info('DO: get TARGET_URL')
logging.debug(TARGET_URL)

try:
    res = requests.get(TARGET_URL)
    #エラーチェック
    res.raise_for_status()
    
    logging.debug(
        '\n responseType : ' + str(type(res))
        + '\n text length : ' + str(len(res.text))
        )
    logging.info('SUCCESS: get TARGET_URL')
except Exception as exc:
    raise Exception('ERROR: \n URLからページのロードに失敗しました : {}'.format(exc))
    
logging.info('DO: analyze TARGET_URL')

try:
    soup = bs4.BeautifulSoup(res.text)

    logging.debug(
        '\n responseType : ' + str(type(soup))
        )
    logging.info('SUCCESS: analyze TARGET_URL')
    
except Exception as exc:
    raise Exception('ERROR: \n ページの解析に失敗しました')

logging.info('END: web-scraping')
