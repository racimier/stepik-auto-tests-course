import os
from selenium import webdriver
import time
# import math


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/file_input.html")

    open('file.txt', 'w')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    # element.send_keys(file_path)

    browser.find_element_by_name('firstname').send_keys('uasya')
    browser.find_element_by_name('lastname').send_keys('123')
    browser.find_element_by_name('email').send_keys('uasya@123.org')

    browser.find_element_by_name('file').send_keys(file_path)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
