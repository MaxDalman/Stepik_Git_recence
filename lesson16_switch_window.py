from selenium import webdriver
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('button')
    input1.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_value = browser.find_element_by_id("input_value")
    otvet = x_value.text
    y = calc(int(otvet))
    
    answer1 = browser.find_element_by_id("answer")
    answer1.send_keys(y)


    button1 = browser.find_element_by_class_name("btn.btn-primary")
    button1.click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла