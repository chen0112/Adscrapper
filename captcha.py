import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from solveRecaptcha import solverecaptcha

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://www.google.com/recaptcha/api2/demo')


result = solverecaptcha('6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-', 'https://www.google.com/recaptcha/api2/demo')

code = result['code']

print(result)

WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.ID, 'g-recaptcha-response'))
)

browser.execute_script(
    "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'"
)

time.sleep(120)

browser.find_element(By.ID, "recaptcha-demo-submit").click()