from config.logger import logger
from config.settings import registrySettings
from controllers.harbor import HarborFactory


def main():
    logger.info("Run Harbor Sync application.")

    try:
        controller = HarborFactory.create_harbor_controller()
        logger.debug("Controller correctly instatiated!")

        repositories = controller.get_repositories_by_project(
            registrySettings.project_name
        )
        logger.debug("Repositories retrieved!")

        if repositories:
            logger.info(f"Found {len(repositories)} repositories.")
            logger.info(f"Repositories: {repositories}")
        else:
            logger.warning("No repository found.")
    except Exception as e:
        logger.error(f"Error during application execution: {e}")


if __name__ == "__main__":
    main()
