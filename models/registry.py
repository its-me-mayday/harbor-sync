class Registry:
    def __init__(self, host: str, username: str, is_source: bool):
        self._host = host
        self._username = username
        self._is_source = is_source

    @property
    def host(self):
        return self._host

    @property
    def username(self):
        return self._username

    @property
    def is_source(self):
        return self._is_source

    @is_source.setter
    def is_source(self, new_is_source):
        self._is_source = new_is_source

    def __repr__(self):
        return (
            f"Registry(host={self.host}, "
            f"username={self.username}, is_source={self.is_source})"
        )
