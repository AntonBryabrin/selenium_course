
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import unittest
from POMissue.homepage import HomePage
from POMissue.itempage import ItemPage
from POMissue.checkout import CheckOutPage

class AddToCartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://localhost/litecart/en/")
        homepage = HomePage(driver,WebDriverWait,EC,By)
        itempage = ItemPage(driver)
        checkout = CheckOutPage(driver)
        homepage.get_all_items_links()

        j = 0
        o = 0
        hrefs = []

        while j < 3:
            homepage.wait_logo_to_load()
            items = homepage.get_all_items_links()

            while items[j].get_attribute('href') in hrefs and o < 5:
                j = j + 1
                o = o + 1

            hrefs.append(items[j].get_attribute('href'))
            items[j].click()
            j = j+1

            price_before = itempage.get_price_before()
            itempage.click_add_to_cart()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class ='content']")))
            price_after = itempage.get_price_before()

            k = 0
    
            if price_before == price_after and k < 10:
                price_after = itempage.get_price_before()
                k = k + 1
                time.sleep(1)

            itempage.click_logo() #Вернуться на главную

        homepage.click_checkout()
        homepage.wait_logo_to_load()
        checkout.click_shortcut()
        table_before = checkout.get_table_to_buy().get_attribute("outerHTML")

        i = 0
        j = 0

        while i < 3:

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "remove_cart_item")))
            checkout.remove_from_cart().click()
            table_after = checkout.get_table_to_buy().get_attribute("outerHTML")

            if table_after == table_before and j < 5:
                time.sleep(1)
                j = j + 1
            i = i + 1

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id = 'checkout-cart-wrapper']/p/em")))
        assert "There are no items in your cart" in driver.find_element_by_xpath("//div[@id = 'checkout-cart-wrapper']/p/em").text



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()