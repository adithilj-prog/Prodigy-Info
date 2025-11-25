from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize ChromeDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Go to demo site
driver.get("https://www.saucedemo.com/")  # replace with your demo site if different

# -------------------
# 1. LOGIN TESTS
# -------------------

# Positive Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
)
print(" Positive login successful")

# Negative Login
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)
if "Epic sadface" in driver.page_source:
    print(" Negative login test passed (error shown)")
else:
    print(" Negative login test failed")

# -------------------
# 2. PRODUCT INTERACTION
# -------------------

# Login again with valid credentials
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add to Cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
print(" Add to cart works")

# Apply Filters
driver.find_element(By.CLASS_NAME, "product_sort_container").click()
driver.find_element(By.XPATH, "//option[@value='az']").click()
print(" Filter A–Z applied")

# -------------------
# 3. CHECKOUT FLOW
# -------------------

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()

# Fill Form
driver.find_element(By.ID, "first-name").send_keys("Adithi")
driver.find_element(By.ID, "last-name").send_keys("Tester")
driver.find_element(By.ID, "postal-code").send_keys("560001")
driver.find_element(By.ID, "continue").click()

# Payment Overview
if "Checkout: Overview" in driver.page_source:
    print(" Payment overview displayed")

# Cancel Order
driver.find_element(By.ID, "cancel").click()
print(" Cancel order works")

# Finish Order
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Adithi")
driver.find_element(By.ID, "last-name").send_keys("Tester")
driver.find_element(By.ID, "postal-code").send_keys("560001")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()

# Confirmation
if "Thank you for your order!" in driver.page_source:
    print(" Order confirmation displayed")

driver.quit()
