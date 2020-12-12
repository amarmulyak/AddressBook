from base.base_page import BasePage
from selenium.webdriver.common.by import By


class ShowAddressesLocators:
    locator_list_link = (By.LINK_TEXT, "List")
    locator_edit_address_link = (By.LINK_TEXT, "Edit")
    locator_result_container = (By.CLASS_NAME, "container")
    locator_container_options = (By.XPATH, "//p")


class ShowAddressPage(BasePage):
    def click_list_link(self):
        self.wait_until_text_in_element((By.LINK_TEXT, "List"), "List")

        list_link = self.driver.find_element(By.LINK_TEXT, "List")

        list_link.click()

        self.find_element(
            (By.TAG_NAME, "h2"),
        )

    def get_results_shown(self):
        dict_results = {}

        self.find_element((By.CLASS_NAME, "container"))

        self.find_elements((By.XPATH, "//p"))

        self.wait_until_text_in_element((By.LINK_TEXT, "List"), "List")

        self.wait_until_text_in_element((By.LINK_TEXT, "Edit"), "Edit")

        results = self.driver.find_elements(By.XPATH, "//p")

        for element in results:
            key = element.find_element_by_xpath(".//span[1]").text
            value = element.find_element_by_xpath(".//span[2]").text
            if key == "Color:":
                value = element.find_element_by_xpath(".//span[2]")
                value = value.get_attribute("style").split("rgb")[1].rstrip(";")
            dict_results[key] = value

        return dict_results

    def check_results_shown(self, address_json):
        dict_results = self.get_results_shown()
        assert address_json == dict_results

    def check_success_message(self, message):
        assert (
            self.find_element(
                ShowAddressesLocators.locator_result_container
            ).text.split("\n")[0]
            == message
        )
