import logging
import requests

logger = logging.getLogger("harbor_sync")

class HarborController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_repositories_by_project(self, project_name):
        logger.info(f"Controller get_repositories_by_project starts using PROJECT: {project_name}")
        url = f"{self.model.url}/api/v2.0/projects/{project_name}/repositories"
        logger.info(f"Controller get_repositories_by_project uses URL: {url}")
        
        auth = (self.model.username, self.model.password)
        logger.info(f"Controller get_repositories_by_project auth params by username: {self.model.username}")
        
        try:
            response = requests.get(url, auth=auth)
            logger.info(f"Controller get_repositories_by_project response: [status: {response.status_code}] {url}")
            logger.debug(f"Controller get_repositories_by_project content response: {response.content}")
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f"Controller get_repositories_by_project encountered an error: {e}")
            raise
        except Exception as e:
            logger.error(f"Controller get_repositories_by_project encountered an error: {e}")
            raise
        return response.json