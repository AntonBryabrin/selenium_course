import pytest
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By





@pytest.fixture
def driver(request):
    # wd = webdriver.Ie()
    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe")
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_item_of_product_verify(driver):

    class Page():
        def __init__(self, driver, where):
            self.driver = driver
            if where == 'item':
                self.name = driver.find_element_by_xpath("//h1").text
                self.regular_price = driver.find_element_by_xpath("//s[@class='regular-price']").text
                self.campaign_price = driver.find_element_by_xpath("//strong[@class='campaign-price']").text

                self.reg_price_color = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("color")
                self.reg_price_fontdec = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("text-decoration")
                self.reg_price_fontweight = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("font-weight")
                self.reg_price_fontsize = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("font-size")

                self.campaign_price_color = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("color")
                self.campaign_price_fontdec = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("text-decoration")
                self.campaign_price_fontweight = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("font-weight")
                self.campaign_price_fontsize = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("font-size")


            if where == 'main':
                self.name = driver.find_element_by_xpath("//div[@id='box-campaigns']//div[@class='name'][contains(text(),*)]").text

                self.regular_price = driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").text
                self.reg_price_color = driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").value_of_css_property("color")
                self.reg_price_fontdec = driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").value_of_css_property("text-decoration")
                self.reg_price_fontweight = driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").value_of_css_property("font-weight")
                self.reg_price_fontsize = driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price'][contains(text(),*)]").value_of_css_property("font-size")
                self.campaign_price_color = driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").value_of_css_property("color")
                self.campaign_price_fontdec = driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").value_of_css_property("text-decoration")
                self.campaign_price_fontweight = driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").value_of_css_property("font-weight")
                self.campaign_price_fontsize = driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").value_of_css_property("font-size")
                self.campaign_price = driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price'][contains(text(),*)]").text

    driver.get("https://pgh.cbwp.net/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.image-wrapper > img.image")))
    main = Page(driver, 'main')
    assert [int(s) for s in re.findall(r'\d+', main.reg_price_fontsize)][0] < [int(s) for s in re.findall(r'\d+', main.campaign_price_fontsize)][0]
    driver.find_element_by_xpath("//div[@id='box-campaigns']//a[@class='link']").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.image-wrapper > img.image")))
    item = Page(driver, 'item')

    assert [int(s) for s in re.findall(r'\d+', item.reg_price_fontsize)][0] < [int(s) for s in re.findall(r'\d+', item.campaign_price_fontsize)][0]

    assert main.name == item.name
    assert main.regular_price == item.regular_price
    assert main.campaign_price == item.campaign_price

    assert main.reg_price_color in ['rgb(119, 119, 119)', 'rgba(119, 119, 119, 1)']
    assert main.reg_price_fontdec in ['line-through', 'line-through solid rgb(119, 119, 119',
                                      'line-through solid rgb(119, 119, 119)']
    assert main.reg_price_fontweight == '400'

    assert main.campaign_price_color in ['rgb(204, 0, 0)', 'rgba(204, 0, 0, 1)']
    assert main.campaign_price_fontdec in ['none', 'none solid rgb(204, 0, 0)']
    assert main.campaign_price_fontweight in ['900', '700']

    assert item.reg_price_color in ['rgb(119, 119, 119)', 'rgba(119, 119, 119, 1)']
    assert item.reg_price_fontdec in ['line-through', 'line-through solid rgb(119, 119, 119)']
    assert item.reg_price_fontweight == '400'

    assert item.campaign_price_color in ['rgb(204, 0, 0)', 'rgba(204, 0, 0, 1)']
    assert item.campaign_price_fontdec in ['none', 'none solid rgb(204, 0, 0)']
    assert item.campaign_price_fontweight in ['900', '700']



