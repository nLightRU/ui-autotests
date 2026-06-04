import pytest

from pages.cart_page import CartPage

@pytest.fixture
def cart_page(base_url, context):
    context.add_cookies([{
        'name': 'session-username',
        'value': 'standard_user',
        'domain': 'www.saucedemo.com',
        'path': '/'
    }])
    url = f'{base_url}/cart.html'
    p = context.new_page()
    return CartPage(url=url, page=p)