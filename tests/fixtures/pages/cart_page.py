import pytest

from pages.cart_page import CartPage

@pytest.fixture
def empty_cart(base_url, standard_user_cookie, context):
    context.add_cookies([standard_user_cookie])
    url = f'{base_url}/cart.html'
    p = context.new_page()
    return CartPage(url=url, page=p)

@pytest.fixture
def cart_with_one_product(base_url, context):
    ...