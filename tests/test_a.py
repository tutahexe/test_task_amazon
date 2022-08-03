from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
elem = driver.find_element(By.ID, "twotabsearchtextbox")
elem.clear()
elem.send_keys("software testing")
elem.send_keys(Keys.RETURN)
search_results = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
search_results[0].click()
add_to_cart = driver.find_element(By.ID, "add-to-cart-button")
add_to_cart.click()
confirmation_image = driver.find_element(By.ID, "add-to-cart-confirmation-image")
assert confirmation_image.is_displayed()
cart = driver.find_element(By.ID, "nav-cart-count")
cart.click()
item_in_cart = driver.find_element(By.CLASS_NAME, "a-truncate-cut")
assert item_in_cart.text == "Full Stack Testing: A Practical Guide for Delivering High Quality Software"
assert "No results found." not in driver.page_source
driver.close()