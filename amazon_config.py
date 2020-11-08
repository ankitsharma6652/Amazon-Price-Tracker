from selenium import webdriver
DIRECTORY='reports'
NAME='led tv'
CURRENCY='₹'
MAX_PRICE='50000'
MIN_PRICE='5000'
FILTERS={
    'max':MAX_PRICE,
    'min':MIN_PRICE
}
BASE_URL='https://www.amazon.in/'

def get_chrome_web_driver(options):
    return webdriver.Chrome(r'C:\All Drivers\chromedriver',chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate_errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def set_automation_as_head_less(options):
    options.add_argument('--headless')
    