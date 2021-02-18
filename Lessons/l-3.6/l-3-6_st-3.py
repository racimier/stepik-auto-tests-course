import math
import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\n==>start browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..==>")
    browser.quit()


@pytest.mark.parametrize('page', ['895', '896', '897', '898', '899', '903', '904', '905'])
def test_guest_should_see_login_link(browser, page):
    # browser = webdriver.Chrome()
    link = f"https://stepik.org/lesson/236{page}/step/1"
    browser.get(link)
    browser.find_element_by_css_selector('.textarea.string-quiz__textarea.ember-text-area.ember-view')\
        .send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector(".submit-submission").click()
    time.sleep(3)
    assert "Correct!" == browser.find_element_by_css_selector(".smart-hints__hint").text
    time.sleep(3)
    # time.sleep(255)

# answer = math.log(int(time.time()))
