import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By




@pytest.fixture
def driver(request):
    #wd = webdriver.Ie()
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    request.addfinalizer(wd.quit)
    return wd



def test_stickers(driver):

    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.image-wrapper > img.image")))
    sticker_counter = 0
    duck_crowd = driver.find_elements_by_xpath(".//ul[@class='listing-wrapper products']//li")


    for duck in duck_crowd:
        sticker = duck.find_elements_by_xpath(".//div[starts-with(@class,'sticker')]")
        sticker_counter = sticker_counter+len(sticker)

    assert sticker_counter == len(duck_crowd)



