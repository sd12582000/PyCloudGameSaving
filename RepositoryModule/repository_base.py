"""
Abstract Repository Class
"""
from abc import ABCMeta, abstractmethod, abstractclassmethod

class Repository(metaclass=ABCMeta):
    """
    Game Save Repsoitory
    """
    @abstractmethod
    def before_launch_game(self):
        """
        launch game event
        """
        pass

    @abstractmethod
    def exit_game(self):
        """
        exit game event
        """
        pass

    @abstractmethod
    def backup_save(self, commit_message):
        """
        backup_save event
        """
        pass

    @abstractclassmethod
    def create_config(cls, file_name):
        """
        create a new config
        """
        from helper import steam_helper
        config = {
            'RepositoryName':steam_helper.get_stream_game_title(file_name),
            'save_dir':'',
            'RepositoryType':'Repository'
        }
        print('=== create a new config for {} ==='.format(file_name))
        repo_name = input("Input RepositoryName (defult:{}) : ".format(config['RepositoryName']))
        if repo_name:
            config['RepositoryName'] = repo_name
        config['save_dir'] = input("Input save data directory : ")
        return config
