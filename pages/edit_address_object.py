from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.new_address_object import Converters
import platform


class EditAddressesLocators:
    locator_list_link = (By.LINK_TEXT, "List")
    locator_show_address_link = (By.LINK_TEXT, "Show")
    locator_first_name_field = (By.NAME, "address[first_name]")
    locator_last_name_field = (By.NAME, "address[last_name]")
    locator_address1_field = (By.NAME, "address[address1]")
    locator_address2_field = (By.NAME, "address[address2]")
    locator_city = (By.NAME, "address[city]")
    locator_state = (By.NAME, "address[state]")
    locator_zip_code = (By.NAME, "address[zip_code]")
    locator_address_country_us = (By.ID, "address_country_us")
    locator_address_country_canada = (By.ID, "address_country_canada")
    locator_address_state = (By.XPATH, '/*[@id="new_address"]/div[8]')
    locator_birthday = (By.NAME, "address[birthday]")
    locator_color = (By.NAME, "address[color]")
    locator_age = (By.NAME, "address[age]")
    locator_website = (By.NAME, "address[website]")
    locator_picture = (By.ID, "address_picture")
    locator_phone = (By.NAME, "address[phone]")
    locator_climbing = (By.ID, "address_interest_climb")
    locator_dancing = (By.ID, "address_interest_dance")
    locator_reading = (By.ID, "address_interest_read")
    locator_note = (By.ID, "address_note")
    locator_update_address_btn = (By.NAME, "commit")
    locator_required_fields_error = (By.XPATH, ".//div[@id = 'error_explanation']")


class EditAddressPage(BasePage):
    def click_on_element_if_yes(self, locator, option):
        element = self.find_element(locator)
        if option == "Yes":
            return element.click()
        elif option == "No":
            element.get_attribute("checked")
            if element.get_attribute("checked"):
                element.click()
            else:
                pass
        else:
            raise Exception("Provide 'Yes' or 'No'")

    def set_data_to_field(self, field_locator, data):
        return self.find_element(field_locator, time=2).send_keys(data)

    def select_dropdown_option(self, dropdown_locator, value):
        dropdown = Select(self.find_element(dropdown_locator, time=2))
        return dropdown.select_by_value(value)

    def select_element_by_locator(self, locator):
        element = Select(self.find_element(locator))
        return element

    def select_state(self, state):
        if state == "us":
            self.click_on_element(EditAddressesLocators.locator_address_country_us)
        elif state == "canada":
            self.click_on_element(EditAddressesLocators.locator_address_country_canada)
        else:
            pass

    def clean_field(self, locator):
        return self.find_element(locator).clear()

    def clean_fields(self, locators_list):
        for locator in locators_list:
            self.clean_field(locator)

    def click_update_address_btn(self):
        self.wait_until_element_clickable((By.NAME, "commit"))

        update_address_btn = self.driver.find_element(By.NAME, "commit")

        update_address_btn.click()

        self.find_element((By.CLASS_NAME, "container"))

    def edit_address(self, data_json):
        converter = Converters()
        self.clean_fields(
            [
                EditAddressesLocators.locator_first_name_field,
                EditAddressesLocators.locator_last_name_field,
                EditAddressesLocators.locator_address1_field,
                EditAddressesLocators.locator_address2_field,
                EditAddressesLocators.locator_city,
                EditAddressesLocators.locator_zip_code,
                EditAddressesLocators.locator_age,
                EditAddressesLocators.locator_website,
                EditAddressesLocators.locator_phone,
                EditAddressesLocators.locator_note,
            ]
        )

        self.set_data_to_field(
            EditAddressesLocators.locator_first_name_field, data_json["First name:"]
        )

        self.set_data_to_field(
            EditAddressesLocators.locator_last_name_field, data_json["Last name:"]
        )

        self.set_data_to_field(
            EditAddressesLocators.locator_address1_field, data_json["Street Address:"]
        )

        self.set_data_to_field(
            EditAddressesLocators.locator_address2_field,
            data_json["Secondary Address:"],
        )

        self.set_data_to_field(EditAddressesLocators.locator_city, data_json["City:"])

        self.select_dropdown_option(
            EditAddressesLocators.locator_state, data_json["State:"]
        )

        self.set_data_to_field(
            EditAddressesLocators.locator_zip_code, data_json["Zip code:"]
        )

        self.select_state(data_json["Country:"])

        if platform.system() == "Linux":
            self.set_data_to_field(
                EditAddressesLocators.locator_birthday, data_json["Birthday:"]
            )
        else:
            self.set_data_to_field(
                EditAddressesLocators.locator_birthday,
                converter.date_converter(data_json["Birthday:"]),
            )

        self.set_data_to_field(
            EditAddressesLocators.locator_color,
            converter.rgb_to_hex(data_json["Color:"]),
        )

        self.set_data_to_field(EditAddressesLocators.locator_age, data_json["Age:"])

        self.set_data_to_field(
            EditAddressesLocators.locator_website, data_json["Website:"]
        )

        self.set_data_to_field(EditAddressesLocators.locator_phone, data_json["Phone:"])

        self.click_on_element_if_yes(
            EditAddressesLocators.locator_climbing, data_json["Climbing?"]
        )

        self.click_on_element_if_yes(
            EditAddressesLocators.locator_dancing, data_json["Dancing?"]
        )

        self.click_on_element_if_yes(
            EditAddressesLocators.locator_reading, data_json["Reading?"]
        )

        self.set_data_to_field(EditAddressesLocators.locator_note, data_json["Note:"])

        self.click_update_address_btn()

    def check_required_fields_error(self, message):
        error_message = self.get_text_from_element(
            EditAddressesLocators.locator_required_fields_error
        )
        assert error_message == message

    def provide_required_fields(self, data_json):
        self.clean_fields(
            [
                EditAddressesLocators.locator_first_name_field,
                EditAddressesLocators.locator_last_name_field,
                EditAddressesLocators.locator_address1_field,
                EditAddressesLocators.locator_address2_field,
                EditAddressesLocators.locator_city,
                EditAddressesLocators.locator_zip_code,
                EditAddressesLocators.locator_age,
                EditAddressesLocators.locator_website,
                EditAddressesLocators.locator_phone,
                EditAddressesLocators.locator_note,
            ]
        )

        self.set_data_to_field(
            EditAddressesLocators.locator_first_name_field, data_json["First name:"]
        )

        self.set_data_to_field(
            EditAddressesLocators.locator_last_name_field, data_json["Last name:"]
        )

        self.set_data_to_field(
            EditAddressesLocators.locator_address1_field, data_json["Street Address:"]
        )

        self.set_data_to_field(EditAddressesLocators.locator_city, data_json["City:"])

        self.set_data_to_field(
            EditAddressesLocators.locator_zip_code, data_json["Zip code:"]
        )

        self.click_on_element(EditAddressesLocators.locator_update_address_btn)
