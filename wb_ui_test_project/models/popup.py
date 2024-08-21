from selene import browser, have, be
import allure


class Popup:
    def check_popup_visible(self):
        with allure.step("Проверка наличия всплывающего окна"):
            browser.element('.popup-list-of-sizes').should(be.visible)
            return self

    def check_popup_sizes_title(self, value):
        with allure.step("Проверка хэдера всплывающего окна_Таблица размеров_"):
            browser.element('.popup-list-of-sizes .popup__header').should(have.exact_text(value))
            return self

    def click_popup_sizes(self):
        with allure.step("Выбрать нужный размер"):
            browser.element('.popup .sizes-table').click()
            return self

    def check_popup_table_title(self, value):
        with allure.step("Проверка выбранного размера"):
            browser.element('.popup-table-of-sizes .popup__header').should(have.exact_text(value))
            return self

    def check_popup_title(self, value):
        with allure.step("Проверка заголовка попапа"):
            browser.element('.simple-menu__currency .popup__header').should(have.exact_text(value))
            return self


pop_up_window = Popup()
