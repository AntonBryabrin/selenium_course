import pytest
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from faker import Faker #https://github.com/joke2k/faker/wiki
import time
from faker import Faker #https://github.com/joke2k/faker/wiki
import os

@pytest.fixture
def driver(request):
    # wd = webdriver.Ie()
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    # wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_new_item(driver):
    fake = Faker()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")

    driver.find_element_by_name("login").click()
    #driver.get("http://localhost/litecart/admin")
    driver.find_element_by_xpath("//span[contains(text(), 'Catalog')]").click()
    driver.find_element_by_xpath("//a[contains(text(), 'Add New Product')]").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1")))

    driver.find_element_by_xpath("//label[contains(text(), 'Enabled')] // input[ @ name = 'status']").click()
    name= fake.word()
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys(name)
    driver.find_element_by_xpath("//input[@name = 'code']").send_keys(fake.pyint())
    driver.find_element_by_xpath("//input[@name = 'new_images[]']").send_keys(os.getcwd() + "\\image.png")
    driver.find_element_by_name("quantity").click()
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys('99')
    driver.find_element_by_name("quantity").send_keys(Keys.TAB)

    driver.find_element_by_xpath("//a[contains(text(), 'Information')]").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1")))

    driver.find_element_by_xpath("//input[@name = 'short_description[en]']").send_keys(fake.text(max_nb_chars=100))
    driver.find_element_by_xpath("//div[@class='trumbowyg-editor']").send_keys(fake.text(max_nb_chars=300))



    driver.find_element_by_xpath("//a[contains(text(), 'Prices')]").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1")))



    driver.find_element_by_xpath("//input[@name = 'purchase_price']").click()
    driver.find_element_by_xpath("//input[@name = 'purchase_price']").clear()
    driver.find_element_by_xpath("//input[@name = 'purchase_price']").send_keys('99')


    driver.find_element_by_name("purchase_price_currency_code").click()

    driver.find_element_by_xpath("//select[@name = 'purchase_price_currency_code']").send_keys('US Dollars')
    driver.find_element_by_name("prices[USD]").send_keys('999')


    driver.find_element_by_xpath("//button[@name = 'save']").click()
    driver.find_element_by_xpath("//li[@id='doc-catalog']//span[@class='name'][contains(text(),'Catalog')]").click()
    str = driver.page_source


    assert re.search(name, str)










