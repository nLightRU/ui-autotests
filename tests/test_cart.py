import allure
import pytest

@allure.feature('Cart')
def test_page_open(cart_page):
    cart_page.open_page()
    cart_page.page_is_opened()
