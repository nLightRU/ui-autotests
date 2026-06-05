import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.product_cart_page import ProductCartPage
from tests.fixtures.pages import products_page


class ProductsPage(BasePage):
    def __init__(self, url: str=None, page: Page=None):
        super().__init__(url, page)
        self.title = self._page.locator('.title')
        self.cart = self._page.locator('shopping_cart_link')
        self.cart_badge = self._page.locator('.shopping_cart_badge')
        self.products_cards = self._page.locator('.inventory_item')

    def get_products_count(self):
        return len(self.products_cards.all())

    def get_product_card(self, product_num: int = None):
        """Получаем элемент с карточкой товара"""
        product = self.products_cards.all()[product_num - 1]
        return product

    @allure.step('Проверяем что страница открывается')
    def check_opened(self):
        expect(self.title).to_have_text('Products')

    @allure.step('Сохраняем название товара на странице с товарами')
    def get_product_name(self, product_num: int = None) -> str | None:
        """Получаем название товара"""
        product = self.get_product_card(product_num)
        return product.locator('.inventory_item_name').text_content()

    @allure.step('Сохраняем описание товара на странице с товарами')
    def get_product_description(self, product_num: int = None) -> str | None:
        product = self.get_product_card(product_num)
        return product.locator('.inventory_item_desc').text_content()

    @allure.step('Проверить цвет названия товара при наведении мышкой')
    def check_product_name_hover_color(self, product_num: int = None):
        product = self.get_product_card(product_num)
        product_name = product.locator('.inventory_item_name')

        expect(product_name).to_have_css('color', 'rgb(24, 88, 58)')
        product_name.hover()
        expect(product_name).to_have_css('color', 'rgb(61, 220, 145)')

    @allure.step('Кликнуть на название товара')
    def click_product_name(self, product_num: int = None):
        product = self.get_product_card(product_num)
        product.locator('.inventory_item_name ').click()
        url = self._page.url
        return ProductCartPage(url=url, page=self._page)

    @allure.step('Кликаем на кнопку у товара')
    def click_product_button(self, product_num: int = None):
        """Кликаем на кнопку Add to cart / Remove у товара"""
        product = self.get_product_card(product_num)
        add_to_cart_button = product.get_by_role('button')
        add_to_cart_button.click()

    @allure.step('Проверить, что кнопка стала Remove')
    def check_product_button_is_remove(self, product_num: int = None):
        product = self.get_product_card(product_num)
        button = product.get_by_role('button')
        expect(button).to_have_text('Remove')
        expect(button).to_contain_class('btn_secondary')
        expect(button).to_have_css('color', 'rgb(226, 35, 26)')

    @allure.step('Проверить отсутствие бейджа у корзины')
    def check_cart_badge_not_visible(self):
        expect(self.cart_badge).not_to_be_visible()

    @allure.step('Проверить наличие бейджа у корзины')
    def check_cart_badge_visible(self):
        expect(self.cart_badge).to_be_visible()

    @allure.step('Получить значение бейджа у корзины')
    def get_cart_badge_value(self):
        return int(self.cart_badge.text_content())
