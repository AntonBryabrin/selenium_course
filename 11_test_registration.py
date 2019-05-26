import pytest

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from faker import Faker #https://github.com/joke2k/faker/wiki



@pytest.fixture
def driver(request):
    # wd = webdriver.Ie()
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    # wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_registration(driver):
    fake = Faker()

    driver.get("http://localhost/litecart/en/")
    driver.find_element_by_xpath("//a[contains(text(), 'New customers click here')]").click()
    driver.find_element_by_name("tax_id").send_keys('1')
    driver.find_element_by_name("company").send_keys('companytest')
    driver.find_element_by_name("firstname").send_keys(fake.first_name())
    driver.find_element_by_name("lastname").send_keys(fake.last_name())
    driver.find_element_by_name("address1").send_keys(fake.address())
    driver.find_element_by_name("postcode").send_keys('426000')
    driver.find_element_by_name("city").send_keys('Chicago')


    driver.find_element_by_xpath("//span[@class='select2-selection__arrow']").click()


    driver.find_element_by_xpath("//input[@class ='select2-search__field']").send_keys('Select')
    driver.find_element_by_xpath("//input[@class ='select2-search__field']").send_keys(Keys.ENTER)

    driver.find_element_by_xpath("//span[@class='select2-selection__arrow']").click()
    driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys('Russian Federation')
    driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys(Keys.ENTER)

    email=fake.safe_email()
    driver.find_element_by_name("email").send_keys(email)

    driver.find_element_by_name("phone").send_keys('12345678')
    driver.find_element_by_name("password").send_keys('qwerty')

    driver.find_element_by_xpath("//input[@name='confirmed_password']").send_keys('qwerty')

    driver.find_element_by_xpath("//button[@name='create_account']").click()


    driver.find_element_by_xpath("//div[@class='content']//a[contains(text(),'Logout')]").click()



    driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@name='password']").send_keys('qwerty')
    driver.find_element_by_xpath("//button[@name='login']").click()

    driver.find_element_by_xpath("//div[@class='content']//a[contains(text(),'Logout')]").click()







