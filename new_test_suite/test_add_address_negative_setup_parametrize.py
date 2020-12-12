from pages.sign_in_object import SignInSearchHelper
from pages.addresses_list_object import AddressesListPage
from pages.new_address_object import NewAddressPage
from selenium import webdriver
from conftest import driver_path
import json
import pathlib
import pytest


class TestAddAddressNegative:
    @classmethod
    def setup_class(cls):
        cur_path = pathlib.Path(__file__).parent
        cls.file = open(f"{cur_path}\\..\\test_input_data\\qa.json")
        cls.data = [json.load(cls.file)]
        cls.data_gen = cls.data[0]["address_negative"]
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        session_email = cls.data[0]["session_email2"]
        session_password = cls.data[0]["session_password2"]
        page = SignInSearchHelper(cls.driver)
        cls.addresses_list_page = AddressesListPage(cls.driver)
        cls.new_address_page = NewAddressPage(cls.driver)

        page.go_to_sign_in_page()
        page.provide_credentials(session_email, session_password)

    @classmethod
    def teardown_class(cls):
        cls.file.close()
        cls.driver.quit()

    @pytest.mark.parametrize("permutation", ["p1", "p2"])
    def test_error_required_fields_blank(self, permutation):
        self.addresses_list_page.navigate()
        self.addresses_list_page.click_new_address_link()

        self.new_address_page.provide_required_fields(
            self.data_gen[f"{permutation}"]["test_input"]
        )

        self.new_address_page.check_required_fields_error(
            self.data_gen[f"{permutation}"]["expected"]
        )
