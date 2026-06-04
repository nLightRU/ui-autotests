import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, url: str=None, page: Page=None):
        super().__init__(url, page)
        self.title = self._page.locator('.title')
        self.cart = self._page.locator('shopping_cart_link')
        self.cart_badge = self._page.locator('.shopping_cart_badge')
        self.products_cards = self._page.locator('.inventory_item')

    def get_products_count(self):
        return len(self.products_cards.all())

    @allure.step('Проверяем что страница открывается')
    def check_opened(self):
        expect(self.title).to_have_text('Products')

    @allure.step('Цвет шрифта названия товара')
    def get_product_title_color(self, product_num: int = None) -> tuple[int, int, int]:
        product_name = self.products_cards \
                        .all()[product_num-1] \
                        .locator('.inventory_item_name')

    @allure.step('Навести мышкой на название товара')
    def hover_product_name(self, product_num: int = None):
        product_name = self.products_cards \
                        .all()[product_num-1] \
                        .locator('.inventory_item_name')
        
    @allure.step('Кликаем на кнопку у товара')
    def click_product_button(self, product_num: int = None):
        """Кликаем на кнопку Add to cart / Remove у товара"""
        products = self.products_cards.all()
        add_to_cart_button = products[product_num-1].get_by_role('button')
        add_to_cart_button.click()

    @allure.step('Проверить, что кнопка стала Remove')
    def check_product_button_is_remove(self, products_num: int = None):
        button = self.products_cards.all()[products_num-1].get_by_role('button')
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
