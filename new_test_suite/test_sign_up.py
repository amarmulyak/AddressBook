from pages.sign_up_object import SignUpSearchHelper
from pages.sign_in_object import SignInSearchHelper
import pytest
import random
import string


class TestSignUp:
    def test_sign_up_link_header(self, browser_fixture):
        sign_in_page = SignInSearchHelper(browser_fixture)
        sign_up_page = SignUpSearchHelper(browser_fixture)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.click_on_sign_up_link()
        sign_up_page.check_sign_up_header("Sign up")

    @pytest.mark.skip(reason="We don't have access to DB to clean created user")
    def test_sign_up(self, browser_fixture):
        sign_up_email = "".join(random.choices(string.ascii_lowercase, k=6)) + "@i.ua"
        sign_up_password = "".join(random.choices(string.ascii_lowercase, k=6))
        sign_up_page = SignUpSearchHelper(browser_fixture)

        sign_up_page.go_to_sign_up_page()
        sign_up_page.provide_sign_up_credentials(sign_up_email, sign_up_password)
        sign_up_page.check_usrer_is_logged_in(sign_up_email)
