#pytest -v --driver Chrome --driver-path C:\Users\0\Desktop\25.5\app\chromedriver.exe
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#1
def test_show_all_pets():
   pytest.driver.find_element_by_id('email').send_keys('ds2905@yandex.ru')
   pytest.driver.find_element_by_id('pass').send_keys('425770')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click() #входим в свой аккаунт
   pytest.driver.implicity_wait(10) #неявные ожидания
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

#У всех питомцев есть фото, имя, возраст и порода.   
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

#2
def test_show_my_pets():
   pytest.driver.find_element_by_id('email').send_keys('ds2905@yandex.ru')
   pytest.driver.find_element_by_id('pass').send_keys('425770')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click() #входим в свой аккаунт
   wait = WebDriverWait(pytest.driver, 5) #явные ожидания
   
   assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME,'h1'), "PetFriends"))
   pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click() #открываем своих питомцев
   assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), "ds"))
   css_locator = 'tbody>tr'
   data_my_pets = pytest.driver.find_elements_by_css_selector(css_locator)
   for i in range(len(data_my_pets)):
      assert wait.until(EC.visibility_of(data_my_pets[i]))

#У всех наших питомцев есть фото.  
   image_my_pets = pytest.driver.find_elements_by_css_selector('img[style="max-width: 100px; max-height: 100px;"]')
   for i in range(len(image_my_pets)):
      if image_my_pets[i].get_attribute('src') != '':
         assert wait.until(EC.visibility_of(image_my_pets[i]))
#У всех наших питомцев есть имена. 
   name_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
   for i in range(len(name_my_pets)):
      assert wait.until(EC.visibility_of(name_my_pets[i]))
#У всех наших питомцев есть порода. 
   type_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[2]')
   for i in range(len(type_my_pets)):
      assert wait.until(EC.visibility_of(type_my_pets[i]))
#У всех наших питомцев есть возраст. 
   age_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')
   for i in range(len(age_my_pets)):
      assert wait.until(EC.visibility_of(age_my_pets[i]))      

   all_statistics = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split("\n")
   statistics_pets = all_statistics[1].split(" ")
   all_my_pets = int(statistics_pets[-1])
   assert len(data_my_pets) == all_my_pets
      m = 0
   for i in range(len(image_my_pets)):
      if image_my_pets[i].get_attribute('src') != '':
         m += 1
   assert m >= all_my_pets/2
#У всех питомцев есть имя.
   for i in range(len(name_my_pets)):
      assert name_my_pets[i].text != ''
#У всех питомцев есть порода.
   for i in range(len(type_my_pets)):
      assert type_my_pets[i].text != ''
#У всех питомцев есть возраст.
   for i in range(len(age_my_pets)):
      assert age_my_pets[i].text != ''
#У всех питомцев разные имена.
   list_name_my_pets = []
   for i in range(len(name_my_pets)):
      list_name_my_pets.append(name_my_pets[i].text)
   set_name_my_pets = set(list_name_my_pets) 
   assert len(list_name_my_pets) == len(set_name_my_pets)
