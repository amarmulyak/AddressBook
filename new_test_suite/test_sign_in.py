import pytest
from pages.sign_in_object import SignInSearchHelper
from pages.sign_up_object import SignUpSearchHelper


class TestSignInPage:
    @pytest.mark.flaky(reruns=5)
    def test_sign_in_link_header(self, browser_fixture):
        sign_up_page = SignUpSearchHelper(browser_fixture)
        sign_in_page = SignInSearchHelper(browser_fixture)
        sign_up_page.go_to_sign_up_page()
        sign_up_page.click_on_sign_in_link()
        sign_in_page.check_sign_in_header("Sign in")

    def test_sign_in(self, browser_fixture, log_in_user2, data_fixture_js):
        sign_in_page = SignInSearchHelper(browser_fixture)
        sign_in_page.check_usrer_is_logged_in(log_in_user2)


class TestSignOut:
    def test_sign_out(self, browser_fixture, log_in_user1, data_fixture_js):
        sign_in_page = SignInSearchHelper(browser_fixture)
        sign_in_page.click_sign_out()
        sign_in_page.check_usrer_is_not_logged_in(log_in_user1)
