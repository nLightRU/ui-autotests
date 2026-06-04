import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage

@pytest.fixture
def login_page(base_url, page: Page):
    """Возвращает объект LoginPage"""
    return LoginPage(url=base_url, page=page)
