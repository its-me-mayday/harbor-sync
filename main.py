from config.logger import logger
from config.settings import settings
from models.registry import RegistryModel
from views.cli import CliView
from controllers.harbor import HarborController

def main():
    logger.info("Run Harbor Sync application.")
    
    logger.info(f"Using registry URL: {settings.REGISTRY_SRC}") 

    try:    
        model = Registry.create(settings.REGISTRY_SRC, settings.USERNAME_SRC, settings.PASSWORD_SRC)
        view = CliView() 
        controller = HarborController(model, view) 
        logger.info(f"Retrieve repositories for project: {PROJECT_NAME}")
        repositories = controller.get_repositories_by_project(PROJECT_NAME)

        if repositories:
            logger.info(f"Found {len(repositories)} repositories.")
            view.display_repositories(repositories)
        else:
            logger.warning("No repository found.")
    except Exception as e:
        logger.error(f"Error during application execution.")

if __name__ == "__main__":
    main()