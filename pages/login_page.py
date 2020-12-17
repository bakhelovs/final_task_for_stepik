from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        # В поле ввода email вводим email
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_REG_FORM).send_keys(email)
        # В поле ввода пароля вводим password
        self.browser.find_element(*LoginPageLocators.PASS_INPUT_REG_FORM).send_keys(password)
        # В поле повторного ввода пароля вводим password
        self.browser.find_element(*LoginPageLocators.PASS_CONFIRM_INPUT_REG_FORM).send_keys(password)
        # Кликаем по кнопке "зарегестрировать"
        self.browser.find_element(*LoginPageLocators.REG_BUTTON_REG_FORM).click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка в линке текста login
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
            "Login link is not presented"
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # Проверка наличия формы с логином и паролем
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK),\
            "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # Проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REG_FORM_LINK),\
            "Registration form is not presented"
        assert True
