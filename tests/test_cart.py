from time import sleep
import allure

@allure.feature('Cart')
@allure.title('Страница открывается')
def test_page_open(empty_cart):
    empty_cart.open_page()
    empty_cart.page_is_opened()


@allure.feature('Cart')
@allure.title('Переход на страницу Products')
def test_back_to_products(empty_cart):
    empty_cart.open_page()
    empty_cart.click_continue_shopping_button()
    empty_cart.check_go_to_products()


@allure.feature('Cart')
@allure.title('Товары отображаются в корзине')
def test_cart_with_one_product(cart_with_one_product):
    product_num = 1
    cart_with_one_product.open_page()
    cart_with_one_product.cart_item_is_visible(product_num)


@allure.feature('Cart')
@allure.title('Переход на страницу Checkout Information')
def test_go_to_checkout(cart_with_one_product):
    cart_with_one_product.open_page()
    cart_with_one_product.click_checkout_button()
    cart_with_one_product.check_go_to_checkout()
    sleep(5)