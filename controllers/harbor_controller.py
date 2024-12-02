import logging

import requests

class HarborController:
    def __init__(self, model, logger):
        self.model = model
        self.logger = logger

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

    def get_tags_by_repository(self, project_name, repository_name):
        logger.debug(
            f"Uses project_name: {project_name}"
            "and repository_name: {repository_name}"
        )

        base_url = f"{self.model.url}/api/v2.0"
        project_url = f"{base_url}/projects/{project_name}"
        repository_url = f"{project_url}/repositories/{repository_name}"
        url = f"{repository_url}/artifacts"
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
