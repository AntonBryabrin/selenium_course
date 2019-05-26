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
    #wd = webdriver.Ie()
    #wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    wd = webdriver.Chrome()
    #wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_logs(driver):
    driver.delete_all_cookies()
    driver.get("http://localhost/litecart/admin/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    hrefs=[]
    items = driver.find_elements_by_xpath("//tr//td[3]/a")

    for i in items:
        #i.get_attribute('href').append(hrefs)
        hrefs.append(i.get_attribute('href'))


    for i in hrefs:
        driver.get(i)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))

        assert len(driver.get_log("browser")) == 0

        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
