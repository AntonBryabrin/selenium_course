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
    #wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_new_window(driver):
    fake = Faker()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_xpath("//a[contains(text(), 'Afghanistan')]").click()

    originalWindow = driver.current_window_handle
    hrefs=driver.find_elements_by_xpath("//form//table//tbody//tr//td//a[@target='_blank']")

    openedWindows = driver.window_handles
    k=0
    for j in hrefs:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        hrefs[k].click()
        #while openedWindows == newopenedWin:
        #    newopenedWin = driver.window_handles
        newopenedWindows = driver.window_handles
        assert newopenedWindows != openedWindows






        for i in newopenedWindows:
            if i not in openedWindows:
                driver.switch_to_window(i)



        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        driver.close()
        driver.switch_to_window(originalWindow)

        k=k+1
