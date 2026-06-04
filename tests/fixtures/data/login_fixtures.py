import os
from dotenv import load_dotenv

import pytest

load_dotenv()

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
def locked_out_username():
    return os.getenv('LOCKED_OUT_USERNAME')


@pytest.fixture
def locked_out_password():
    return os.getenv('LOCKED_OUT_PASSWORD')
