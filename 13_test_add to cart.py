import pytest
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time



@pytest.fixture
def driver(request):
    # wd = webdriver.Ie()
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    # wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_add_to_cart(driver):

    driver.get("http://localhost/litecart/en/")
    price_before = driver.find_element_by_xpath("//a[ @class ='content']").text

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id = 'box-most-popular']//li[1]//a[1]")))
    hrefs = []
    duck_crowd = driver.find_elements_by_xpath("//ul//li//a[@class='link']")


    j=0
    o=0
    while j < 5:
        driver.find_element_by_xpath("//div[@id='logotype-wrapper']//a").click()
        items = driver.find_elements_by_xpath("//ul//li//a[@class='link']") #массив всех товаров
        while items[j].get_attribute('href') in hrefs and o < 5:
            j = j+1
            o = o+1
        hrefs.append(items[j].get_attribute('href'))
        items[j].click()

        price_before= driver.find_element_by_xpath("//a[ @class ='content']").text
        driver.find_element_by_xpath("// button[@name = 'add_cart_product']").click()
        price_after = driver.find_element_by_xpath("//a[@class ='content']").text
        k = 0

        while price_before == price_after and k < 10:
            price_after = driver.find_element_by_xpath("//a[@class ='content']").text
            k = k + 1
            time.sleep(1)
        j = j+1





        j=j+1


    driver.find_element_by_xpath("//a[contains(text(), 'Checkout »')]").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "remove_cart_item")))
    driver.find_element_by_xpath("//ul[@class='shortcuts']//li[1]").click()


    table_before = driver.find_element_by_xpath("//table[@class ='dataTable rounded-corners']").get_attribute("outerHTML")
    i = 0
    j = 0
    while i < 4:
        driver.find_element_by_name("remove_cart_item").click()
        table_after = driver.find_element_by_xpath("//table[@class ='dataTable rounded-corners']").get_attribute("outerHTML")
        while table_after == table_before and j < 5:
            table_after = driver.find_element_by_xpath("//table[@class ='dataTable rounded-corners']").get_attribute("outerHTML")
            time.sleep(1)
            j= j+1
        i = i+1



