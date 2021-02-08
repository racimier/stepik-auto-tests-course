from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://SunInJuly.github.io/execute_script.html')

try:
    x = browser.find_element_by_id("input_value").text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    check_b = browser.find_element_by_id("robotCheckbox")
    check_b.click()

    radio_b = browser.find_element_by_id("robotsRule")
    radio_b.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
