import logging, datetime, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

CONF = json.loads(open('./conf/setting.json').read())

#設定化
LOG_HOME = CONF['log_home']
CHROME_DRIVER = CONF['chrome_driver_path']
CHROME_WINDOW_HEIGHT = CONF['chrome_window_height']
CHROME_WINDOW_WIDTH = CONF['chrome_window_width']
TRGET_LIST = CONF['TARGET']
SCREENSHOT_PATH = CONF['screenshot_dump_path']
DIST_PATH = CONF['dist_path']

##Init##
dt = datetime.datetime.now()
today = str(dt.year) + '-' + str(dt.month) + '-' + str(dt.day)

logging.basicConfig(
        level = logging.INFO
        , format = '%(asctime)s - %(levelname)s - %(message)s'
        , filename = LOG_HOME + '/log-' + today + '.log'
    )

##Init終わり##
logging.info('START: web-scraping')
logging.info('START: webdriver initialize')

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(
    executable_path = CHROME_DRIVER
    ,service_log_path = LOG_HOME + '/driver-log-' + today + '.log'
    ,chrome_options = options
    )
driver.set_window_size(CHROME_WINDOW_WIDTH, CHROME_WINDOW_HEIGHT )
logging.info('END: webdriver initialize')

logging.info('START: scraping to target list')
for i in range(len(TRGET_LIST)) :
    logging.info('START: scraping to target ' + str(i))
    TARGET = TRGET_LIST[i]
    DIST = {}
    DIST['name'] = TARGET['page_name']
    
    driver.get(TARGET['page_url'])
    dh = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(CHROME_WINDOW_WIDTH, dh )
    
    time.sleep(TARGET['sleep_time'])
    driver.save_screenshot(SCREENSHOT_PATH + '/shot-' + str(round(time.time())) + '.png')

    content_list = driver.find_elements_by_xpath(TARGET['list_path'])
    logging.debug(
            "\n contents_list : " + str(len(content_list))
            + "\n selector : " + TARGET['list_path']
        )
    
    DIST['contents_list'] = []
    for j in range(len(content_list)) :
        try :
            #リストタイトルの取得
            list_title = content_list[j].find_element_by_xpath(TARGET['list_title_path'])
            logging.debug(
                "\n list_title : " + str(list_title.get_attribute('text'))
                )
            DIST['contents_list'].append( {
                    'list_title' : str(list_title.get_attribute('text')),
                    'contents' : []
                })

            #イメージコンテンツのリストを取得
            contents = content_list[j].find_elements_by_xpath(TARGET['contents_path'])
            logging.debug(
                    "\n contents_list : " + str(len(contents))
                    + "\n selector : " + TARGET['contents_path']
                )

            for k in range(len(contents)) :
                try :
                    #イメージのタイトルを取得
                    content_title = contents[k].find_element_by_xpath(TARGET['content_title_path'])
                    title = content_title.get_property('dataset')
                    logging.debug(
                        "\n content_title : " + str(title)
                        )
                    #イメージの説明を取得
                    content_description = contents[k].find_element_by_xpath(TARGET['content_description_path'])
                    description = content_description.get_property('textContent')
                    #変な文字対策
                    description = description.encode('cp932', "ignore").decode('cp932')
                    logging.debug(
                        "\n content_title : " + str(description)
                        )
                    #イメージのソースを取得
                    content_image = contents[k].find_element_by_xpath(TARGET['content_image_path'])
                    image = content_image.get_attribute('src')
                    logging.debug(
                        "\n content_image : " + str(image)
                        )

                    DIST['contents_list'][j]['contents'].append({
                            'content_title' : title,
                            'content_description' : description,
                            'content_image' : image
                        })

                    
                except Exception as err:
                    logging.error("コンテンツの取得にあたりエラーが発生しました")
        except Exception as err :
            logging.error("リストの取得にあたりエラーが発生しました")
        

    #post処理
    driver.quit()

    file = open(
        DIST_PATH + '/' + DIST['name'] + '-' + str(round(time.time())) + '.json'
        , 'w'
        )
    try : 
        json.dump(
            DIST
            , file
            , ensure_ascii=False
            , indent=4
            , sort_keys=False
            , separators=(',', ': ')
            )
    except Exception as err:
        logging.error(err)
    file.close()
    

    logging.info('END: scraping to target ' + str(i))


logging.info('END: scraping to target list')


logging.info('END: web-scraping')
