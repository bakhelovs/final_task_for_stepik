from .pages.main_page import MainPage
from .pages.login_page import LoginPage

LINK_GLOBAL = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    link = LINK_GLOBAL
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = LINK_GLOBAL
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()