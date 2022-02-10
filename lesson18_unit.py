from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
        def test_registration1(self): 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
            input1.send_keys("Max")
            input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
            input2.send_keys("Daubert")
            input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
            input3.send_keys("maksimdaubert@gmail.com")
            input4 = browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
            input4.send_keys("911")
            input5 = browser.find_element_by_xpath('//input[@placeholder="Input your address:"]')
            input5.send_keys("Saint-Petersburg")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)



        def test_registration2(self): 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
            input1.send_keys("Max")
            input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
            input2.send_keys("Daubert")
            input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
            input3.send_keys("maksimdaubert@gmail.com")
            input4 = browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
            input4.send_keys("911")
            input5 = browser.find_element_by_xpath('//input[@placeholder="Input your address:"]')
            input5.send_keys("Saint-Petersburg")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)




if __name__ == "__main__":
    unittest.main()