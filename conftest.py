import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser): # метод для передачи параметров командной строке
    parser.addoption('--language', # принимаем язык
                     action='store',
                     default='en',
                     help="Choose language : ru, es ..." )
    #pytest -s -v --language --language=es test_.py


@pytest.fixture(scope="function")
def browser(request): # принимаем  реквест от pytest_addoption  с введенным языком из командной строки
    user_language = request.config.getoption("language") # запрос значения языка
    options = Options() # создаем экземпляр Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) # передаем нужный язык
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options) # создаем экземпляр браузера и передаем результат options
    yield browser
    print("\nquit browser..")
    browser.quit()