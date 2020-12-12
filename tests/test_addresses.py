from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.addresses_list_object import AddressesListLocators as ALL
from pages.addresses_list_object import AddressesListPage
from pages.new_address_object import NewAddressLocators as NAL
from pages.new_address_object import NewAddressPage
from pages.show_address_object import ShowAddressesLocators as SAL
from pages.show_address_object import ShowAddressPage
from pages.edit_address_object import EditAddressesLocators as EAL
from pages.edit_address_object import EditAddressPage
from pages.new_address_object import Converters


class TestAddAddress:
    def test_add_address(self, browser_fixture, data_fixture_js):
        session_email = data_fixture_js["session_email2"]
        session_password = data_fixture_js["session_password2"]

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses_list_page = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)
        show_address_page = ShowAddressPage(browser_fixture)
        converter = Converters()

        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()

        addresses_list_page.click_new_address_link()

        new_address_page.set_data_to_field(
            NAL.locator_first_name_field,
            data_fixture_js["dict_add_address"]["First name:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_last_name_field,
            data_fixture_js["dict_add_address"]["Last name:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address1_field,
            data_fixture_js["dict_add_address"]["Street Address:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address2_field,
            data_fixture_js["dict_add_address"]["Secondary Address:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_city, data_fixture_js["dict_add_address"]["City:"]
        )

        new_address_page.select_dropdown_option(
            NAL.locator_state, data_fixture_js["dict_add_address"]["State:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_zip_code, data_fixture_js["dict_add_address"]["Zip code:"]
        )

        new_address_page.select_state(data_fixture_js["dict_add_address"]["Country:"])

        new_address_page.set_data_to_field(
            NAL.locator_birthday,
            converter.date_converter(data_fixture_js["dict_add_address"]["Birthday:"]),
        )

        new_address_page.set_data_to_field(
            NAL.locator_color,
            converter.rgb_to_hex(data_fixture_js["dict_add_address"]["Color:"]),
        )

        new_address_page.set_data_to_field(
            NAL.locator_age, data_fixture_js["dict_add_address"]["Age:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_website, data_fixture_js["dict_add_address"]["Website:"]
        )

        new_address_page.find_element(NAL.locator_picture).send_keys("C:\\123.png")

        new_address_page.set_data_to_field(
            NAL.locator_phone, data_fixture_js["dict_add_address"]["Phone:"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_climbing, data_fixture_js["dict_add_address"]["Climbing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_dancing, data_fixture_js["dict_add_address"]["Dancing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_reading, data_fixture_js["dict_add_address"]["Reading?"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_note, data_fixture_js["dict_add_address"]["Note:"]
        )

        new_address_page.click_create_address_btn()

        dict_results = show_address_page.get_results_shown()

        assert (
            show_address_page.find_element(SAL.locator_result_container).text.split(
                "\n"
            )[0]
            == "Address was successfully created."
        )

        assert data_fixture_js["dict_add_address"] == dict_results

        show_address_page.click_list_link()

        addresses_list_page.click_destroy_link()

        addresses_list_page.click_ok_on_alert()

        common.click_sign_out()


class TestShowAddress:
    def test_show_address(self, browser_fixture, data_fixture_js):
        session_email = data_fixture_js["session_email2"]
        session_password = data_fixture_js["session_password2"]

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses_list_page = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)
        show_address_page = ShowAddressPage(browser_fixture)
        converter = Converters()

        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()

        addresses_list_page.click_new_address_link()

        new_address_page.set_data_to_field(
            NAL.locator_first_name_field,
            data_fixture_js["dict_add_address"]["First name:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_last_name_field,
            data_fixture_js["dict_add_address"]["Last name:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address1_field,
            data_fixture_js["dict_add_address"]["Street Address:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address2_field,
            data_fixture_js["dict_add_address"]["Secondary Address:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_city, data_fixture_js["dict_add_address"]["City:"]
        )

        new_address_page.select_dropdown_option(
            NAL.locator_state, data_fixture_js["dict_add_address"]["State:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_zip_code, data_fixture_js["dict_add_address"]["Zip code:"]
        )

        new_address_page.select_state(data_fixture_js["dict_add_address"]["Country:"])

        new_address_page.set_data_to_field(
            NAL.locator_birthday,
            converter.date_converter(data_fixture_js["dict_add_address"]["Birthday:"]),
        )

        new_address_page.set_data_to_field(
            NAL.locator_color,
            converter.rgb_to_hex(data_fixture_js["dict_add_address"]["Color:"]),
        )

        new_address_page.set_data_to_field(
            NAL.locator_age, data_fixture_js["dict_add_address"]["Age:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_website, data_fixture_js["dict_add_address"]["Website:"]
        )

        new_address_page.find_element(NAL.locator_picture).send_keys("C:\\123.png")

        new_address_page.set_data_to_field(
            NAL.locator_phone, data_fixture_js["dict_add_address"]["Phone:"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_climbing, data_fixture_js["dict_add_address"]["Climbing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_dancing, data_fixture_js["dict_add_address"]["Dancing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_reading, data_fixture_js["dict_add_address"]["Reading?"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_note, data_fixture_js["dict_add_address"]["Note:"]
        )

        new_address_page.click_create_address_btn()

        show_address_page.click_list_link()

        addresses_list_page.click_show_address_link()

        dict_results = show_address_page.get_results_shown()

        assert data_fixture_js["dict_add_address"] == dict_results

        show_address_page.click_list_link()

        addresses_list_page.click_destroy_link()

        addresses_list_page.click_ok_on_alert()

        common.click_sign_out()


class TestEditAddress:
    def test_edit_addresses(self, browser_fixture, data_fixture_js):
        session_email = data_fixture_js["session_email2"]
        session_password = data_fixture_js["session_password2"]

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses_list_page = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)
        show_address_page = ShowAddressPage(browser_fixture)
        edit_address_page = EditAddressPage(browser_fixture)
        converter = Converters()

        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()

        addresses_list_page.click_new_address_link()

        new_address_page.set_data_to_field(
            NAL.locator_first_name_field,
            data_fixture_js["dict_add_address"]["First name:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_last_name_field,
            data_fixture_js["dict_add_address"]["Last name:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address1_field,
            data_fixture_js["dict_add_address"]["Street Address:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address2_field,
            data_fixture_js["dict_add_address"]["Secondary Address:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_city, data_fixture_js["dict_add_address"]["City:"]
        )

        new_address_page.select_dropdown_option(
            NAL.locator_state, data_fixture_js["dict_add_address"]["State:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_zip_code, data_fixture_js["dict_add_address"]["Zip code:"]
        )

        new_address_page.select_state(data_fixture_js["dict_add_address"]["Country:"])

        new_address_page.set_data_to_field(
            NAL.locator_birthday,
            converter.date_converter(data_fixture_js["dict_add_address"]["Birthday:"]),
        )

        new_address_page.set_data_to_field(
            NAL.locator_color,
            converter.rgb_to_hex(data_fixture_js["dict_add_address"]["Color:"]),
        )

        new_address_page.set_data_to_field(
            NAL.locator_age, data_fixture_js["dict_add_address"]["Age:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_website, data_fixture_js["dict_add_address"]["Website:"]
        )

        new_address_page.find_element(NAL.locator_picture).send_keys("C:\\123.png")

        new_address_page.set_data_to_field(
            NAL.locator_phone, data_fixture_js["dict_add_address"]["Phone:"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_climbing, data_fixture_js["dict_add_address"]["Climbing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_dancing, data_fixture_js["dict_add_address"]["Dancing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_reading, data_fixture_js["dict_add_address"]["Reading?"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_note, data_fixture_js["dict_add_address"]["Note:"]
        )

        new_address_page.click_create_address_btn()

        show_address_page.click_list_link()

        addresses_list_page.click_edit_link()

        edit_address_page.clean_field(EAL.locator_first_name_field)
        edit_address_page.clean_field(EAL.locator_last_name_field)
        edit_address_page.clean_field(EAL.locator_address1_field)
        edit_address_page.clean_field(EAL.locator_address2_field)
        edit_address_page.clean_field(EAL.locator_city)
        edit_address_page.clean_field(EAL.locator_zip_code)
        edit_address_page.clean_field(EAL.locator_age)
        edit_address_page.clean_field(EAL.locator_website)
        edit_address_page.clean_field(EAL.locator_phone)
        edit_address_page.clean_field(EAL.locator_note)

        edit_address_page.set_data_to_field(
            EAL.locator_first_name_field,
            data_fixture_js["dict_edit_address"]["First name:"],
        )

        edit_address_page.set_data_to_field(
            EAL.locator_last_name_field,
            data_fixture_js["dict_edit_address"]["Last name:"],
        )

        edit_address_page.set_data_to_field(
            EAL.locator_address1_field,
            data_fixture_js["dict_edit_address"]["Street Address:"],
        )

        edit_address_page.set_data_to_field(
            EAL.locator_address2_field,
            data_fixture_js["dict_edit_address"]["Secondary Address:"],
        )

        edit_address_page.set_data_to_field(
            EAL.locator_city, data_fixture_js["dict_edit_address"]["City:"]
        )

        edit_address_page.select_dropdown_option(
            EAL.locator_state, data_fixture_js["dict_edit_address"]["State:"]
        )

        edit_address_page.set_data_to_field(
            EAL.locator_zip_code, data_fixture_js["dict_edit_address"]["Zip code:"]
        )

        edit_address_page.select_state(data_fixture_js["dict_edit_address"]["Country:"])

        edit_address_page.set_data_to_field(
            EAL.locator_birthday,
            converter.date_converter(data_fixture_js["dict_edit_address"]["Birthday:"]),
        )

        edit_address_page.set_data_to_field(
            EAL.locator_color,
            converter.rgb_to_hex(data_fixture_js["dict_edit_address"]["Color:"]),
        )

        edit_address_page.set_data_to_field(
            EAL.locator_age, data_fixture_js["dict_edit_address"]["Age:"]
        )

        edit_address_page.set_data_to_field(
            EAL.locator_website, data_fixture_js["dict_edit_address"]["Website:"]
        )

        # addresses.find_element_by_locator(AL.locator_picture).send_keys("C:\\123.png")

        edit_address_page.set_data_to_field(
            EAL.locator_phone, data_fixture_js["dict_edit_address"]["Phone:"]
        )

        edit_address_page.click_on_element_if_yes(
            EAL.locator_climbing, data_fixture_js["dict_edit_address"]["Climbing?"]
        )

        edit_address_page.click_on_element_if_yes(
            EAL.locator_dancing, data_fixture_js["dict_edit_address"]["Dancing?"]
        )

        edit_address_page.click_on_element_if_yes(
            EAL.locator_reading, data_fixture_js["dict_edit_address"]["Reading?"]
        )

        edit_address_page.set_data_to_field(
            EAL.locator_note, data_fixture_js["dict_edit_address"]["Note:"]
        )

        edit_address_page.click_update_address_btn()

        dict_results = show_address_page.get_results_shown()

        assert (
            show_address_page.find_element(SAL.locator_result_container).text.split(
                "\n"
            )[0]
            == "Address was successfully updated."
        )

        assert data_fixture_js["dict_edit_address"] == dict_results

        show_address_page.click_list_link()

        addresses_list_page.click_destroy_link()

        addresses_list_page.click_ok_on_alert()

        common.click_sign_out()


class TestDestroyAddress:
    def test_destroy_address(self, browser_fixture, data_fixture_js):
        session_email = data_fixture_js["session_email2"]
        session_password = data_fixture_js["session_password2"]

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses_list_page = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)
        show_address_page = ShowAddressPage(browser_fixture)
        converter = Converters()

        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()

        addresses_list_page.click_new_address_link()

        new_address_page.set_data_to_field(
            NAL.locator_first_name_field,
            data_fixture_js["dict_add_address"]["First name:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_last_name_field,
            data_fixture_js["dict_add_address"]["Last name:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address1_field,
            data_fixture_js["dict_add_address"]["Street Address:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address2_field,
            data_fixture_js["dict_add_address"]["Secondary Address:"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_city, data_fixture_js["dict_add_address"]["City:"]
        )

        new_address_page.select_dropdown_option(
            NAL.locator_state, data_fixture_js["dict_add_address"]["State:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_zip_code, data_fixture_js["dict_add_address"]["Zip code:"]
        )

        new_address_page.select_state(data_fixture_js["dict_add_address"]["Country:"])

        new_address_page.set_data_to_field(
            NAL.locator_birthday,
            converter.date_converter(data_fixture_js["dict_add_address"]["Birthday:"]),
        )

        new_address_page.set_data_to_field(
            NAL.locator_color,
            converter.rgb_to_hex(data_fixture_js["dict_add_address"]["Color:"]),
        )

        new_address_page.set_data_to_field(
            NAL.locator_age, data_fixture_js["dict_add_address"]["Age:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_website, data_fixture_js["dict_add_address"]["Website:"]
        )

        new_address_page.find_element(NAL.locator_picture).send_keys("C:\\123.png")

        new_address_page.set_data_to_field(
            NAL.locator_phone, data_fixture_js["dict_add_address"]["Phone:"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_climbing, data_fixture_js["dict_add_address"]["Climbing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_dancing, data_fixture_js["dict_add_address"]["Dancing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_reading, data_fixture_js["dict_add_address"]["Reading?"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_note, data_fixture_js["dict_add_address"]["Note:"]
        )

        new_address_page.click_create_address_btn()

        show_address_page.click_list_link()

        addresses_list_page.click_destroy_link()

        addresses_list_page.click_ok_on_alert()

        assert (
            addresses_list_page.find_element(ALL.locator_destroyed_message).text
            == "Address was successfully destroyed."
        )

        common.click_sign_out()
