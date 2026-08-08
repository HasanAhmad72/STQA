import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# -------------------------------------------------------------
# TEST CASE 1: Valid Login Verification
# -------------------------------------------------------------
def test_case_1_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    title_text = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert title_text == "Products", "Failed: User did not navigate to Products page"
    print("\n[PASS] Test Case 1: Valid Login successful")


# -------------------------------------------------------------
# TEST CASE 2: Invalid/Locked User Verification
# -------------------------------------------------------------
def test_case_2_locked_out_user(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "locked out" in error_msg, "Failed: Error message for locked user not displayed"
    print("[PASS] Test Case 2: Locked-out user validation successful")


# -------------------------------------------------------------
# TEST CASE 3: Add Product to Cart Verification
# -------------------------------------------------------------
def test_case_3_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert cart_badge == "1", "Failed: Shopping cart badge count mismatch"
    print("[PASS] Test Case 3: Add to cart successful")


# -------------------------------------------------------------
# TEST CASE 4: User Logout Verification
# -------------------------------------------------------------
def test_case_4_logout(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()

    login_btn_visible = driver.find_element(By.ID, "login-button").is_displayed()
    assert login_btn_visible, "Failed: User was not redirected to login page"
    print("[PASS] Test Case 4: Logout successful")
