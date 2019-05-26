
import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By





@pytest.fixture
def driver(request):
    # wd = webdriver.Ie()
    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    #wd = webdriver.Chrome()
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '62.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1024x768'
    }
    wd = webdriver.Remote(
        command_executor='http://johnsmith1639:npVTZqF8Ho4rm9ZsxoRf@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)

    request.addfinalizer(wd.quit)
    return wd


def test_cloud(driver):
    driver.get("https://pgh.cbwp.net/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.image-wrapper > img.image")))

    duck_crowd = driver.find_element_by_xpath("//div[@id='box-campaigns']//a[@class='link']")

    main_name = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//div[@class='name'][contains(text(),*)]").text

    main_regular_price = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").text

    main_reg_price_color = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").value_of_css_property("color")
    main_reg_price_fontdec = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").value_of_css_property(
        "text-decoration")
    main_reg_price_fontweight = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").value_of_css_property(
        "font-weight")
    main_reg_price_fontsize = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").value_of_css_property("font-size")

    main_campaign_price_color = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").value_of_css_property(
        "color")
    main_campaign_price_fontdec = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").value_of_css_property(
        "text-decoration")
    main_campaign_price_fontweight = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").value_of_css_property(
        "font-weight")
    main_campaign_price_fontsize = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").value_of_css_property(
        "font-size")
    main_campaign_price = duck_crowd.find_element_by_xpath(
        "//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").text


    duck_crowd.click()
    item_regular_price = driver.find_element_by_xpath("//s[@class='regular-price']").text
    item_campaign_price = driver.find_element_by_xpath("//strong[@class='campaign-price']").text
    item_name = driver.find_element_by_tag_name("h1").text

    item_reg_price_color = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("color")
    item_reg_price_fontdec = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property(
        "text-decoration")
    item_reg_price_fontweight = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property(
        "font-weight")
    item_reg_price_fontsize = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property(
        "font-size")

    item_campaign_price_color = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property(
        "color")
    item_campaign_price_fontdec = driver.find_element_by_xpath(
        "//strong[@class='campaign-price']").value_of_css_property("text-decoration")
    item_campaign_price_fontweight = driver.find_element_by_xpath(
        "//strong[@class='campaign-price']").value_of_css_property("font-weight")
    item_campaign_price_fontsize = driver.find_element_by_xpath(
        "//strong[@class='campaign-price']").value_of_css_property("font-size")


    assert main_name == item_name
    assert main_regular_price == item_regular_price
    assert main_campaign_price == item_campaign_price

    assert main_reg_price_color in ['rgb(119, 119, 119)', 'rgba(119, 119, 119, 1)']
    assert main_reg_price_fontdec in ['line-through', 'line-through solid rgb(119, 119, 119',
                                      'line-through solid rgb(119, 119, 119)']
    assert main_reg_price_fontweight == '400'

    assert main_campaign_price_color in ['rgb(204, 0, 0)', 'rgba(204, 0, 0, 1)']
    assert main_campaign_price_fontdec in ['none', 'none solid rgb(204, 0, 0)']
    assert main_campaign_price_fontweight in ['900', '700']

    assert item_reg_price_color in ['rgb(119, 119, 119)', 'rgba(119, 119, 119, 1)']
    assert item_reg_price_fontdec in ['line-through', 'line-through solid rgb(119, 119, 119)']
    assert item_reg_price_fontweight == '400'

    assert item_campaign_price_color in ['rgb(204, 0, 0)', 'rgba(204, 0, 0, 1)']
    assert item_campaign_price_fontdec in ['none', 'none solid rgb(204, 0, 0)']
    assert item_campaign_price_fontweight in ['900', '700']