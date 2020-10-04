import pytest
import json
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader
import pathlib
import requests
import os


@pytest.fixture(scope="class")
def browser_fixture():
    chrome_driver = ChromeDriverDownloader()
    driver_path = chrome_driver.download_and_install()
    driver = webdriver.Chrome(
        executable_path=driver_path[0])
    yield driver
    driver.quit()


@pytest.fixture
def data_fixture_js():
    cur_path = pathlib.Path(__file__).parent
    # json_file = open(f'{cur_path}\\test_input_data\\qa.json')
    json_file = open(f'{cur_path}/test_input_data/qa.json')
    # path = os_json_path()
    # file_path = f'{cur_path}{path}'
    # json_file = open(file_path)
    data_from_file = json.load(json_file)
    yield data_from_file
    json_file.close()


@pytest.fixture
def delete_address(data_fixture_js):
    data_fixture_js["addresses_to_delete"] = {}
    yield data_fixture_js["addresses_to_delete"]
    for address, headers in data_fixture_js["addresses_to_delete"].items():
        requests.delete(address, headers=headers)


def pytest_generate_tests(metafunc):
    if "data_gen" in metafunc.fixturenames:
        cur_path = pathlib.Path(__file__).parent
        # file = open(f'{cur_path}\\test_input_data\\qa.json')
        file = open(f'{cur_path}/test_input_data/qa.json')
        # path = os_json_path()
        # file_path = f'{cur_path}{path}'
        # file = open(file_path)
        data = [json.load(file)]
        metafunc.parametrize("data_gen", [
            data[0]["address_negative"]["p1"],
            data[0]["address_negative"]["p2"]
            ]
        )


def os_json_path():
    os_path = os.environ.get("PATH")
    if "\\" in os_path:
        path = "\\test_input_data\\qa.json"
        # path = "/test_input_data/qa.json"
    else:
        path = "/test_input_data/qa.json"
    return path
