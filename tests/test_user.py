class TestUser:

    def test_get_user_forbidden(self, client):
        # Нужно ли ловить ошибки тут или нет?
        response = client.get_user()
        data = response.json()
        assert data.get("status") == 403
