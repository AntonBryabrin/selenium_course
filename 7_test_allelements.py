import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    request.addfinalizer(wd.quit)
    return wd



def test_allelements(driver):

    def h1present():
        try:
            driver.find_element_by_tag_name('h1')
        except NoSuchElementException:
            return False
        return True

    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")

    driver.find_element_by_name("login").click()
    
    i=0
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Appearence')]")))
    ids = driver.find_elements_by_xpath("//*[@id='app-']/a/span[2]")

    for ii in ids:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Appearence')]")))
        idsnew = driver.find_elements_by_xpath("//*[@id='app-']/a/span[2]")
        idsnew[i].click()
        i=i+1
        assert h1present()

        sub_menu = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")

        if len(sub_menu) < 1:

            assert h1present()

        for j in range(len(sub_menu)):
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Appearence')]")))
            sub_menu_el = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
            sub_menu_el[j].click()


            assert h1present()



