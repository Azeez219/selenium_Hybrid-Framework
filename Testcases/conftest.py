# This file is for Selecting the Browser and creating the html reports....

import pytest
from selenium import webdriver
import pytest_html

@pytest.fixture
def setup():
    # if browser=='chrome':
    driver = webdriver.Chrome()
    return driver
#     elif browser=='chrome':
#         driver = webdriver.Firefox()

#     else:
#         driver = webdriver.Edge()
#     return driver

# def pytest_addoption(parser):   # This will get the values from CLI/hooks
#     parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):   # This will return the Browser value to setup method.
#     return request.config.getoption("--browser")



# ############   pytest-html reports ##############

# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester Name'] = 'Azeez'

# # It is hook to Modidy/Delete Environment info to HTML Reports

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA HOME", None)
#     metadata.pop("Plugins", None)





