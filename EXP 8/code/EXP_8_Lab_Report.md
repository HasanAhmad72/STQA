# Experiment No. 8: Functional Testing of Gmail and Amazon India

## Objective
To validate core login, messaging, search, cart, and logout functionalities for Gmail and Amazon India using manual test execution documentation and a headless automated Selenium test suite.

---

## Part 1: Manual Test Execution Documentation

### Website 1: Gmail (https://mail.google.com)

| Test Case ID | Test Scenario | Test Steps | Expected Result | Actual Result | Status |
| --- | --- | --- | --- | --- | --- |
| GM-01 | Valid Login | Enter valid email and password, then click Next | User is redirected to Gmail Inbox | Redirected to Inbox | PASS |
| GM-02 | Invalid Password | Enter valid email and incorrect password, then click Next | Error message "Wrong password" is displayed | Error message displayed | PASS |
| GM-03 | Compose Email | Click Compose, enter recipient, subject, body, then click Send | Message sent popup appears; mail saved in Sent | Email sent successfully | PASS |
| GM-04 | Search Email | Enter a search term in the top search bar and press Enter | Matching emails are filtered and listed | Relevant emails listed | PASS |
| GM-05 | User Logout | Click the profile icon at top-right and select Sign Out | Session terminates and user is redirected to login page | Logged out successfully | PASS |

### Website 2: Amazon India (https://www.amazon.in)

| Test Case ID | Test Scenario | Test Steps | Expected Result | Actual Result | Status |
| --- | --- | --- | --- | --- | --- |
| AM-01 | Search Product | Type "Laptop" in the search bar and click search | Relevant laptops are displayed | Search results displayed | PASS |
| AM-02 | Apply Filters | Select a brand filter such as HP and a price range | Only matching products remain | Filtered list displayed | PASS |
| AM-03 | Open Product | Click the first product title in the results page | Product detail page opens | Product page loaded | PASS |
| AM-04 | Add to Cart | Click the Add to Cart button on the product page | Cart badge increases and confirmation appears | Item added to cart | PASS |
| AM-05 | Remove Product | Open the Cart page and click Delete beside the item | Item is removed and cart subtotal updates | Item deleted from cart | PASS |

### Overall Result
All test cases were executed successfully without defects during the validation cycle.

---

## Part 2: Headless Python Automated Test Suite

The following script executes the core smoke tests in headless mode without opening a visible browser window.

### Run command
```bash
pytest -s test_suite_exp8.py
```

### Test file
The Python Selenium suite has been created in the same folder as this report.

---

## Conclusion
The experiment demonstrates that both Gmail and Amazon India provide expected functional behavior for the tested scenarios. The manual test execution documentation confirms the pass status, and the automated headless suite offers a reusable automated testing approach for future validation.
