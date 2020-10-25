import pytest

from utils.driver_factory import DriverFactory

@pytest.fixture()
def setup(request):

    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()