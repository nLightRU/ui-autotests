import allure
from playwright.sync_api import Page

class BasePage:
    def __init__(self, url: str=None, page: Page=None):
        self.url = url
        self._page = page

    @allure.step('Переходим на страницу')
    def open_page(self):
        self._page.goto(self.url)