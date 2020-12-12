from pages.addresses_list_object import AddressesListPage
from pages.edit_address_object import EditAddressPage
import pytest


class TestEditAddressNegative:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                {
                    "First name:": "",
                    "Last name:": "Marm",
                    "Street Address:": "Street",
                    "City:": "Lviv",
                    "Zip code:": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nFirst name can't be blank",
            ),
            (
                {
                    "First name:": "Andrii",
                    "Last name:": "",
                    "Street Address:": "Street",
                    "City:": "Lviv",
                    "Zip code:": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nLast name can't be blank",
            ),
            (
                {
                    "First name:": "Andrii",
                    "Last name:": "Marm",
                    "Street Address:": "",
                    "City:": "Lviv",
                    "Zip code:": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nAddress1 can't be blank",
            ),
            (
                {
                    "First name:": "Andrii",
                    "Last name:": "Marm",
                    "Street Address:": "",
                    "City:": "Lviv",
                    "Zip code:": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nAddress1 can't be blank",
            ),
            (
                {
                    "First name:": "Andrii",
                    "Last name:": "Marm",
                    "Street Address:": "Street",
                    "City:": "",
                    "Zip code:": "79000",
                },
                "1 error prohibited this address from being saved:"
                "\nCity can't be blank",
            ),
            (
                {
                    "First name:": "Andrii",
                    "Last name:": "Marm",
                    "Street Address:": "Street",
                    "City:": "Lviv",
                    "Zip code:": "",
                },
                "1 error prohibited this address from being saved:"
                "\nZip code can't be blank",
            ),
        ],
    )
    def test_edit_address_negative(
        self,
        browser_fixture,
        add_address_fixture,
        data_fixture_js,
        test_input,
        expected,
    ):
        addresses_list_page = AddressesListPage(browser_fixture)
        edit_address_page = EditAddressPage(browser_fixture)

        addresses_list_page.navigate()
        addresses_list_page.click_edit_created_address(add_address_fixture)
        edit_address_page.provide_required_fields(test_input)
        edit_address_page.check_required_fields_error(expected)
