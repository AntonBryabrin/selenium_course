class CheckOutPage():
    def __init__(self, driver):
        self.driver = driver
        self.xpath_locator_shortcuts = "//ul[@class='shortcuts']//li[1]"
        self.xpath_locator_table_to_buy = "//table[@class ='dataTable rounded-corners']"
        self.name_locator_remove_from_cart = "remove_cart_item"




    def click_shortcut(self):
        self.driver.find_element_by_xpath(self.xpath_locator_shortcuts).click()

    def get_table_to_buy(self):
        table_to_buy = self.driver.find_element_by_xpath(self.xpath_locator_table_to_buy)
        return table_to_buy

    def remove_from_cart(self):
        remove_from_cart = self.driver.find_element_by_name(self.name_locator_remove_from_cart)
        return remove_from_cart