import logging

logger = logging.getLogger("harbor_sync")

class RegistryModel:
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password

    @classmethod
    def create(cls, url: str, username: str, password: str):
        """
        Factory method to create an instance of RegistryModel with parameter validation.
        """
        missing = [param for param, value in {"url": url, "username": username, "password": password}.items() if not value]
        if missing:
            logger.error(f"The following parameters are missing or empty: {', '.join(missing)}")
            raise ValueError(f"The following parameters are mandatory: {', '.join(missing)}")
        
        logger.info(f"Creating RegistryModel with URL: {url}")
        
        return cls._internal_create(url, username, password)