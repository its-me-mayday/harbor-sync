class Registry:
    def __init__(self, host: str, username: str):
        self._host = host
        self._username = username
    
    @property
    def host(self):
        self._host = host
    
    @property
    def username(self):
        self._username = username
    
    def __repr__(self):
      return f"Registry(host={self.host}, username={self.username})"
