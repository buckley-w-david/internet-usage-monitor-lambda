from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from usage_monitor.config import UsageConfig
from usage_monitor.scan import scan as usage_scan

def scan(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver', chrome_options=options)

    config = UsageConfig.from_env(driver=driver)

    usage_scan(config)

    driver.close();
    driver.quit();
