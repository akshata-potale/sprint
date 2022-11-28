import pytest
from selenium import webdriver
from Library.config import Config
# path=r"C:\Users\admin\Desktop\Driver\chromedriver_win32\chromedriver.exe"
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


#Cross browsing
@pytest.fixture(params=["Chrome","Edge"])
def _driver(request):

    if request.param == "Chrome":
        driver = webdriver.Chrome(Config.Chrome_Driver_Path)

    # elif request.param == "Firefox":
    #     option = Options()
    #     option.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #     driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path, options=option)
    #     # driver= webdriver.Firefox(executable_path=Config.Firefox_Driver_Path)

    elif request.param == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    print(driver.title)
    driver.save_screenshot("test_hotelbooking.png")
    driver.close()
