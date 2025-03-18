import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# pytest -n 2   to run in parallel mode
#pytest -n 3 -m smoke --browser_name chrome  --html=reports/report.html

from pageObjects.login import  LoginPage

test_data_path="../data/test_e2eTestFramework.json"
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list) #from data list it takes on set of value at a time in test_list_item
def test_e2e(browser_Instance,test_list_item):
    driver = browser_Instance
    loginPage=LoginPage(driver)
    print(loginPage.getTitle())
    shop_page=loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])

    shop_page.addProduct(test_list_item["productName"])
    checkout_confirmation=shop_page.goToCart()

    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
    time.sleep(2)






