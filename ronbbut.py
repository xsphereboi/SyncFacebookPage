from selenium import webdriver
import time
import json
import os
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.chrome.options import Options
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import configparser
from facebook_scraper import get_posts

#Reading Config Files################
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config = configparser.ConfigParser()
config.read(os.path.join(path, 'settings.conf'))
options = Options()
op_page_url = config['settings']['opponent_page_id']
page_url = config['settings']['your_page_url']
user = config['settings']['email']
passw = config['settings']['pass']
image = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
img = (os.path.join(path, 'img.png').replace('\\','/'))
#######################################

print(img)
options.add_argument('--log-level=3')

def onlytext(text):
    try:
        JS_ADD_TEXT_TO_INPUT = """
        var elm = arguments[0], txt = arguments[1];
        elm.value += txt;
        elm.dispatchEvent(new Event('change'));
        """
        #JS_ADD_TEXT_TO_INPUT is required if you want to add emojies
        browser = webdriver.Chrome(options=options)
        browser.get("https://mbasic.facebook.com/")
        browser.find_element_by_name('email').send_keys(user)
        browser.find_element_by_name('pass').send_keys(passw)
        browser.find_element_by_name('login').click()
        time.sleep(1)
        browser.get(page_url)
        post_box = browser.find_element_by_name('xc_message')
        browser.execute_script(JS_ADD_TEXT_TO_INPUT, post_box, text)
        browser.find_element_by_name('view_post').click()
        browser.close()
        data = {"error":"false"}
        return json.dumps(data)
    except Exception as e:
        print('Eggh Error Happened , Login Details Might Bad , Turn Headless = False to see whats going on')
        browser.close()
        data = {"error":"true"}
        return json.dumps(data)


def photowithcaption(text):
    try:
        JS_ADD_TEXT_TO_INPUT = """
        var elm = arguments[0], txt = arguments[1];
        elm.value += txt;
        elm.dispatchEvent(new Event('change'));
        """
        browser = webdriver.Chrome(options=options)
        browser.get("https://mbasic.facebook.com/")
        browser.find_element_by_name('email').send_keys(user)
        browser.find_element_by_name('pass').send_keys(passw)
        browser.find_element_by_name('login').click()
        time.sleep(1)
        browser.get(page_url)
        browser.find_element_by_xpath(""".//*[@id="mbasic-composer-form"]/div/span/div[1]/table/tbody/tr/td[2]/input""").click()
        browser.find_element_by_xpath(""".//*[@id="root"]/table/tbody/tr/td/form/div[1]/div/input[1]""").send_keys(r"C:\Users\Xsphere\Desktop\GUI\ronb but arthur gun sucks\img.png")
        browser.find_element_by_name('add_photo_done').click()
        post_box = browser.find_element_by_name('xc_message')
        browser.execute_script(JS_ADD_TEXT_TO_INPUT, post_box, text)
        browser.find_element_by_name('view_post').click()
        browser.close()
        data = {"error":"false"}
        return json.dumps(data)
    except Exception:
        browser.close()
        print('Eggh Error Happened , Login Details Might Bad , Turn Headless = False to see whats going on')
        data = {"error":"true"}
        return json.dumps(data)


def latest():
    latest = []
    for post in get_posts(op_page_url,pages=1):
        latest.append(post)
    return latest[0]
