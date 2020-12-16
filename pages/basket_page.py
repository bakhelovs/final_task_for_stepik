from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        # Отрицательная проверка отсутвия в пустой корзине товаров
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTALS_FORM), \
            "The basket is not empty"
        assert True

    def should_be_basket_is_empty_message(self):
        # Проверка наличия сообщения о пустой корзине
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), \
            "Message about the basket is empty is not presented"
        assert True
