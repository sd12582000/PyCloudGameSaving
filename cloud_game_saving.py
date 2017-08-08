"""
Start play game
"""
import sys
import RepositoryModule
def get_config_options():
    """
    get config options list
    """
    result = []
    for class_name in dir(sys.modules['RepositoryModule']):
        if class_name[0].isupper() and class_name != 'Repository':
            result.append(class_name)

    return result

def creat_config(config_name):
    """
    Creat a new config file
    """
    options = get_config_options()
    print("Select one Repository Type : ")
    for index, config_type in enumerate(options):
        print('ID {} = {}'.format(index, config_type))
    choice = int(input("Type ID? : "))
    config = getattr(sys.modules['RepositoryModule'], options[choice]).create_config(config_name)
    #config = LocalRepository.create_config(config_name)
    return config

def clear_file_name(config_name):
    """
    remove illegal char
    """
    error_char = ['<', '>', ':', '\"', '/', '\\', '|', '?', '*']
    for ecr in error_char:
        config_name = config_name.replace(ecr, '_')
    return config_name

def run_game(launch_target,is_steam_game=False):
    import subprocess
    if is_steam_game:
        subprocess.call(["start", launch_target], shell=True)
    else:
        commad_list = ["start", "", "/B", "/WAIT"]
        for parm in sys.argv[1:]:
            commad_list.append(parm)
        subprocess.call(commad_list, shell=True)

def main():
    """
    enter point
    """
    import os
    import subprocess
    import datetime

    #change dir for save config
    script_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(script_path)

    if len(sys.argv) < 2:
        print("No launch target")
        os.system("pause")
        return

    is_steam_game = False
    launch_target = ' '.join(sys.argv[1:])
    config_name = launch_target
    wait_second = 30
    monitor_process_name = ''
    token = sys.argv[1].split('/')
    if token[0] == 'steam:':
        config_name = token[len(token)-1]
        is_steam_game = True

    config_name = clear_file_name(config_name)
    config_file_path = os.path.join("config", "{}.conf".format(config_name))
    config = {}
    if not os.path.exists(config_file_path):
        from json import dump
        config = creat_config(config_name)
        config['launch_target'] = launch_target
        config['wait_second'] = 30
        with open(config_file_path, 'w') as json_file:
            dump(config, json_file)
    else:
        from json import load
        with open(config_file_path, 'r') as json_file:
            config = load(json_file)
    if 'wait_second' in config:
        wait_second = config['wait_second']
    if 'process_name' in config:
        monitor_process_name = config['process_name']

    repository_controller = getattr(sys.modules['RepositoryModule']
                                    , config['RepositoryType'])(config)
    repository_controller.before_launch_game()

    run_game(launch_target, is_steam_game)

    if is_steam_game or monitor_process_name:
        from helper import process_helper
        from time import sleep
        print("wait game launch")
        sleep(wait_second)
        pid = -1

        if is_steam_game:
            from helper import steam_helper
            pid = steam_helper.find_current_steam_game_pid()
        else:
            pid = process_helper.find_launch_game_pid(monitor_process_name)

        if pid == -1:
            print("[error] pid not found !")
            return
        else:
            process_helper.wait_game_terminate(pid)

    repository_controller.exit_game()
    commit_message = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
    repository_controller.backup_save(commit_message)
    os.system("pause")

if __name__ == "__main__":
    main()
