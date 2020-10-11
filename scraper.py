#scraper
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#creates a headless instance of chrome, connects to five thirty eight and pages down twice to reach the forecast data,
#which is then inspected by element id
def scrape():

    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options, executable_path='C:\chromedriver_win32\chromedriver.exe')

    browser.get("https://projects.fivethirtyeight.com/2020-election-forecast/")

    page_down = browser.find_element_by_tag_name('html')
    page_down.send_keys(Keys.PAGE_DOWN)
    page_down.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    #inspects element id and stores text
    element = browser.find_element_by_id('desc-topline-chart').text
    #finds the digits from the string
    digits = find_digits(element)
    return(digits)


#pulls the digits out of the sentence, but won't work if Trump goes to single digits.
def find_digits(string_name):
    list = [string_name[11] + string_name[12], string_name[32] + string_name[33]]

    return list



