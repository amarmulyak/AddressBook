from selenium.common.exceptions import TimeoutException
from pages.sign_up_object import SignUpSearchHelper
from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.addresses_list_object import AddressesListPage
from pages.new_address_object import NewAddressPage
from pages.new_address_object import NewAddressLocators as NAL
from pages.show_address_object import ShowAddressPage
from pages.new_address_object import Converters
import platform
import requests


class TestHelper:
    class CreateUser:
        def create_user(self, browser_fixture):
            sign_up_page = SignUpSearchHelper(browser_fixture)
            common = CommonSearchHelper(browser_fixture)
            sign_up_page.go_to_sign_up_page()
            sign_up_page.type_sign_up_email("mymail@i.ua")
            sign_up_page.type_sign_up_password("123456")
            sign_up_page.click_sign_up_btn()
            try:
                common.click_sign_out()
            except TimeoutException:
                pass

    class AddAddress:
        def add_address(self, browser_fixture, data_fixture_js, delete_address):
            session_email = data_fixture_js["session_email2"]
            session_password = data_fixture_js["session_password2"]
            page = SignInSearchHelper(browser_fixture)
            common = CommonSearchHelper(browser_fixture)
            addresses_list_page = AddressesListPage(browser_fixture)
            new_address_page = NewAddressPage(browser_fixture)
            show_address_page = ShowAddressPage(browser_fixture)
            converter = Converters()

            url = f"{page.base_url}session"
            headers_log_in = requests.post(
                url,
                data={
                    "session[email]": f"{session_email}",
                    "session[password]": f"{session_password}",
                },
            )

            build_headers = {"Cookie": f"{headers_log_in.headers['Set-Cookie']}"}

            delete_address["headers"] = build_headers

            page.go_to_sign_in_page()
            try:
                page.type_sign_in_email(session_email)
                page.type_sign_in_password(session_password)
                page.click_sign_in_btn()
            except TimeoutException:
                pass
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

            new_address_page.select_state(
                data_fixture_js["dict_add_address"]["Country:"]
            )

            if platform.system() == "Linux":
                new_address_page.set_data_to_field(
                    NAL.locator_birthday,
                    data_fixture_js["dict_add_address"]["Birthday:"],
                )
            else:
                new_address_page.set_data_to_field(
                    NAL.locator_birthday,
                    converter.date_converter(
                        data_fixture_js["dict_add_address"]["Birthday:"]
                    ),
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

            # new_address_page.find_element(NAL.locator_picture)\
            #     .send_keys("C:\\123.png")

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

            show_address_url = show_address_page.driver.current_url
            delete_address["address"].append(show_address_url)

            return show_address_url.split(addresses_list_page.base_url)[1]

    class LogIn:
        def log_in(self, browser_fixture, session_email, session_password):
            page = SignInSearchHelper(browser_fixture)
            page.go_to_sign_in_page()
            page.type_sign_in_email(session_email)
            page.type_sign_in_password(session_password)
            page.click_sign_in_btn()

            return session_email
