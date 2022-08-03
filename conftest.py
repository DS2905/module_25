#pip install selenium
#pip install pytest-selenium
import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\Users\0\Desktop\25.5\app\chromedriver.exe')

   # Переходим на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()
