import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope='session')
def base_url():
    return os.getenv('BASE_URL')


@pytest.fixture
def wrong_password_error():
    return 'Epic sadface: Username and password do not match any user in this service'


@pytest.fixture
def locked_out_user_error():
    return 'Epic sadface: Sorry, this user has been locked out.'