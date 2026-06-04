import allure
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, url: str=None, page: Page=None):
        self.url = url
        self._page = page
        self.title = None

    @allure.step('Переходим на страницу')
    def open_page(self):
        self._page.goto(self.url)

    @allure.step('Страница открывается')
    def page_is_opened(self):
        expect(self.title).to_be_visible()