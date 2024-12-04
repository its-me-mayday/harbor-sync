class Registry:
    def __init__(self, host: str, username: str):
        self._host = host
        self._username = username

    @property
    def host(self):
        return self._host

    @property
    def username(self):
        return self._username

    def __repr__(self):
        return f"Registry(host={self.host}, username={self.username})"
