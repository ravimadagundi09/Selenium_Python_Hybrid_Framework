from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sortTable(browser_Instance):
    driver = browser_Instance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/Offers")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    actualitems = driver.find_elements(By.XPATH, "//tr/td[1]")
    itemssortedactual = []

    for items in actualitems:
        itemssortedactual.append(items.text)
    print(itemssortedactual)

    orginalsorteditems = itemssortedactual.copy()

    itemssortedactual.sort()

    assert itemssortedactual == orginalsorteditems