import allure

@allure.feature('Login')
def test_success_login(
        login_page,
        success_login_username,
        success_login_password
):
    login_page.open_page()
    login_page.fill_username(success_login_username)
    login_page.fill_password(success_login_password)
    login_page.click_login()
    login_page.check_susscess_login()

@allure.feature('Login')
def test_wrong_password(
    login_page,
    success_login_username,
    wrong_password,
    wrong_password_error
):
    login_page.open_page()
    login_page.fill_username(success_login_username)
    login_page.fill_password(wrong_password)
    login_page.click_login()
    login_page.check_error_message_visible()
    login_page.check_error_message_text(wrong_password_error)