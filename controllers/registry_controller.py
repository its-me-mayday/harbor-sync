from services.registry_service import RegistryService


class RegistryController:
    def __init__(self, logger):
        self.logger = logger
        self._registry_service = RegistryService(logger)

    def setup(self, settings):
        self.logger.debug(f"The settings are: {settings}")
        registry = self._registry_service.setup(settings)
        self.logger.debug(f"The registry is: {registry}")

        return registry
