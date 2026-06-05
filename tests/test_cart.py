from time import sleep
import allure

@allure.feature('Cart')
@allure.title('Страница открывается')
def test_page_open(empty_cart):
    empty_cart.open_page()
    empty_cart.page_is_opened()
    sleep(5)


@allure.feature('Cart')
@allure.title('Переход на страницу Products')
def test_back_to_products(empty_cart):
    empty_cart.open_page()
    empty_cart.click_continue_shopping_button()
    empty_cart.check_go_to_products()

@allure.feature('Cart')
@allure.title('Товары отображаются в корзине')
def test_cart_with_one_product(cart_with_one_product):
    cart_with_one_product.open_page()
    sleep(5)
