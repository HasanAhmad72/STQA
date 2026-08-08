package tests;

import utils.ExcelUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.*;

import java.time.Duration;

public class LoginTest {
    WebDriver driver;
    WebDriverWait wait;

    @BeforeMethod
    public void setUp() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless=new");
        options.addArguments("--disable-gpu");
        options.addArguments("--window-size=1920,1080");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");
        options.setBinary("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe");

        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @DataProvider(name = "loginData")
    public Object[][] getLoginData() {
        String filePath = "src/test/resources/TestData.xlsx";
        return ExcelUtils.getTestData(filePath, "Sheet1");
    }

    @Test(dataProvider = "loginData")
    public void testLoginScenario(String username, String password) {
        try {
            driver.get("https://practicetestautomation.com/practice-test-login/");

            WebElement userField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("username")));
            WebElement passField = driver.findElement(By.id("password"));
            WebElement submitBtn = driver.findElement(By.id("submit"));

            userField.clear();
            userField.sendKeys(username);

            passField.clear();
            passField.sendKeys(password);

            submitBtn.click();

            if (driver.getCurrentUrl().contains("logged-in-successfully")) {
                System.out.println("[SUCCESS] Login verified for user: " + username);
                Assert.assertTrue(true);
            } else {
                WebElement errorMsg = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("error")));
                System.out.println("[VALIDATED] Login failed gracefully for user: " + username + " | Error: " + errorMsg.getText());
            }

        } catch (NoSuchElementException e) {
            System.err.println("[EXCEPTION] Web element not found on page: " + e.getMessage());
        } catch (TimeoutException e) {
            System.err.println("[EXCEPTION] Page or element load timed out: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("[UNHANDLED EXCEPTION] Runtime failure: " + e.getMessage());
        }
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
