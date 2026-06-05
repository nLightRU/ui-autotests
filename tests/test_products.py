import allure
from time import sleep

import pytest


@allure.feature('Products')
@allure.title('Страница открывается (health check)')
def test_health(products_page):
    products_page.open_page()
    products_page.check_opened()


@allure.feature('Products')
@allure.title('При добавлении в корзину появляется бейдж')
def test_cart_badge_appear(products_page):
    products_page.open_page()
    products_page.check_cart_badge_not_visible()
    products_page.click_product_button(1)
    products_page.check_cart_badge_visible()
    assert 1 == products_page.get_cart_badge_value()


@allure.feature('Products')
@allure.title('Увеличивается значение бейджа')
def test_badge_value_incrementing(products_page):
    products_page.open_page()
    products_page.check_cart_badge_not_visible()
    
    products_page.click_product_button(1)
    products_page.check_cart_badge_visible()
    assert 1 == products_page.get_cart_badge_value()

    products_page.click_product_button(2)
    products_page.check_cart_badge_visible()
    assert 2 == products_page.get_cart_badge_value()


@allure.feature('Products')
@allure.title('Удаляется бейдж у корзины')
def test_cart_badge_dissappearing(products_page):
    products_page.open_page()
    products_page.check_cart_badge_not_visible()

    products_page.click_product_button(1)
    products_page.check_cart_badge_visible()

    products_page.click_product_button(1)
    products_page.check_cart_badge_not_visible()


@allure.feature('Products')
@allure.title('Кнопка у товара меняется на Remove')
def test_product_button_is_changing(products_page):
    product_num = 1
    products_page.open_page()
    products_page.click_product_button(product_num)
    products_page.check_product_button_is_remove(product_num)


@allure.feature('Products')
@allure.title('При наведении на название товара меняется цвет')
def test_product_title_hover_color(products_page):
    product_num = 1
    products_page.open_page()
    products_page.check_product_name_hover_color(product_num)


@allure.feature('Products')
@allure.title('Можно открыть карточку товара')
@pytest.mark.parametrize('product_num', [1, 4])
def test_products_cart_open(products_page, product_num:int):
    products_page.open_page()
    name = products_page.get_product_name(product_num)
    description = products_page.get_product_description(product_num)

    card = products_page.open_product_page(product_num)
    card.check_name(name)
    card.check_description(description)


@allure.feature('Products')
@allure.title('При открытии карточки товара в корзине кнопка остаётся Remove')
def test_product_button_is_changing(products_page):
    product_num = 1