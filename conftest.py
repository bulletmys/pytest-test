import pytest

from api.client import EmailClient


@pytest.fixture(scope="session")
def client():
    client = EmailClient("https://e.mail.ru", "/api/v1/")
    return client
