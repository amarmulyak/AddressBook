from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost:3000/"
        # self.base_url = "http://a.testaddressbook.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def wait_until_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Locator {locator} is not visible",
        )

    def wait_until_text_in_element(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Locator {locator} is not visible",
        )

    def wait_until_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Locator {locator} is not clickable",
        )

    def wait_until_alert_appear(self, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.alert_is_present(), message="Alert is not present"
        )

    def wait_until_alert_disappear(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.alert_is_present())

    def click_on_element(self, locator):
        return self.find_element(locator).click()

    def go_to_home_page(self):
        return self.driver.get(self.base_url)

    def go_to_sign_up_page(self):
        return self.driver.get(self.base_url + "sign_up")

    def go_to_sign_in_page(self):
        return self.driver.get(self.base_url + "sign_in")

    def get_text_from_element(self, locator):
        return self.find_element(locator, time=2).text
