class HomePage():
    def __init__(self, driver, WebDriverWait, EC, By):
        self.driver = driver
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.By = By
        self.xpath_locator_all_items_links = "//div[@class='content']//a[@class='link']"
        self.xpath_locator_price_before = "//a[@class ='content']"
        self.xpath_locator_checkout = "//a[contains(text(), 'Checkout »')]"
        self.logo_locatorxpath = "logotype-wrapper"
        #self.xpath_locator_add_to_cart = "//button[@name = 'add_cart_product']"
        #self.xpath_locator_logo = "//div[@id = 'logotype-wrapper']//a"

    def get_all_items_links(self):
        all_items_links = self.driver.find_elements_by_xpath(self.xpath_locator_all_items_links)
        #print(self.driver.find_elements_by_xpath(self.xpath_locator_all_items_links))
        return all_items_links

    #def click_to_logo(self):
    #    self.driver.find_elements_by_xpath(self.xpath_locator_logo)

    def get_price_before(self):
        self.driver.find_element_by_xpath(self.xpath_locator_price_before).text

    #def click_add_to_cart(self):
    #    self.driver.find_element_by_xpath(self.xpath_locator_add_to_cart).click()
    def click_checkout(self):
        self.driver.find_element_by_xpath(self.xpath_locator_checkout).click()

    def wait_logo_to_load(self):

        #self.driver.find_element_by_name(self.username_locatorname).send_keys(username)
        self.WebDriverWait(self.driver, 100).until(self.EC.visibility_of_element_located((self.By.ID, self.logo_locatorxpath)))