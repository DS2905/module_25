from selenium import webdriver
import pytest
from settings import valid_password
from settings import valid_email
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_all_pets():
   # Вводим логин (email)
   pytest.driver.find_element_by_id('email').send_keys('valid_email')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('valid_password')
   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)