from config.logger import logger
from config.settings import destination_settings, source_settings
from controllers.factories import (create_harbor_controller,
                                   create_registry_controller)
from services.harbor_service import HarborService


def main():
    logger.info("Run Harbor Sync application.")

    harbor_controller = create_harbor_controller(logger)
    logger.debug(f"Harbor Controller initiated: {harbor_controller}")

    registry_controller = create_registry_controller(logger)
    logger.debug(f"Registry Controller initiated: {registry_controller}")

    source_registry = registry_controller.setup(source_settings)
    logger.debug(f"Source Registry: {source_registry}")
    destination_registry = registry_controller.setup(destination_settings)
    logger.debug(f"Destination Registry: {destination_registry}")


if __name__ == "__main__":
    main()
