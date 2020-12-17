from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    MESSAGE_BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    BASKET_TOTALS_FORM = (By.CSS_SELECTOR, "basket_totals")


class MainPageLocators:
    pass


class LoginPageLocators:
    REG_FORM_LINK = (By.CSS_SELECTOR, "form#register_form.well")
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "form#login_form.well")
    EMAIL_INPUT_REG_FORM = (By.ID, "id_registration-email")
    PASS_INPUT_REG_FORM = (By.ID, "id_registration-password1")
    PASS_CONFIRM_INPUT_REG_FORM = (By.ID, "id_registration-password2")
    REG_BUTTON_REG_FORM = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
