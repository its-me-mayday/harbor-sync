import logging

import requests

from config.settings import registrySettings
from models.registry import RegistryModel

logger = logging.getLogger("harbor_sync")


class HarborController:
    def __init__(self, model):
        self.model = model

    def get_repositories_by_project(self, project_name):
        logger.debug(f"Uses project_name: {project_name}")

        url = f"{self.model.url}/api/v2.0/projects/{project_name}/repositories"
        logger.debug(f"Uses url: {url}")

        auth = (self.model.username, self.model.password)
        logger.info(f"Auth params by username: {self.model.username}")

        try:
            response = requests.get(url, auth=auth)
            logger.info(
                f"Status response: {response.status_code} with url: {url}"
            )
            logger.debug(f"Content response: {response.content}")
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f"Encountered a RequestException: {e}")
            raise
        except Exception as e:
            logger.error(f"Encountered an Exception: {e}")
            raise

        return response.json()


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
