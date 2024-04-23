from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = ReadConfigurations.read_configuration("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()

    app_url = ReadConfigurations.read_configuration("basic info","url")
    driver.get(app_url)
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Cancellation Policy")))
    request.cls.driver = driver
    yield
    driver.quit()
