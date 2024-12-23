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
        tags = []

        for repository in repositories:
            repository_name = self._encode_slashes(repository["name"])

            url = self._url_tags(registry.host, project_name, repository_name)
            self.logger.debug(
                f"repository_name: {repository_name} "
                f"from repository: {repository} "
                f"with url: {url}"
            )

            auth = self._setup_auth(registry)
            self.logger.info("Set authentication part")

            try:
                response = requests.get(url, auth=auth)
                content = response.content
                tags.append(
                    {
                        "repository_name": repository["name"],
                        "artifacts": content,
                    }
                )
                self.logger.debug(f"tags: {tags}")
                self.logger.info(
                    f"Status response: {response.status_code} with url: {url}"
                )
                self.logger.debug(f"Content response: {response}")
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                self.logger.error(
                    f"Encountered a RequestException with url {url}: {e}"
                )
                raise
            except Exception as e:
                self.logger.error(f"Encountered an Exception: {e}")
                raise

        return tags

    # In future: build a Utility class
    def _encode_slashes(self, input_string):
        return input_string.split("/", 1)[-1].replace("/", "%252F")

    # In future: build an ApiService and setup settings route
    def _base_url(self, host):
        return f"{host}/api/v2.0"

    def _url_projects(self, host, project_name):
        base_url = self._base_url(host)
        return f"{base_url}/projects/{project_name}"

    def _url_tags(self, host: str, project_name: str, repository_name: str):
        project_url = self._url_projects(host, project_name)
        return f"{project_url}/repositories/{repository_name}/artifacts"

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
