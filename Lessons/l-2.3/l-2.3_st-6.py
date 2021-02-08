from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element_by_css_selector("button.btn").click()

    browser.switch_to.window(browser.window_handles[1])

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(browser.find_element_by_id("input_value").text))

    print(browser.window_handles)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
