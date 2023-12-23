# # lesson 1 task 1
import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import os
#
# #
# #
# #
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     treasure = browser.find_element(By.ID, "treasure")
#
#     x = treasure.get_attribute("valuex")
#     print(x)
# #
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     treasure = browser.find_element(By.ID, "treasure")
#     x = treasure.get_attribute("valuex")
#
#     y = calc(x)
#
#
#
#     # Ваш код, который заполняет поле ответа
#     input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
#     input1.send_keys(y)
#
#     option1 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
#     option1.click()
#
#     option2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
#     option2.click()
#
#     button = browser.find_element(By.XPATH, "//button")
#     button.click()
# #
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# lesson 1 task 2


# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = " https://suninjuly.github.io/selects2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#
#     def calc(a, b):
#         return int(a) + int(b)
#
#
#     a_elm = browser.find_element(By.XPATH, "//span[@id='num1']")
#     b_elm = browser.find_element(By.XPATH, "//span[@id='num2']")
#
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     a = a_elm.text
#     b = b_elm.text
#
#     y = str(calc(a, b))
#
#     select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
#     select.select_by_value(y)  # ищем элемент с числом
#
#     button = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# lesson 2 task 2

# try:
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
#     x = x_element.text
#     y = calc(x)
#
#
#
#     # Ваш код, который заполняет поле ответа
#     input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
#     input1.send_keys(y)
#
#     option1 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
#     option1.click()
#
#     option2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
#     option2.click()
#
#     button = browser.find_element(By.TAG_NAME, "button")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#


# lesson 2 task 3
# try:
#     link = " http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
#     input3.send_keys("Mail.ru")
#
#     with open("test.txt", "w") as file:
#         content = file.write("automationbypython")  # create test.txt file
#     current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#
#
#     file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
#     element = browser.find_element(By.XPATH, "//input[@type='file']")
#     element.send_keys(file_path)
#
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # lesson 3 task 1
# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     button = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
#     button.click()
#     # option 1
#     # alert = browser.switch_to.alert
#     # alert.accept()
#     # option 2
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
#     x = x_element.text
#     y = calc(x)
#
#
#
#     # Ваш код, который заполняет поле ответа
#     input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
#     input1.send_keys(y)
#
#
#     button = browser.find_element(By.TAG_NAME, "button")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# lesson 3 task 2
# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
#     x = x_element.text
#     y = calc(x)
#
#     # Ваш код, который заполняет поле ответа
#     input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
#     input1.send_keys(y)
#
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# lesson 4 example 1

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
# lesson 4 example 2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
# # lesson 4 example 3
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# lesson 4 task 2
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/explicit_wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# WebDriverWait(browser, 12).until(
#     EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '100'))
#
# button = browser.find_element(By.ID, "book")
# button.click()
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
# x = x_element.text
# y = calc(x)
#
# # Ваш код, который заполняет поле ответа
# input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
# input1.send_keys(y)
#
# button = browser.find_element(By.ID, "solve")
# button.click()
# time.sleep(10)
#
# browser.quit()