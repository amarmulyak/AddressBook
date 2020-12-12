from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.addresses_list_object import AddressesListPage
from pages.new_address_object import NewAddressPage
from pages.new_address_object import NewAddressLocators as NAL


class TestAddAddressNegative:
    def test_error_required_fields_blank(
        self, browser_fixture, data_fixture_js, data_gen
    ):
        session_email = data_fixture_js["session_email2"]
        session_password = data_fixture_js["session_password2"]
        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)
        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()

        addresses.click_new_address_link()

        new_address_page.set_data_to_field(
            NAL.locator_first_name_field, data_gen["test_input"]["first_name"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_last_name_field, data_gen["test_input"]["last_name"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_address1_field, data_gen["test_input"]["address1"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_city, data_gen["test_input"]["city"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_zip_code, data_gen["test_input"]["zip_code"]
        )

        new_address_page.click_on_element(NAL.locator_create_address_btn)

        error_message = common.get_text_from_element(NAL.locator_required_fields_error)
        assert error_message == data_gen["expected"]

        common.click_sign_out()
