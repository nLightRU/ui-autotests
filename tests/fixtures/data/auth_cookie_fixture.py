import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.fixture
def standard_user_cookie():
    return dict(
        name='session-username',
        value='standard_user',
        domain=os.getenv('DOMAIN'),
        path='/'
    )