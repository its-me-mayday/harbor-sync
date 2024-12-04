from services.harbor_service import HarborService


class HarborController:
    def __init__(self, logger):
        self.logger = logger
        self._harbor_service = HarborService(logger)

    def repositories_by_project(self, registry, project_name):
        self.logger.debug(
            f"Uses registry: {registry} and project_name: {project_name}"
        )

        repositories = self._harbor_service.repositories_by_project(
            registry, project_name
        )

        return repositories.json()

    def tags_by_repository(self, repositories, registry, project_name):
        self.logger.debug(
            f"Uses project_name: {project_name}"
            "and repository_name: {repositories}"
        )

        tags = self._harbor_service.tags_by_project(
            repositories, registry, project_name
        )

        return tags
