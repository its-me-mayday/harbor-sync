from models.registry import Registry

class RegistryService:
  def __init__(self, logger):
    self.logger = logger
  
  def setup(self, settings):
    return Registry(settings.url, settings.username, settings.password)