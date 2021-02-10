from selenium import webdriver
import unittest


class TestForm(unittest.TestCase):

    def setUp(self):  # обязательное название метода
        self.driver = webdriver.Chrome()
        
    def form(self, link):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('div.first_block .form-control.first').send_keys("Ivan")
        browser.find_element_by_css_selector('div.first_block .form-control.second').send_keys("Petrov")
        browser.find_element_by_css_selector('div.first_block .form-control.third').send_keys("Petrov")

        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()
        # Проверяем, что смогли зарегистрироваться
        
        # находим элемент, содержащий текст
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        welcome_text = browser.find_element_by_tag_name('h1').text
        return welcome_text
        
    def test_form1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_form2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):  # обязательное название метода
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
