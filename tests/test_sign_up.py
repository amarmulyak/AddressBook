from pages.sign_up_object import SignUpSearchHelper
from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
import pytest
import random
import string
import time


@pytest.mark.skip(reason="We don't have access to DB to clean created user")
class TestSignUp:
    def test_sign_in_link(self, browser_fixture):
        sign_up_page = SignUpSearchHelper(browser_fixture)
        sign_in_page = SignInSearchHelper(browser_fixture)
        sign_up_page.go_to_sign_up_page()
        sign_up_page.click_on_sign_in_link()
        time.sleep(2)
        assert sign_in_page.sign_in_page_header() == "Sign in"

    def test_sign_up(self, browser_fixture):
        sign_up_email = "".join(random.choices(string.ascii_lowercase, k=6)) + "@i.ua"
        sign_up_password = "".join(random.choices(string.ascii_lowercase, k=6))
        sign_up_page = SignUpSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        sign_up_page.go_to_sign_up_page()
        sign_up_page.type_sign_up_email(sign_up_email)
        sign_up_page.type_sign_up_password(sign_up_password)
        sign_up_page.click_sign_up_btn()
        assert sign_up_email in common.navbar_items()
        common.click_sign_out()
