from models.registry import RegistryModel
from views.cli import CliView
from controllers.harbor import HarborController

def main():
    REGISTRY_SRC = "https://harbor.navarcos.ccoe-nc.com"
    USERNAME_SRC = "" # subsitute with robot$harbor
    PASSWORD_SRC = "" # substitute with robot$harbor and setup a setting for this part (information hiding)
    PROJECT_NAME = "ccoe"
    
    model = Registry(REGISTRY_SRC, USERNAME_SRC, PASSWORD_SRC)
    view = CliView() 
    controller = HarborController(model, view) 

    repositories = controller.get_repositories_by_project(PROJECT_NAME)
    if repositories:
        view.display_repositories(repositories)