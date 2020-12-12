from pages.addresses_list_object import AddressesListPage
from pages.new_address_object import NewAddressPage


class TestAddAddressNegative:
    def test_error_required_fields_blank(self, log_in_user2, browser_fixture, data_gen):
        addresses = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)

        addresses.navigate()
        addresses.click_new_address_link()
        new_address_page.provide_required_fields(data_gen["test_input"])
        new_address_page.check_required_fields_error(data_gen["expected"])
