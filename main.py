from config.logger import logger
from config.settings import destination_settings, source_settings
from controllers.factories import (
    create_harbor_controller,
    create_registry_controller,
)


def main():
    logger.info("Run Harbor Sync application.")

    harbor_controller = create_harbor_controller(logger)
    logger.debug(f"Harbor Controller initiated: {harbor_controller}")

    registry_controller = create_registry_controller(logger)
    logger.debug(f"Registry Controller initiated: {registry_controller}")

    source_registry = registry_controller.setup(source_settings, True)
    logger.debug(f"Source Registry: {source_registry}")
    destination_registry = registry_controller.setup(
        destination_settings, False
    )
    logger.debug(f"Destination Registry: {destination_registry}")

    repositories = harbor_controller.repositories_by_project(
        source_registry, source_settings.project_name
    )
    logger.debug(f"Repositories: {repositories}")

    tags = harbor_controller.tags_by_repository(
        repositories, source_registry, source_settings.project_name
    )
    logger.debug(f"Tags: {tags}")


if __name__ == "__main__":
    main()
