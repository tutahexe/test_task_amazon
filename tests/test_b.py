import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from models.item import Item

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
time.sleep(10)
elem = driver.find_element(By.ID, "twotabsearchtextbox")
elem.clear()
elem.send_keys("software testing")
elem.send_keys(Keys.RETURN)
search_results = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
for search_result in search_results:
    try:
        item_name = search_result.find_element(By.CLASS_NAME, "a-size-base-plus.a-color-base.a-text-normal").text
    except:
        item_name = 'kek'
    try:
        item_rate = search_result.find_element(By.CLASS_NAME, "a-icon-alt").get_attribute("textContent")
        item_rate_2 = str(item_rate)
        item_rate_3 = item_rate_2[0:3]
    except:
        item_rate_3 = 0.0
    try:
        item_date = search_result.find_element(By.CLASS_NAME, "a-size-base.a-color-secondary.a-text-normal").get_attribute("textContent")
    except:
        item_date = "Aug 1, 0001"
    item = Item(item_name, item_rate_3, item_date)
    print(item)

driver.close()
