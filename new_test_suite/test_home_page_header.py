from pages.home_page import HomePageSearchHelper


class TestHomePage:
    def test_home_page_header(self, browser_fixture):
        home_page = HomePageSearchHelper(browser_fixture)
        home_page.go_to_home_page()
        home_page.check_home_page_header(
            "Welcome to Address Book\n\nA simple web app for showing off your testing"
        )
