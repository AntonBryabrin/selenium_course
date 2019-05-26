import pytest
from selenium import webdriver



@pytest.fixture
def driver(request):
    #wd = webdriver.Ie()
    #wd = webdriver.Chrome()
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    assert driver.find_elements_by_xpath("//div[@class='logotype']//a//img")
    
    