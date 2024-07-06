
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://ya.ru")
search_box = driver.find_element(By.id,"searchbox")
search_box.send_keys("Hello world")
find_button = driver.find_element(By.class_name,"btn")
find_button.click()
driver.quit()
