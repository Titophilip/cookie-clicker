import time

from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

now = time.time()
five_minutes = now + 300

cookie = driver.find_element_by_id("cookie")

while time.time() <= five_minutes:
    five_seconds = time.time() + 5
    while time.time() <= five_seconds:
        cookie.click()
    cursors = driver.find_elements_by_css_selector("#store b")

    for cursor in cursors[::-1]:
        try:
            cursor.click()
        except:
            pass

print(driver.find_element_by_id("cps").text)

driver.quit()
