import os
from dotenv import load_dotenv
import allure
from playwright.sync_api import Page, expect

load_dotenv()

class LoginPage:
    def __init__(self, page: Page):
        self._page = page
        self.url = os.getenv('BASE_URL')
        self.login_button = self._page.get_by_role('button')
        self.username_input = self._page.locator('#user-name')
        self.password_input = self._page.locator('#password')
        self.error_message_container = self._page.locator(".error-message-container")

    @allure.step('Переходим на страницу')
    def open_page(self):
        """Переходим на URL для данной страницы"""
        self._page.goto(self.url)

    @allure.step('Заполнить поле "username"')
    def fill_username(self, text: str = None):
        self.username_input.fill(text)
    
    @allure.step('Заполнить поле "password"')
    def fill_password(self, text: str = None):
        self.password_input.fill(text)

    @allure.step('Кликнуть по кнопке "Login"')
    def click_login(self):
        self.login_button.click()

    @allure.step("Проверить наличие сообщения об ошибке")
    def check_error_message_visible(self):
        expect(self.error_message_container).to_be_visible()

    @allure.step("Проверить успешный логин")
    def check_susscess_login(self):
        expect(self._page.get_by_text('Products')).to_be_visible()

    @allure.step('Проверить сообщение об ошибке')
    def check_error_message_text(self, text: str=None):
        if not text:
            raise ValueError(f'No text to check in {self.__qualname__}')
        expect(self.error_message_container).to_have_text(text)