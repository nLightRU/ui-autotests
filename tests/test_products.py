import allure
from time import sleep

@allure.feature('Products')
@allure.title('Страница открывается (health check)')
def test_health(products_page):
    products_page.open_page()
    products_page.check_opened()


@allure.feature('Products')
@allure.title('Добавление 1 товара в корзину')
def test_add_one_item_to_cart(products_page):
    products_page.open_page()
    products_page.check_cart_badge_not_visible()
    products_page.add_product_to_cart(1)
    products_page.check_cart_badge_visible()
    assert 1 == products_page.get_cart_badge_value()


@allure.feature('Products')
@allure.title('Добавление 2 товаров в корзину')
def test_add_two_items_to_cart(products_page):
    products_page.open_page()
    products_page.check_cart_badge_not_visible()
    products_page.add_product_to_cart(1)
    products_page.check_cart_badge_visible()
    assert 1 == products_page.get_cart_badge_value()
    products_page.add_product_to_cart(2)
    assert 2 == products_page.get_cart_badge_value()
