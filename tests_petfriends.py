#pytest -v --driver Chrome --driver-path C:\Users\0\Desktop\25.5\app\chromedriver.exe
import pytest
import time
from selenium import webdriver

#1.Присутствуют все питомцы
def test_show_pets_all():
   pytest.driver.find_element_by_id('email').send_keys('ds2905@yandex.ru')
   pytest.driver.find_element_by_id('pass').send_keys('425770')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   pytest.driver.implicity_wait(10) #неявные ожидания
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

#2.Хотя бы у половины питомцев есть фото

#3.У всех питомцев есть имя, возраст и порода.
images = pytest.driver.find_elements_by_xpath('//img[@class="card-img-top"]')
names = pytest.driver.find_elements_by_xpath('//h5[@class="card-title"]')
descriptions = pytest.driver.find_elements_by_xpath('//p[@class="card-text"]')

for i in range(len(names)):
   assert images[i].get_attribute('src') != ''
   assert names[i].text != ''
   assert descriptions[i].text != ''
   parts = descriptions[i].text.split(", ")
   assert len(parts[0]) > 0
   assert len(parts[1]) > 0

#4.У всех питомцев разные имена

#5.В списке нет повторяющихся питомцев.

#6.В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов (фото, имя питомца, его возраст)
#7.В написанном тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы.