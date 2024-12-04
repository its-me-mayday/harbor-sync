from services.registry_service import RegistryService


class RegistryController:
    def __init__(self, logger):
        self.logger = logger
        self._registry_service = RegistryService(logger)

    def setup(self, settings, is_source):
        self.logger.debug(
            f"Settings are: {settings} and is_source: {is_source}"
        )
        registry = self._registry_service.setup(settings, is_source)
        self.logger.debug(f"The registry is: {registry}")

        return registry
