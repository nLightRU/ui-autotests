from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductCartPage(BasePage):
    def __init__(self, url:str, page:Page):
        super().__init__(url, page)
        self.product_name = self._page.locator('.inventory_details_name')
        self.product_description = self._page.locator('.inventory_details_desc')

    def check_name(self, text: str | None):
        if text is None:
            raise ValueError('text is required')
        return self.product_name.text_content() == text

    def check_description(self, text: str | None):
        if text is None:
            raise ValueError('text is required')
        return self.product_description.text_content() == text