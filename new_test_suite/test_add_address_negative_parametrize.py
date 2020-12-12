from pages.addresses_list_object import AddressesListPage
from pages.new_address_object import NewAddressPage
import pytest


class TestAddAddressNegative:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                {
                    "first_name": "",
                    "last_name": "",
                    "address1": "",
                    "city": "",
                    "zip_code": "",
                },
                "5 errors prohibited this address from being saved:"
                "\nFirst name can't be blank"
                "\nLast name can't be blank"
                "\nAddress1 can't be blank"
                "\nCity can't be blank"
                "\nZip code can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "",
                    "address1": "",
                    "city": "",
                    "zip_code": "",
                },
                "4 errors prohibited this address from being saved:"
                "\nLast name can't be blank"
                "\nAddress1 can't be blank"
                "\nCity can't be blank"
                "\nZip code can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "M",
                    "address1": "",
                    "city": "",
                    "zip_code": "",
                },
                "3 errors prohibited this address from being saved:"
                "\nAddress1 can't be blank"
                "\nCity can't be blank"
                "\nZip code can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "M",
                    "address1": "Street",
                    "city": "",
                    "zip_code": "",
                },
                "2 errors prohibited this address from being saved:"
                "\nCity can't be blank"
                "\nZip code can't be blank",
            ),
            (
                {
                    "first_name": "Andrii",
                    "last_name": "M",
                    "address1": "Street",
                    "city": "Lviv",
                    "zip_code": "",
                },
                "1 error prohibited this address from being saved:"
                "\nZip code can't be blank",
            ),
        ],
    )
    def test_error_required_fields_blank(
        self, browser_fixture, log_in_user2, data_fixture_js, test_input, expected
    ):
        addresses_list_page = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)

        addresses_list_page.navigate()
        addresses_list_page.click_new_address_link()
        new_address_page.provide_required_fields(test_input)
        new_address_page.check_required_fields_error(expected)
