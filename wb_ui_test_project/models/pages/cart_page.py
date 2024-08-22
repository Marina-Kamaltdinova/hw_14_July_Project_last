from selene import browser, have, command
import allure


class Cart:
    def product_add_to_cart(self):
        with allure.step("Добавление продукта в корзину"):
            browser.element('.product-page__order-buttons [aria-label="Добавить в корзину"]').click()
            return self

    def added_in_cart(self, value):
        with allure.step("Продукт в корзине"):
            browser.element('.action-notification__text').should(have.text(value))
            return self

    def check_after_delete(self, value):
        with allure.step("Проверка корзины после удаления"):
            browser.element('.basket-empty__title').should(have.text(value))
            return self

    def search_del_button(self):
        with allure.step("Клик на корзину"):
            browser.element('.j-item-basket').click()
            return self

    def press_del(self):
        with allure.step("Нажать на корзину для удаления"):
            browser.element('.btn .j-basket-item-del').perform(command.js.click)
            return self


cart = Cart()
