from base.base_page import BasePage
from pages.common_objects import CommonSearchHelper
from selenium.webdriver.common.by import By


class SignInLocators:
    locator_sign_in_page_tittle = (By.TAG_NAME, "h2")
    # locator_sign_in_page_tittle = (By.XPATH, "//div[@class='sign-in']")
    locator_sign_in_email_field = (By.ID, "session_email")
    locator_sign_in_pass_field = (By.ID, "session_password")
    locator_sign_in_button = (
        By.XPATH,
        '//*[@id="clearance"]/div/div' "/form/div[3]/input",
    )
    locator_sign_up_link = (By.LINK_TEXT, "Sign up")
    locator_error_message = (By.XPATH, ".//div[@class = 'alert alert-notice']")


class SignInSearchHelper(CommonSearchHelper):
    def sign_in_page_header(self):
        self.wait_until_visible(SignInLocators.locator_sign_in_page_tittle)
        self.wait_until_visible(SignInLocators.locator_sign_in_button)
        return self.find_element(
            SignInLocators.locator_sign_in_page_tittle, time=2
        ).text

    def check_sign_in_header(self, header):
        assert self.sign_in_page_header() == header

    def error_message(self):
        return self.find_element(SignInLocators.locator_error_message, time=5).text

    def type_sign_in_email(self, email):
        self.email_field = self.find_element(
            SignInLocators.locator_sign_in_email_field, time=2
        )
        self.email_field.send_keys(email)
        return self.email_field

    def type_sign_in_password(self, password):
        self.password_field = self.find_element(
            SignInLocators.locator_sign_in_pass_field, time=2
        )
        self.password_field.send_keys(password)
        return self.password_field

    def click_sign_in_btn(self):
        return self.find_element(SignInLocators.locator_sign_in_button, time=2).click()

    def click_on_sign_up_link(self):
        return self.find_element(SignInLocators.locator_sign_up_link, time=2).click()

    def provide_credentials(self, email, password):
        self.type_sign_in_email(email)
        self.type_sign_in_password(password)
        self.click_sign_in_btn()

    def check_error_message(self, message):
        error_message = self.error_message()
        assert error_message == message

    # def check_usrer_is_not_logged_in(self, email):
    #     assert email not in self.navbar_items()

    # def check_email_field_is_active(self):
    #     email_field = self.driver.switch_to_active_element()
    #     placeholder = email_field.get_attribute("placeholder")
    #     assert placeholder == "Email"
