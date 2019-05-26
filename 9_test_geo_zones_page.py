import pytest
from selenium import webdriver



@pytest.fixture
def driver(request):
    # wd = webdriver.Ie()
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    request.addfinalizer(wd.quit)
    return wd


def test_geo_zones_page(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")

    driver.find_element_by_name("login").click()

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    countries_in_geozones=[]

    links_for_countries=driver.find_elements_by_xpath("//form//a[contains(text(),*)]")
    for link in links_for_countries:
        print(link.get_attribute('href'))
        countries_in_geozones.append(link.get_attribute('href'))

    j=0

    for i in countries_in_geozones:
        geozones_list=[]
        driver.get(countries_in_geozones[j])
        geo_zones_in_selects = driver.find_elements_by_xpath(".//*[@id='table-zones']/tbody/tr/td/select[starts-with(@name,'zones[') and not(contains (@aria-hidden,'true'))]/option[@selected='selected']")
        for geozones in geo_zones_in_selects:
            geozones_list.append(geozones.text)

        sorted_geozones_list = sorted(geozones_list)
        print(geozones_list)
        assert geozones_list == sorted_geozones_list
        j=j+1

