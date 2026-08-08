import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(8)
    yield driver
    driver.quit()


# -------------------------------------------------------------
# WEBSITE 1: Gmail Landing / Login Page Tests
# -------------------------------------------------------------
def test_GM_01_gmail_landing(driver):
    driver.get("https://mail.google.com")
    page_text = driver.page_source.lower()
    assert "gmail" in page_text or "sign in" in page_text or "google" in page_text
    print("\n[PASS] GM-01: Gmail page loaded successfully")


def test_GM_02_gmail_invalid_user(driver):
    driver.get("https://accounts.google.com/signin/v2/identifier?service=mail")
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_input.clear()
    email_input.send_keys("invalid_test_user_999@gmail.com" + Keys.ENTER)

    current_url = driver.current_url.lower()
    assert "accounts.google.com" in current_url
    print("[PASS] GM-02: Invalid user input handled")


# -------------------------------------------------------------
# WEBSITE 2: Amazon India Functional Tests
# -------------------------------------------------------------
def test_AM_01_amazon_search(driver):
    driver.get("https://www.amazon.in")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.clear()
    search_box.send_keys("Laptop" + Keys.ENTER)

    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-component-type='s-search-result']"))
    )
    assert len(results) > 0, "No search results returned for 'Laptop'"
    print("[PASS] AM-01: Amazon search results verified")


def test_AM_02_amazon_cart_navigation(driver):
    driver.get("https://www.amazon.in/gp/cart/view.html")
    body = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    page_text = body.text.lower()
    assert "shopping cart" in page_text or "your amazon cart" in page_text or "empty" in page_text
    print("[PASS] AM-02: Amazon Cart accessible")


if __name__ == "__main__":
    pytest.main(["-s", __file__])
