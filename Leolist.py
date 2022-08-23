import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

with open("data.json", "w") as f:
    json.dump([], f)


def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


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
            print(e, "side error")
            isNextDisabled = True

try:
    with open('all_list', 'r') as f:
        for line in f:
            browser.get(line)

            try:
                elem_list = browser.find_element(By.CSS_SELECTOR, "div.dir-side")

                item = elem_list.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[2]/section[4]')

            except:
                print("this profile doesn't exist :" + line)
                continue

            number = "Number Not Found"

            email = "Email Not Found"

            # Some name will come with emojis
            name = "Name Not Found"

            main_text = browser.find_element(By.CSS_SELECTOR, "div.dir-main-text")

            try:
                # l = len(main_text.find_elements(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/h1'))
                # print(l)
                name = main_text.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/h1').get_attribute(
                    "textContent")
            except:
                pass

            try:
                number = item.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div[3]/div/div/div[2]/section[4]/div[1]/a/strong').get_attribute(
                    "textContent")
            except:
                pass

            try:
                email = item.find_element(By.XPATH,
                                          '/html/body/div[1]/div/div[3]/div/div/div[2]/section[4]/div[2]/a/strong').get_attribute(
                    "textContent")
            except:
                pass

            write_json({
                "Email": email,
                "Tel": number,
                "Name": name

            })


except Exception as e:
    print(e, "main error")
