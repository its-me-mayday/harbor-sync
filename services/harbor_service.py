from config.logger import logger


class HarborService:
    def __init__(self, src_settings):
        self.src_settings = src_settings

    def migrate_repository(self):
        logger.debug(
            "Starts migration repositories of project "
            f"{self.src_settings.project_name}"
        )

        try:
            logger.debug("Repositories retrieved!")

            if repositories:
                logger.info(f"Found {len(repositories)} repositories.")
                logger.info(f"Repositories: {repositories}")

                repository_name = "superset"  # to be deleted
                tags = controller.get_tags_by_repository(
                    self.src_settings.project_name, repository_name
                )
                logger.debug(f"Tags from {repository_name} are: {tags}")
            else:
                logger.warning("No repository found.")
        except Exception as e:
            logger.error(f"Error during application execution: {e}")
        return True


# for item in data:
#    for tag in item.get('tags', []):
#        tags.append(tag['name'])
