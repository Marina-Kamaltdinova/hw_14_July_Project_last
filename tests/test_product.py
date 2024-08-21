from wb_ui_test_project.models.pages.home_page import home
from wb_ui_test_project.models.pages.catalog_page import catalog
from wb_ui_test_project.models.popup import pop_up_window
from wb_ui_test_project.models.pages.cart_page import cart


def test_adding_to_favorites():
    home.open_page()
    home.search_item('платье')
    catalog.check_title_search('платье')
    catalog.search_filter_tab('платье женское')
    catalog.check_title_search('платье женское')
    catalog.click_product_heart()
    pop_up_window.check_popup_visible()


def test_table_sizes():
    home.open_page()
    home.search_item('платье')
    catalog.check_title_search('платье')
    catalog.search_filter_tab('платье женское')
    catalog.check_title_search('платье женское')
    catalog.click_product_heart()
    pop_up_window.check_popup_visible()
    pop_up_window.check_popup_sizes_title('Выберите размер')
    pop_up_window.click_popup_sizes()
    pop_up_window.check_popup_table_title('Таблица размеров')


def test_search_item_by_id():
    home.open_page()
    home.search_item('144132398')
    catalog.validate_text('144132398')


def test_add_item_to_cart():
    home.open_page()
    home.search_item('144132398')
    catalog.validate_text('144132398')
    cart.product_add_to_cart()
    cart.added_in_cart('Товар добавлен в корзину')


def test_add_item_and_delete():
    home.open_page()
    home.search_item('144132398')
    catalog.validate_text('144132398')
    cart.product_add_to_cart()
    cart.added_in_cart('Товар добавлен в корзину')
    cart.search_del_button()
    cart.press_del()
    cart.check_after_delete('В корзине пока пусто')

