from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.admin_link_selector = '.oxd-main-menu-item.active'
        self.menu_icon_class = 'oxd-userdropdown-name'
        self.logout_link_linkText = 'Logout'

    def click_admin_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.admin_link_selector).click()

    def click_menu_icon(self):
        self.driver.find_element(By.CLASS_NAME, self.menu_icon_class).click()

    def click_logout_link(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()

