from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import (AddressesLocators as AL,
                                   AddressesSearchHelper)
# from selenium import webdriver
#
# driver = webdriver.Chrome(
#         executable_path="C:\\Users\\Andrii\\PycharmProjects\\"
#                         "testaddressbook\\chromedriver.exe")

first_name = "Andrii"
last_name = "AQA"
address1 = "Street"
address2 = "Street2"



def test_add_address(browser_fixture):
    session_email = "andrii1@i.ua"
    session_password = "123456"
    page = SignInSearchHelper(browser_fixture)
    common = CommonSearchHelper(browser_fixture)  # is it correct
    addresses = AddressesSearchHelper(browser_fixture)
    page.go_to_sign_in_page()
    page.type_sign_in_email(session_email)
    page.type_sign_in_password(session_password)
    page.click_sign_in_btn()
    common.click_addresses()
    addresses.click_on_element(AL.locator_new_address_link)
    addresses.set_data_to_field(AL.locator_first_name_field, first_name)
    addresses.set_data_to_field(AL.locator_last_name_field, last_name)
    addresses.set_data_to_field(AL.locator_address1_field, address1)
    addresses.set_data_to_field(AL.locator_address2_field, address2)
    addresses.set_data_to_field(AL.locator_city, "Lviv")
    addresses.select_dropdown_option(AL.locator_state, "Alaska")
    addresses.set_data_to_field(AL.locator_zip_code, "79000")
    addresses.click_on_element(AL.locator_address_country_us)
    addresses.set_data_to_field(AL.locator_birthday, "11.06.1985")
    addresses.set_data_to_field(AL.locator_color, "#00FF33")
    addresses.set_data_to_field(AL.locator_age, "35")
    addresses.set_data_to_field(AL.locator_website, "https://www.site.com")
    addresses.find_element_by_locator(AL.locator_picture).send_keys("C:\\123.png")
    addresses.set_data_to_field(AL.locator_phone, "123456")
    addresses.click_on_element(AL.locator_climbing)
    addresses.click_on_element(AL.locator_dancing)
    addresses.click_on_element(AL.locator_reading)
    addresses.set_data_to_field(AL.locator_note, "Test note")
    addresses.click_on_element(AL.locator_create_address_btn)
    container = addresses.find_element_by_locator(AL.locator_result_container)
    options = container.text.split('\n')
    # for option

    breakpoint()



