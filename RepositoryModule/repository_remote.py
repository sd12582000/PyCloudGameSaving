"""
Repository in remote Repository
"""
from helper import git_helper
from . import LocalRepository
class RemoteRepository(LocalRepository):
    """
    Repository in remote Repository
    """
    def __init__(self, config):
        """
        init
        """
        self.config = config
        self.repo_path = config['save_dir']
        self.repo_url = config['RepositoryUrl']

    def before_launch_game(self):
        """
        launch game event
        check Repository status
        create Repository
        add remote repo
        pull
        """
        super(RemoteRepository, self).before_launch_game()

        if git_helper.call_git_pull(self.repo_path) != 0:
            git_helper.call_git_remote_add(self.repo_path, self.repo_url)
            git_helper.call_git_clean(self.repo_path, force=True)
            git_helper.call_git_pull(self.repo_path, force=True)
        print("=== RemoteRepository launch_game ===")

    def exit_game(self):
        """
        exit game event
        """
        super(RemoteRepository, self).exit_game()

        print("=== RemoteRepository exit_game ===")

    def backup_save(self, commit_message):
        """
        backup_save event
        git add .
        git commit -m commit_message
        git push
        """
        super(RemoteRepository, self).backup_save(commit_message)
        git_helper.call_git_push(self.repo_path)

        print("=== RemoteRepository backup_save ===")

    @classmethod
    def create_config(cls, file_name):
        """
        create a new config
        """
        config = super(RemoteRepository, cls).create_config(file_name)
        repo_url = input("Input Remote Repository Url : ")
        config['RepositoryUrl'] = repo_url
        config['RepositoryType'] = 'RemoteRepository'
        print("=============================")
        return config
