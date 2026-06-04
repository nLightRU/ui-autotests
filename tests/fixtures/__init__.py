import os
import pytest
from dotenv import load_dotenv

from .login_page import login_page

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