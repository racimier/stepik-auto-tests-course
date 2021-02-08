from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("{}".format(num1 + num2))  # ищем элемент с текстом суммы

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
