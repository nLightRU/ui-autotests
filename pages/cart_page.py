import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, url: str=None, page: Page=None):
        super().__init__(url, page)
        self.title = self._page.locator('.title')
        self.checkout_button = self._page.locator('.checkout-button')
        self.cart_items = self._page.locator('.cart_item')

    @allure.step('У товара в корзине есть кнопка Remove')
    def check_button(self, product_num: int = None):
        if not product_num:
            raise ValueError('product_num is required')
        products = self.cart_items.all()[product_num]
        expect(products.get_by_role('button')).to_have_text('Remove')