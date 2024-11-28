from config.logger import logger
from config.settings import settings
from controllers.harbor import HarborController
from models.registry import RegistryModel


def main():
    logger.info("Run Harbor Sync application.")
    logger.info(f"Using registry URL: {settings.REGISTRY_SRC}")

    try:
        model = RegistryModel(
            settings.REGISTRY_SRC, settings.USERNAME_SRC, settings.PASSWORD_SRC
        )
        logger.debug("Model correctly instatiated!")
        controller = HarborController(model)
        logger.debug("Controller correctly instatiated!")

        logger.info(
            f"Retrieve repositories for project: {settings.PROJECT_NAME}"
        )
        repositories = controller.get_repositories_by_project(
            settings.PROJECT_NAME
        )

        if repositories:
            logger.info(f"Found {len(repositories)} repositories.")
            logger.info(f"Repositories: {repositories}")
        else:
            logger.warning("No repository found.")
    except Exception as e:
        logger.error(f"Error during application execution: {e}")


if __name__ == "__main__":
    main()
