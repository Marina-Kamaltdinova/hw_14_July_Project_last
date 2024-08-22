from selene import browser, have, be
import allure


class Home:
    def open_page(self):
        with allure.step("Открыть домашнюю страницу"):
            browser.open('https://www.wildberries.ru/')
            return self

    def search_item(self, value):
        with allure.step("Выбор продукта"):
            search = browser.element('#searchInput')
            search.click()
            search.set_value(' ')
            browser.element('.autocomplete__content').should(be.visible)
            search.set_value(value).press_enter()
            return self

    def open_chat(self):
        with allure.step("Открыть чат"):
            browser.element('button.btn-chat').with_(timeout=30).click()
            return self

    def verify_chat_title(self, title):
        with allure.step("Проверка содержимого чата"):
            browser.element('.chat__text').should(have.text(title))
            return self


home = Home()
