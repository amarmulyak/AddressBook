from pages.home_page import HomePageSearchHelper


class TestHomePage:
    def test_home_page_header(self, browser_fixture):
        address_main_page = HomePageSearchHelper(browser_fixture)
        address_main_page.go_to_home_page()
        assert (
            address_main_page.home_page_header() == "Welcome to Address Book"
            "\n\nA simple web app for showing off your testing"
        )
