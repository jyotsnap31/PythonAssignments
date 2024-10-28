import time
from datetime import date, datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from BaseConfig import BaseData

def testEbay():
    driver = webdriver.Chrome()
    driver.get(BaseData.BASE_URL)
    driver.maximize_window()

    driver.find_element(By.ID, "gh-ac").send_keys(BaseData.SEARCH_TEXT)
    driver.find_element(By.ID, "gh-btn").click()

    driver.find_element(By.XPATH, "//span[@class = 'srp-format-tabs-h2' and text()='Buy It Now']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='srp-sort srp-sort--filter-evolution']/span/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[text()='Time: newly listed']").click()
    time.sleep(2)
    currentdate1 = date.today().day
    currentmonth1 = datetime.now().strftime('%b')
    expectedText = currentmonth1+"-"+str(currentdate1)
    print(expectedText)
    actualText=driver.find_element(By.XPATH, "(//span[@class='s-item__dynamic s-item__listingDate']/span)[1]").text
    assert (actualText.__contains__(expectedText))
    driver.close()













