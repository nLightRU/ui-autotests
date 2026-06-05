from collections import namedtuple
import pytest

from pages.cart_page import CartPage

@pytest.fixture
def empty_cart(base_url, standard_user_cookie, context):
    context.add_cookies([standard_user_cookie])
    url = f'{base_url}/cart.html'
    p = context.new_page()
    return CartPage(url=url, page=p)

@pytest.fixture
def cart_with_one_product(empty_cart):
    empty_cart.open_page()
    empty_cart._page.evaluate("localStorage.setItem('cart-contents','[4]')")

    return CartPage(url=empty_cart.url, page=empty_cart._page)
