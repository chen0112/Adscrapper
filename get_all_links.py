from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("https://www.leolist.cc/directory/metro-vancouver")

isNextDisabled = False

with open("all_list", "w") as f:
    while not isNextDisabled:
        try:

            elem_list = browser.find_element(By.XPATH, '//*[@id="dir-list"]')

            items = elem_list.find_elements(By.CLASS_NAME, 'item')

            links = []
            for item in items:
                link = item.get_attribute('href')
                links.append(link)
                f.write(link)
                f.write('\n')

            next_btn = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ml')))

            next_class = next_btn.get_attribute('class')

            if 'disabled' in next_class:
                isNextDisabled = True

            else:
                next_page = browser.find_element(By.CLASS_NAME, 'ml').get_attribute(
                    'href')
                browser.get(next_page)

            print(links)
            print(next_page)

        except Exception as e:
            print(e, "main error")
            isNextDisabled = True
