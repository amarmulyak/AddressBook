from pages.sign_in_object import SignInSearchHelper
import pytest
import random
import string


class TestSignInNegative:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                {"email": "", "password": ""},  # blank email and password
                "Bad email or password.",
            ),
            (
                {
                    "email": "mymail@i.ua",  # existed user and blank password
                    "password": "",
                },
                "Bad email or password.",
            ),
            (
                {
                    "email": "mymail@i.ua",  # existed user and incorrect password
                    "password": "111111",
                },
                "Bad email or password.",
            ),
            (
                {"email": "", "password": "123456"},  # blank email with valid password
                "Bad email or password.",
            ),
            (
                {
                    # unregistered user
                    "email": "".join(random.choices(string.ascii_lowercase, k=6))
                    + "@i.ua",
                    "password": "123456",
                },
                "Bad email or password.",
            ),
        ],
    )
    def test_sign_in_invalid_email_password(
        self, browser_fixture, data_fixture_js, test_input, expected
    ):
        session_email = test_input["email"]
        session_password = test_input["password"]
        sign_in_page = SignInSearchHelper(browser_fixture)

        sign_in_page.go_to_sign_in_page()
        sign_in_page.provide_credentials(session_email, session_password)
        sign_in_page.check_error_message(expected)
        sign_in_page.check_usrer_is_not_logged_in(session_email)

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                {"email": "mymaili.ua", "password": "123456"},  # email without @ sign
                "Bad email or password.",
            ),
            pytest.param(
                {"email": "mymail@i", "password": "123456"},  # email without TLD
                "Bad email or password.",
                marks=pytest.mark.xfail
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
    def test_sign_in_bad_email_format(self, browser_fixture, test_input, expected):
        session_email = test_input["email"]
        session_password = test_input["password"]
        sign_in_page = SignInSearchHelper(browser_fixture)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.provide_credentials(session_email, session_password)
        sign_in_page.check_email_field_is_active()
        sign_in_page.check_usrer_is_not_logged_in(session_email)
