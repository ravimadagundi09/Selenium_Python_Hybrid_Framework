from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage
from utils.browserUtils import BrowserUtils


class LoginPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.username_input=(By.ID, "username") #add the arguments in a tuple
        self.password=(By.ID, "password")
        self.sign_button=(By.ID, "signInBtn")



    def login(self,username,password):  # * will break the tuple and those values become as arguments for find element
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shoppage=ShopPage(self.driver) #create obejct of next page and intitiliaze driver and return
        return shoppage
