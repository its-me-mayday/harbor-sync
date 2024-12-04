from models.registry import Registry

class RegistryService:
  def __init__(self, logger):
    self.logger = logger
  
  def setup(self, settings):
    registry = Registry(settings.host, settings.username)
    return registry