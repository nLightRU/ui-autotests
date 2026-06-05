import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductCartPage(BasePage):
    def __init__(self, url:str, page:Page):
        super().__init__(url, page)
        self.product_name = self._page.locator('.inventory_details_name')
        self.product_description = self._page.locator('.inventory_details_desc')

        self.product_button = self._page \
                               .locator('.inventory_details_desc_container') \
                               .get_by_role('button')

        self.back_to_products = self._page.locator('#back-to-products')

    @allure.step('Проверяем названеи товара')
    def check_name(self, text: str | None):
        if text is None:
            raise ValueError('text is required')
        return self.product_name.text_content() == text

    @allure.step('Проверяем описание товара')
    def check_description(self, text: str | None):
        if text is None:
            raise ValueError('text is required')
        return self.product_description.text_content() == text

    @allure.step('Проверяем название кнопки')
    def check_button_is_remove(self):
        expect(self.product_button).to_have_text('Remove')

    @allure.step('Кликнуть на кнопку Add to cart / Remove')
    def click_button(self):
        self.product_button.click()

    @allure.step('Кликнуть Back to products')
    def click_back_to_products(self):
        self.back_to_products.click()