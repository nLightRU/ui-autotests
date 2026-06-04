import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope='session')
def base_url():
    return os.getenv('BASE_URL')

@pytest.fixture
def success_login_username():
    return os.getenv('SUCCESS_LOGIN_USERNAME')

@pytest.fixture
def success_login_password():
    return os.getenv('SUCCESS_LOGIN_PASSWORD')

@pytest.fixture
def wrong_password():
    return 'wrongpassword'

@pytest.fixture
def wrong_password_error():
    return 'Epic sadface: Username and password do not match any user in this service'