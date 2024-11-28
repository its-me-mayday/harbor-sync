import logging

logger = logging.getLogger("harbor_sync")


class RegistryModel:
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password
