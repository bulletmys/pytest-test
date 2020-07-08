import requests


class EmailClient:
    _s = requests.session()
    host = None
    prefix = "api/v1/"

    def __init__(self, host, prefix):
        self.host = host
        self.prefix = prefix

    def get(self, endpoint, args=None):
        return self._s.get(self.host + self.prefix + endpoint, params=args)
