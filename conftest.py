import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config_helper import read_value_from_config
from fixtures.ui import UI

db_fixture = None
ui_fixture = None


@pytest.fixture()
def ui(request):
    global ui_fixture
    if ui_fixture is None:
        driver = pick_driver_from_config()
        ui_fixture = UI(wd=driver)
    return ui_fixture


def pick_driver_from_config():
    conf_driver = read_value_from_config('driver')
    if conf_driver == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        if ui_fixture is not None:
            ui_fixture.close()

    request.addfinalizer(fin)
    return ui_fixture
