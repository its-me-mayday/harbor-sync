from controllers.harbor_controller import HarborController
from controllers.registry_controller import RegistryController


def create_harbor_controller(logger):
    return HarborController(logger)


def create_registry_controller(logger):
    return RegistryController(logger)
