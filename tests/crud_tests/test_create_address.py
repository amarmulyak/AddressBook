from pages.show_address_object import ShowAddressPage
from pages.addresses_list_object import AddressesListPage


class TestCreateAddress:
    def test_create_address(
        self, add_address_fixture, browser_fixture, data_fixture_js
    ):
        show_address_page = ShowAddressPage(browser_fixture)
        show_address_page.check_success_message("Address was successfully created.")
        show_address_page.check_results_shown(data_fixture_js["dict_add_address"])


class TestShowAddress:
    def test_show_address(
        self, add_address_fixture, browser_fixture, data_fixture_js
    ):
        show_address_page = ShowAddressPage(browser_fixture)
        address_list_page = AddressesListPage(browser_fixture)
        address_list_page.navigate()
        address_list_page.click_show_created_address(add_address_fixture)
        show_address_page.check_results_shown(data_fixture_js["dict_add_address"])
