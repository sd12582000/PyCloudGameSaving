"""
Repository in local Repository
"""
from helper import git_helper
from . import Repository
class LocalRepository(Repository):
    """
    Repository in local Repository
    """
    def __init__(self, config):
        """
        init
        """
        import platform
        self.config = config
        self.repo_path = config['save_dir']
        self.use_shell = True if platform.system() == 'Windows' else False

    def before_launch_game(self):
        """
        launch game event
        check Repository status
        create Repository
        """
        if git_helper.call_git_status(self.repo_path, shell=self.use_shell) != 0:
            git_helper.call_git_init(self.repo_path, shell=self.use_shell)
        print("=== LocalRepository launch_game ===")

    def exit_game(self):
        """
        exit game event
        """
        print("=== LocalRepository exit_game ===")

    def backup_save(self, commit_message):
        """
        backup_save event
        git add .
        git commit -m commit_message
        """
        git_helper.call_git_add_all(self.repo_path, shell=self.use_shell)
        git_helper.call_git_commit(self.repo_path, commit_message, shell=self.use_shell)

        print("=== LocalRepository backup_save ===")

    @classmethod
    def create_config(cls, file_name):
        """
        create a new config
        """
        config = super(LocalRepository, cls).create_config(file_name)
        config['RepositoryType'] = 'LocalRepository'
        print("=============================")
        return config
