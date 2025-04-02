from sys import executable

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        server = Service()
        chrome = webdriver.ChromeOptions()
        #Options.add_experimental_option("some_option", "some_value")
        chrome.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome)
    elif browser_name == "firefox":
        service = Service(executable_path=r'C:\\Users\eshwar.m\Downloads\geckodriver.exe')
        driver = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        print("edge")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()