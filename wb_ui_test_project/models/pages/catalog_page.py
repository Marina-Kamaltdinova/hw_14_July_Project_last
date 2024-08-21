from selene import browser, have
import allure


class Catalog:
    def check_title_search(self, value):
        with allure.step("Кликнуть на строку поиска"):
            browser.element(".searching-results__title").should(have.exact_text(value))
            return self

    def search_filter_tab(self, value):
        with allure.step("Нажать на нужный фильтр"):
            browser.all(".search-tags__item").element_by(have.exact_text(value)).click()
            return self

    def click_product_heart(self):
        with allure.step("Нажать на сердечко"):
            browser.all('.product-card').first.element('.product-card__heart').click()
            return self

    def validate_text(self, value):
        with allure.step("Проверка товара по результату поиска"):
            browser.element("#productNmId").should(have.text(value))
            return self


catalog = Catalog()
