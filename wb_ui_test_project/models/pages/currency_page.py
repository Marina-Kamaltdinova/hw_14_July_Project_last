from selene import browser, have
import allure


class Currency:
    def currency_replacement_check(self, value):
        with allure.step("Проверка текущей валюты"):
            browser.element('.simple-menu__currency').should(have.exact_text(value))
            return self

    def choice_currency(self):
        with allure.step("Выбор валюты для замены"):
            browser.element('.header__currency').hover()
            return self

    def currency_replacement(self, value):
        with allure.step("Замена валюты"):
            browser.all('.radio-with-text__name').element_by(have.text(value)).click()
            return self

    def check_replacement(self, value):
        with allure.step("Проверка отображения валюты после замены"):
            browser.element('.simple-menu__currency').should(have.text(value))
            return self

    def currency_back(self, value):
        with allure.step("Возврат валюты в исходное состояние"):
            browser.all('.radio-with-text__name').element_by(have.text(value)).click()
            return self


currency = Currency()
