from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        # Поиск кнопки "добавить в корзину" и переход по ней
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        link.click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Message about adding is not presented"
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), \
            "Message basket total is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Product price is not presented"
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        # Проверка отсутствия уведомления о добавлении товара
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        # Проверка исчезания уведомления о добавлении товара
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is not disappeared, but should be"
