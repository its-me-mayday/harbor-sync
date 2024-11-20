class CliView:
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_error(error_message):
        print(f"[ERROR] {error_message}")

    @staticmethod
    def display_progress(repository, tag):
        print(f"Processing: {repository}:{tag}")
    
    @staticmethod
    def display_repositories(repositories):
        if not repositories:
            print("No repositories found.")
        else:
            print("Repositories:")
            for repo in repositories:
                print(f" - {repo['name']}")