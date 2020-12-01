from pages.show_address_object import ShowAddressPage
from pages.addresses_list_object import AddressesListPage
from pages.edit_address_object import EditAddressPage
from pages.common_objects import CommonSearchHelper
from pages.new_address_object import NewAddressPage


class TestCreateAddress:
    def test_create_address(
        self, add_address_fixture, browser_fixture, data_fixture_js
    ):
        show_address_page = ShowAddressPage(browser_fixture)
        show_address_page.check_success_message("Address was successfully created.")
        show_address_page.check_results_shown(data_fixture_js["dict_add_address"])


class TestShowAddress:
    def test_show_address(self, add_address_fixture, browser_fixture, data_fixture_js):
        show_address_page = ShowAddressPage(browser_fixture)
        address_list_page = AddressesListPage(browser_fixture)
        address_list_page.navigate()
        address_list_page.click_show_created_address(add_address_fixture)
        show_address_page.check_results_shown(data_fixture_js["dict_add_address"])


class TestEditAddress:
    def test_edit_address(self, add_address_fixture, browser_fixture, data_fixture_js):
        show_address_page = ShowAddressPage(browser_fixture)
        address_list_page = AddressesListPage(browser_fixture)
        edit_address_page = EditAddressPage(browser_fixture)
        address_list_page.navigate()
        address_list_page.click_edit_created_address(add_address_fixture)
        edit_address_page.edit_address(data_fixture_js)
        show_address_page.check_success_message("Address was successfully updated.")
        show_address_page.check_results_shown(data_fixture_js["dict_edit_address"])


class TestDestroyAddress:
    def test_destroy_address(self, add_address_fixture, browser_fixture):
        address_list_page = AddressesListPage(browser_fixture)
        address_list_page.navigate()
        address_list_page.destroy_created_address(add_address_fixture)
        address_list_page.check_destroyed_message("Address was successfully destroyed.")


class TestAddAddressNegative:
    def test_error_required_fields_blank(
            self,
            log_in,
            browser_fixture,
            data_gen
    ):
        addresses = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)

        addresses.navigate()
        addresses.click_new_address_link()
        new_address_page.provide_required_fields(data_gen)
        new_address_page.check_required_fields_error(data_gen["expected"])