import os

# a = "C:\\Users\\Andrii\\repositories\\AddressBook\\venv\\Scripts;"
#
# print(a + 'adskjf;lasdj')

def os_json_path():
    os_path = os.environ.get("PATH")
    if "\\" in os_path:
        path = "\\test_input_data\\qa.json"
    else:
        path = "/test_input_data/qa.json"
    return path

print('www.abc' + os_json_path())
