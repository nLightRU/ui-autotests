from time import sleep

def test_success_login(
        login_page,
        success_login_username,
        success_login_password
):
    login_page.open_page()
    login_page.fill_username(success_login_username)
    login_page.fill_password(success_login_password)
    login_page.click_login()