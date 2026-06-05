import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, url: str=None, page: Page=None):
        super().__init__(url, page)
        self.title = self._page.locator('.title')
        self.checkout_button = self._page.locator('.checkout-button')
        self.continue_shopping_button = self._page.locator('#continue-shopping')
        self.cart_items = self._page.locator('.cart_item')

    @allure.step('Есть кнопка Checkout')
    def check_checkout_button(self):
        expect(self.checkout_button).to_be_visible()

    @allure.step('Есть кнопка Continue Shopping')
    def check_continue_shopping_button(self):
        expect(self.checkout_button).to_be_visible()

    @allure.step('Кликнуть по кнопке Checkout')
    def click_checkout_button(self):
        self.checkout_button.click()

    @allure.step('Кликнуть по кнопке Continue Shopping')
    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()

    @allure.step('Проверка перехода на страницу Products')
    def check_go_to_products(self):
        expect(self._page.locator('.title')).to_have_text('Products')

    @allure.step('У товара в корзине есть кнопка Remove')
    def check_remove_product_button(self, product_num: int = None):
        if not product_num:
            raise ValueError('product_num is required')
        products = self.cart_items.all()[product_num]
        expect(products.get_by_role('button')).to_have_text('Remove')