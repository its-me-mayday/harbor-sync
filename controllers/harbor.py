import requests

class HarborController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_repositories_by_project(self, project_name):
        url = f"{self.model.url}/api/v2.0/projects/{project_name}/repositories"
        
        auth = (self.model.username, self.model.password)
        response = request.get(url, auth=self.auth)
        response.raise_for_status()
        return response.json