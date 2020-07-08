import pytest

from api.client import EmailClient


@pytest.fixture(scope="session")
def client():
    client = EmailClient("https://e.mail.ru", "/api/v1/")
    return client


@pytest.fixture()
def pwd_gen(client):
    def _method(locale, count, complexity):
        args = {"locale": locale, "count": count, "complexity": complexity}

        return client.get("utils/password/generate", args)

    return _method
