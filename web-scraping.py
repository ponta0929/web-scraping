import logging
import requests

#後で設定化
TARGET_URL = 'https://www.happyon.jp/index.html'

logging.basicConfig(
        level = logging.DEBUG
        , format = '%(asctime)s - %(levelname)s - %(message)s'
    )
logging.debug('start web-scraping')

logging.debug('do get URL index page')
logging.debug(TARGET_URL)

try:
    res = requests.get(TARGET_URL)
    #エラーチェック
    res.raise_for_status()
    
    logging.debug('success get URL index page')
    logging.debug(
        '\n responseType : ' + str(type(res))
        + '\n text length : ' + str(len(res.text))
        )
except Exception as exc:
    raise Exception('URLからページのロードに失敗しました : {}'.format(exc))
    


logging.debug('end web-scraping')
