from pages.sign_up_object import SignUpSearchHelper
import random
import string
import pytest


class TestSignUpNegative:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                {"email": "", "password": ""},  # blank email and password
                "Bad email or password.",
            ),
            (
                {
                    "email": "mymail@i.ua",  # existed user and valid password
                    "password": "123456",
                },
                "Bad email or password.",
            ),
            (
                {
                    # new user and blank password
                    "email": "".join(random.choices(string.ascii_lowercase, k=6))
                    + "@i.ua",
                    "password": "",
                },
                "Bad email or password.",
            ),
            (
                {"email": "", "password": "123456"},  # blank email with valid password
                "Bad email or password.",
            ),
        ],
    )
    def test_sign_up_invalid_email_password(
        self, browser_fixture, data_fixture_js, test_input, expected
    ):
        sign_up_email = test_input["email"]
        sign_up_password = test_input["password"]
        sign_up_page = SignUpSearchHelper(browser_fixture)
        sign_up_page.go_to_sign_up_page()
        sign_up_page.provide_sign_up_credentials(sign_up_email, sign_up_password)
        sign_up_page.check_usrer_is_not_logged_in(sign_up_email)

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                {"email": "mymaili.ua", "password": "123456"},  # email without @ sign
                "Bad email or password.",
            ),
            (
                {"email": "mymail@i", "password": "123456"},  # email without TLD
                "Bad email or password.",
            ),
            (
                {
                    "email": "mymail@i.",  # email with dot without TLD
                    "password": "123456",
                },
                "Bad email or password.",
            ),
            (
                {"email": "mymaili@.com", "password": "123456"},  # email without TLD
                "Bad email or password.",
            ),
            (
                {"email": "mymaili@", "password": "123456"},  # email without TLD
                "Bad email or password.",
            ),
            (
                {"email": "mymaili", "password": "123456"},  # email without TLD
                "Bad email or password.",
            ),
        ],
    )
    def test_sign_up_bad_email_format(self, browser_fixture, test_input, expected):
        session_email = test_input["email"]
        session_password = test_input["password"]
        sign_up_page = SignUpSearchHelper(browser_fixture)
        sign_up_page.go_to_sign_up_page()
        sign_up_page.provide_sign_up_credentials(session_email, session_password)
        sign_up_page.check_email_field_is_active()
        sign_up_page.check_usrer_is_not_logged_in(session_email)
