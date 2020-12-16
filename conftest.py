import pytest
import json
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader
from new_test_suite.test_helper import TestHelper
import pathlib
import requests


def get_driver_path():
    chrome_driver = ChromeDriverDownloader()
    path = chrome_driver.download_and_install()
    return path[0]


driver_path = get_driver_path()


@pytest.fixture(scope="function")
def browser_fixture():
    driver = webdriver.remote.webdriver.WebDriver(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=None, browser_profile=None,
        proxy=None,
        keep_alive=False,
        file_detector=None,
        options=None
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def data_fixture_js():
    cur_path = pathlib.Path(__file__).parent
    json_file = open(f"{cur_path}/test_input_data/qa.json")
    data_from_file = json.load(json_file)
    yield data_from_file
    json_file.close()


@pytest.fixture(scope="function")
def log_in_user2(browser_fixture, data_fixture_js):
    log_in_helper = TestHelper.LogIn()
    email = log_in_helper.log_in(
        browser_fixture,
        data_fixture_js["session_email2"],
        data_fixture_js["session_password2"]
    )
    yield email


@pytest.fixture(scope="function")
def log_in_user1(browser_fixture, data_fixture_js):
    log_in_helper = TestHelper.LogIn()
    email = log_in_helper.log_in(
        browser_fixture,
        data_fixture_js["session_email"],
        data_fixture_js["session_password"]
    )
    yield email


@pytest.fixture(scope="function")
def add_address_fixture(browser_fixture, data_fixture_js, delete_address):
    add_address_helper = TestHelper.AddAddress()
    address_url = add_address_helper.add_address(
        browser_fixture, data_fixture_js, delete_address
    )
    yield address_url


@pytest.fixture
def delete_address():
    addresses_to_delete = {"address": [], "headers": ""}
    yield addresses_to_delete
    for address in addresses_to_delete["address"]:
        requests.delete(address, headers=addresses_to_delete["headers"])


def pytest_generate_tests(metafunc):
    if "data_gen" in metafunc.fixturenames:
        cur_path = pathlib.Path(__file__).parent
        file = open(f"{cur_path}/test_input_data/qa.json")
        data = [json.load(file)]
        metafunc.parametrize(
            "data_gen",
            [data[0]["address_negative"]["p1"], data[0]["address_negative"]["p2"]],
        )
