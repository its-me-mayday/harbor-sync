from config.logger import logger
from config.settings import source_settings, destination_settings
from services.harbor_service import HarborService
from controllers.factories import create_harbor_controller, create_registry_controller


def main():
    logger.info("Run Harbor Sync application.")

    harbor_controller = create_harbor_controller(logger)
    logger.debug(f"Harbor Controller initiated: {harbor_controller}")
    
    registry_controller = create_registry_controller(logger)
    logger.debug(f"Registry Controller initiated: {registry_controller}")


if __name__ == "__main__":
    main()
