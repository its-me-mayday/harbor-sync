import logging

from config.settings import registrySettings
from controllers.harbor_controller import HarborController
from models.registry import RegistryModel

logger = logging.getLogger("harbor_sync")


class HarborFactory:
    @staticmethod
    def create_registry_model():
        """Create and returns a RegistryModel instance."""
        return RegistryModel(
            registrySettings.host,
            registrySettings.username,
            registrySettings.secret,
        )

    @staticmethod
    def create_harbor_controller():
        """Create and returns a HarborController instance."""
        model = HarborFactory.create_registry_model()
        return HarborController(model)
