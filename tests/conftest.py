import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver(request):
    driver = webdriver.Chrome(executable_path=r'/Users/aleksandrparafijnyk/Desktop/chromedriver')
    request.addfinalizer(driver.quit)
    return driver