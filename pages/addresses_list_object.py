from base.base_page import BasePage
from selenium.webdriver.common.by import By


class AddressesListLocators:
    locator_new_address_link = (By.LINK_TEXT, "New Address")
    locator_show_address_link = (By.LINK_TEXT, "Show")
    locator_edit_address_link = (By.LINK_TEXT, "Edit")
    locator_destroy_address_link = (By.LINK_TEXT, "Destroy")
    locator_destroyed_message = (By.XPATH, "/html/body/div/div")
    locator_create_update_address_btn = (By.NAME, "commit")
    locator_addresses_page_header = (By.TAG_NAME, "h2")


class AddressesListPage(BasePage):
    def navigate(self):
        self.driver.get(self.base_url + "addresses")

    def click_new_address_link(self):
        self.wait_until_text_in_element((By.LINK_TEXT, "New Address"), "New Address")

        new_address_link = self.driver.find_element(By.LINK_TEXT, "New Address")

        new_address_link.click()

        self.wait_until_text_in_element((By.TAG_NAME, "h2"), "New Address")

    def click_show_address_link(self):
        self.wait_until_text_in_element((By.LINK_TEXT, "Show"), "Show")

        show_link = self.driver.find_element(By.LINK_TEXT, "Show")

        show_link.click()

        self.wait_until_text_in_element((By.LINK_TEXT, "List"), "List")

    def click_edit_link(self):
        self.wait_until_text_in_element((By.LINK_TEXT, "Edit"), "Edit")

        edit_link = self.driver.find_element(By.LINK_TEXT, "Edit")

        edit_link.click()

        self.wait_until_text_in_element((By.TAG_NAME, "h2"), "Editing Address")

    def click_destroy_link(self):
        self.find_element((By.XPATH, "//tr"))

        self.find_elements((By.XPATH, "//td"))

        self.wait_until_text_in_element((By.LINK_TEXT, "Show"), "Show")

        self.wait_until_text_in_element((By.LINK_TEXT, "Edit"), "Edit")

        destroy_link = self.driver.find_element(By.LINK_TEXT, "Destroy")

        destroy_link.click()

        self.wait_until_alert_appear()

    def click_ok_on_alert(self):
        self.wait_until_alert_appear()

        popup = self.driver.switch_to.alert

        popup.accept()

        self.wait_until_alert_disappear()

        self.wait_until_text_in_element((By.LINK_TEXT, "New Address"), "New Address")

        self.wait_until_visible((By.CLASS_NAME, "table"))

    def click_address_navigation_link(self, navigator, new_address_url):
        self.click_on_element(
            (
                By.XPATH,
                f"//*[contains(@data-test, '{navigator}') and contains(@href,'{new_address_url}')]",
            )
        )

    def click_show_created_address(self, new_address_url):
        self.click_address_navigation_link("show", new_address_url)

    def click_edit_created_address(self, new_address_url):
        self.click_address_navigation_link("edit", new_address_url)

    def destroy_created_address(self, new_address_url):
        self.click_address_navigation_link("destroy", new_address_url)
        self.click_ok_on_alert()

    def check_destroyed_message(self, message):
        assert (
            self.find_element(AddressesListLocators.locator_destroyed_message).text
            == message
        )
