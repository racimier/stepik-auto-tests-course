import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    input1 = browser.find_element_by_id("answer")
    y = calc(x)
    input1.send_keys(y)

    check_b = browser.find_element_by_id("robotCheckbox")
    check_b.click()

    radio_b = browser.find_element_by_id("robotsRule")
    radio_b.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
