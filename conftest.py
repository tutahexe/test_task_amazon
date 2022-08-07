import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config_helper import read_value_from_config
from fixtures.db import Db
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


@pytest.fixture()
def db(request):
    global db_fixture
    if db_fixture is None:
        db = read_value_from_config('db_connection')
        print(db)
        db_fixture = Db(db=db)
    return db_fixture


def pick_driver_from_config():
    conf_driver = read_value_from_config('driver')
    if conf_driver == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        if ui_fixture is not None:
            ui_fixture.close()

    request.addfinalizer(fin)
    return ui_fixture
