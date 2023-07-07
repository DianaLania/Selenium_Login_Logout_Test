from selenium import webdriver
import time
import unittest
from SampleTest.Pages.loginPage import LoginPage
from SampleTest.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_admin_link()
        homepage.click_menu_icon()
        homepage.click_logout_link()

        # driver.find_element(By.NAME, "username").send_keys("Admin")
        # driver.find_element(By.NAME, "password").send_keys("admin123")
        # driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # driver.find_element(By.CSS_SELECTOR, '.oxd-main-menu-item.active').click()
        # driver.find_element(By.CLASS_NAME, 'oxd-userdropdown-name').click()
        # driver.find_element(By.LINK_TEXT, "Logout").click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()