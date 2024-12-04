class Registry:
    def __init__(self, url: str, username: str, password: str):
        self._url = url
        self._username = username
        self._password = password

    def __repr__(self):
      return f"Registry(url={self.url}, username={self.username}, password=****)"
