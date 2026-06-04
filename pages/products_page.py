import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, url: str=None, page: Page=None):
        super().__init__(url, page)
        self.title = self._page.locator('.title')
        self.cart = self._page.locator('shopping_cart_link')
        self.cart_badge = self._page.locator('.shopping_cart_badge')
    
        self.test_product_button = self._page.locator('//*[@id="add-to-cart-sauce-labs-backpack"]')
        self.products_cards = self._page.locator('.inventory_item')

    def check_opened(self):
        expect(self.title).to_have_text('Products')

    def add_first_product(self):
        self.test_product_button.click()

    def get_products_count(self):
        return len(self.products_cards.all())

    @allure.step('Добавить товар в корзину')
    def add_product_to_cart(self, product_num: int = 1):
        products = self.products_cards.all()
        add_to_cart_button = products[product_num-1].get_by_role('button')
        add_to_cart_button.click()

    @allure.step('Проверить отсутствие бейджа у корзины')
    def check_cart_badge_not_visible(self):
        expect(self.cart_badge).not_to_be_visible()

    @allure.step('Проверить наличие бейджа у корзины')
    def check_cart_badge_visible(self):
        expect(self.cart_badge).to_be_visible()

    @allure.step('Получить значение бейджа у корзины')
    def get_cart_badge_value(self):
        return int(self.cart_badge.text_content())