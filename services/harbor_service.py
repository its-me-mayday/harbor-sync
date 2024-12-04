import requests

from config.settings import destination_secret, source_secret
from models.registry import Registry


class HarborService:
    def __init__(self, logger):
        self.logger = logger

    def repositories_by_project(self, registry: Registry, project_name):
        url = f"{registry.host}/api/v2.0/projects/{project_name}/repositories"
        self.logger.debug(f"Repositories by project URL: {url}")

        auth = self._setup_auth(registry)
        self.logger.info("Set authentication part")

        try:
            response = requests.get(url, auth=auth)
            self.logger.info(
                f"Status response: {response.status_code} with url: {url}"
            )
            self.logger.debug(f"Content response: {response.content}")
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Encountered a RequestException: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Encountered an Exception: {e}")
            raise
        return response

    def tags_by_project(
        self, repositories, registry: Registry, project_name: str
    ):
        base_url = f"{registry.host}/api/v2.0"
        project_url = f"{base_url}/projects/{project_name}"
        self.logger.debug(f"Project url: {project_url}")

        for repository in repositories:
            repository_name = repository["name"]
            url = f"{project_url}/repositories/{repository_name}/artifacts"
            self.logger.debug(
                f"repository_name: {repository_name} "
                f"from repository: {repository} "
                f"with url: {url}"
            )

    # def migrate_repository(self):
    #    logger.debug(
    #        "Starts migration repositories of project "
    #        f"{self.src_settings.project_name}"
    #    )

    #    try:
    #        logger.debug("Repositories retrieved!")

    #        if repositories:
    #            logger.info(f"Found {len(repositories)} repositories.")
    #            logger.info(f"Repositories: {repositories}")

    #            repository_name = "superset"  # to be deleted
    #            tags = controller.get_tags_by_repository(
    #                self.src_settings.project_name, repository_name
    #            )
    #            logger.debug(f"Tags from {repository_name} are: {tags}")
    #        else:
    #            logger.warning("No repository found.")
    #    except Exception as e:
    #        logger.error(f"Error during application execution: {e}")
    #    return True

    def _setup_auth(self, registry: Registry):
        if registry.is_source:
            return (registry.host, source_secret.password)
        else:
            return (registry.host, destination_secret.password)


# for item in data:
#    for tag in item.get('tags', []):
#        tags.append(tag['name'])
