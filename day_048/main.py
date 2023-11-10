import time
from selenium import webdriver
from selenium.webdriver.common.by import By

####################### Initialize driver #######################

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://orteil.dashnet.org/cookieclicker/")

####################### Initialize website #######################

driver.implicitly_wait(5)
driver.find_element(By.ID, "langSelect-EN").click()
time.sleep(5)
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "cc_btn").click()

####################### Play game #######################

while True:
    timer = time.time() + 1

    ####################### Click for 5 seconds #######################

    while time.time() < timer:
        driver.find_element(By.ID, "bigCookie").click()

    cookies = driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", "")

    if float(cookies) < 100:
        i = 3
    else: 
        i = 4

    while i > 0:
        price = driver.find_element(By.ID, f"productPrice{i-1}").text.replace(",", "")

        if float(cookies) > float(price):
            driver.find_element(By.ID, f"product{i-1}").click()

        i -= 1
    