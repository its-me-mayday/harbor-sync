from config.logger import logger
from models.registry import RegistryModel
from views.cli import CliView
from controllers.harbor import HarborController

def main():
    REGISTRY_SRC = "https://harbor.navarcos.ccoe-nc.com"
    USERNAME_SRC = "" # subsitute with robot$harbor
    PASSWORD_SRC = "" # substitute with robot$harbor and setup a setting for this part (information hiding)
    PROJECT_NAME = "ccoe"

    logger.info("Run Harbor Sync application.")

    try:    
        model = Registry(REGISTRY_SRC, USERNAME_SRC, PASSWORD_SRC)
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