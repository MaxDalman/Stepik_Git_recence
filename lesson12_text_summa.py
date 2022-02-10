from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time 


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id('num1')
    number1 = input1.text
    input2 = browser.find_element_by_id('num2')
    number2 = input2.text
    number = int(number1) + int(number2)
    answer = str(number)
    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(answer)


    button1 = browser.find_element_by_class_name("btn.btn-default")
    button1.click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла