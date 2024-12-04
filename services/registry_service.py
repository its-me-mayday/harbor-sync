from models.registry import Registry


class RegistryService:
    def __init__(self, logger):
        self.logger = logger

    def setup(self, settings, is_source):
        registry = Registry(settings.host, settings.username, is_source)
        return registry
