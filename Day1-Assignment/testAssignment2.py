import time
from datetime import date, datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from BaseConfig import BaseData

def testAmazon():
    driver = webdriver.Chrome()
    driver.get(BaseData.BASE_URL_AMAZON)
    driver.maximize_window()
    #driver.implicitly_wait(10)

    driver.find_element(By.XPATH, '//a[text()="Today\'s Deals"]').click()
    driver.find_element(By.CSS_SELECTOR, "a#nav-hamburger-menu>i").click()
    time.sleep(5)
    element = driver.find_element(By.XPATH, '//div[text()="Women\'s Fashion"]/following-sibling::i')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    #driver.find_element(By.XPATH, '//div[text()="Women\'s Fashion"]/following-sibling::i').click()
    element.click()
    time.sleep(5)
    watch_element =driver.find_element(By.XPATH, "(//a[text()='Watches'])[2]")
    driver.execute_script("arguments[0].click();", watch_element)
    driver.find_element(By.XPATH, "//input[@id='apb-browse-refinements-checkbox_4']/following-sibling::i").click()
    time.sleep(5)

    actual_text=driver.find_element(By.XPATH, "//div[@class='s-no-outline']/h2").text
    expected_text = "Results"


    assert actual_text == expected_text


