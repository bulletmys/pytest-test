import requests


class EmailClient:
    _s = requests.session()
    host = None
    version = "v1"

    def __init__(self, host, version):
        self.host = host
        self.version = version

    def get_user(self):
        return self._s.get(self.host + "/api/" + self.version + "/user")
