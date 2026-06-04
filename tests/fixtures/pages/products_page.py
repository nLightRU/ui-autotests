import pytest

from pages.products_page import ProductsPage

@pytest.fixture
def products_page(base_url, context):
    context.add_cookies([{
            'name':'session-username', 
            'value':'standard_user',
            'domain': 'www.saucedemo.com',
            'path': '/'
    }])
    url = f'{base_url}/inventory.html'
    p = context.new_page()
    return ProductsPage(url=url, page=p)