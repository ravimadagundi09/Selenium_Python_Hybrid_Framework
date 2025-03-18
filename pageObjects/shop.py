from selenium.webdriver.common.by import By

from pageObjects.checkout_confiramtion import Checkout_Confirmation
from utils.browserUtils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.shop_link=(By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards=(By.XPATH, "//div[@class='card h-100']")
        self.checkout_button=(By.XPATH, "//a[@class='nav-link btn btn-primary']")



    def addProduct(self,productName):
        self.driver.find_element(*self.shop_link).click()
        devices = self.driver.find_elements(*self.product_cards)
        devicesnames = []
        for d in devices:
            # devicesnames.append(d.find_element(By.XPATH,"div/h4/a").text)
            if d.find_element(By.XPATH, "div/h4/a").text == productName:# "Blackberry":
                d.find_element(By.XPATH, "div/button").click()
                break


    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation=Checkout_Confirmation(self.driver)
        return checkout_confirmation