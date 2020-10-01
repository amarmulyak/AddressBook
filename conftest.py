import pytest
import json
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader
import pathlib
import requests


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
    json_file = open(f'{cur_path}\\test_input_data\\qa.json')
    # json_file = open(f'{cur_path}/test_input_data/qa.json')
    data_from_file = json.load(json_file)
    yield data_from_file
    json_file.close()


@pytest.fixture
def delete_address(data_fixture_js):
    data_fixture_js["addresses_to_delete"] = {}
    yield data_fixture_js["addresses_to_delete"]
    breakpoint()
    for address, headers in data_fixture_js["addresses_to_delete"].items():
        requests.delete(address, headers=headers)


def pytest_generate_tests(metafunc):
    if "data_gen" in metafunc.fixturenames:
        cur_path = pathlib.Path(__file__).parent
        file = open(f'{cur_path}\\test_input_data\\qa.json')
        # file = open(f'{cur_path}/test_input_data/qa.json')
        data = [json.load(file)]
        metafunc.parametrize("data_gen", [
            data[0]["address_negative"]["p1"],
            data[0]["address_negative"]["p2"]
            ]
        )
