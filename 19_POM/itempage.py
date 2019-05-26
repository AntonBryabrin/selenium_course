class ItemPage():
    def __init__(self, driver):
        self.driver = driver
        self.xpath_locator_logo = "//div[@id = 'logotype-wrapper']//a"
        self.xpath_locator_add_to_cart = "//button[@name = 'add_cart_product']"
        self.xpath_locator_price_before = "//span[@class='formatted_value']"

    def click_logo(self):
        self.driver.find_element_by_xpath(self.xpath_locator_logo).click()

    def click_add_to_cart(self):
        self.driver.find_element_by_xpath(self.xpath_locator_add_to_cart).click()

    def get_price_before(self):
        self.driver.find_element_by_xpath(self.xpath_locator_price_before).text