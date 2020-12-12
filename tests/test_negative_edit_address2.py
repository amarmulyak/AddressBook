from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.addresses_list_object import AddressesListPage
from pages.edit_address_object import EditAddressesLocators as EAL
from pages.edit_address_object import EditAddressPage
from pages.show_address_object import ShowAddressPage
from new_test_suite.test_helper import TestHelper
import pytest


class TestEditAddressNegative:
    before_all = False

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                {
                    "first_name": "",
                    "last_name": "Marm",
                    "address1": "Street",
                    "city": "Lviv",
                    "zip_code": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nFirst name can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "",
                    "address1": "Street",
                    "city": "Lviv",
                    "zip_code": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nLast name can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "Marm",
                    "address1": "",
                    "city": "Lviv",
                    "zip_code": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nAddress1 can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "Marm",
                    "address1": "",
                    "city": "Lviv",
                    "zip_code": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nAddress1 can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "Marm",
                    "address1": "Street",
                    "city": "",
                    "zip_code": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nCity can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "Marm",
                    "address1": "Street",
                    "city": "Lviv",
                    "zip_code": "",
                },
                "1 error prohibited this address from being saved:"
                "\nZip code can't be blank",
            ),
        ],
    )
    def test_edit_address_negative(
        self, browser_fixture, data_fixture_js, test_input, expected
    ):
        if not TestEditAddressNegative.before_all:
            before_all = TestHelper()
            before_all.add_address(browser_fixture, data_fixture_js)
            TestEditAddressNegative.before_all = True

        session_email = data_fixture_js["session_email"]
        session_password = data_fixture_js["session_password"]

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses_list_page = AddressesListPage(browser_fixture)
        edit_address_page = EditAddressPage(browser_fixture)
        show_address_page = ShowAddressPage(browser_fixture)

        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()
        addresses_list_page.click_edit_link()

        edit_address_page.clean_field(EAL.locator_first_name_field)
        edit_address_page.clean_field(EAL.locator_last_name_field)
        edit_address_page.clean_field(EAL.locator_address1_field)
        edit_address_page.clean_field(EAL.locator_city)
        edit_address_page.clean_field(EAL.locator_zip_code)

        edit_address_page.set_data_to_field(
            EAL.locator_first_name_field, test_input["first_name"]
        )

        edit_address_page.set_data_to_field(
            EAL.locator_last_name_field, test_input["last_name"]
        )

        edit_address_page.set_data_to_field(
            EAL.locator_address1_field, test_input["address1"]
        )

        edit_address_page.set_data_to_field(EAL.locator_city, test_input["city"])

        edit_address_page.set_data_to_field(
            EAL.locator_zip_code, test_input["zip_code"]
        )

        edit_address_page.click_update_address_btn()

        error_message = common.get_text_from_element(EAL.locator_required_fields_error)

        assert error_message == expected

        common.click_sign_out()
