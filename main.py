from config.logger import logger
from config.settings import registrySettings
from services.harbor_services import HarborService


def main():
    logger.info("Run Harbor Sync application.")
    harborService = HarborService(registrySettings)
    result = harborService.migrate_repository()
    logger.info(f"Harbor Sync Outcome: {result}.")


if __name__ == "__main__":
    main()
