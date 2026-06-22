from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Open a clean Google Chrome browser window
driver = webdriver.Chrome()
try:
    # 2. Direct the browser to Google
    driver.get("https://google.com")
    driver.maximize_window()
    print("Browser opened successfully!")
    # 3. Find the search text input box using its HTML 'name' attribute
    search_box = driver.find_element(By.NAME, "q")
    # 4. Simulate a user typing a query and hitting 'Enter'
    search_box.send_keys("Selenium Python automation")
    search_box.send_keys(Keys.RETURN)
    print("Search query submitted.")
    # 5. Leave the window open for 5 seconds so you can watch the results load
    time.sleep(5)
finally:
    # 6. Safely shut down the browser session and clean up system memory
    driver.quit()
    print("Browser closed. Test complete!")