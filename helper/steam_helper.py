"""
steam game helper
"""
import psutil
def get_stream_game_title(appid):
    """
    get appdetails
    """
    import requests
    url = "http://store.steampowered.com/api/appdetails?appids={}".format(appid)
    appdetails = requests.get(url)
    if appdetails.status_code != 200:
        return appid

    json_data = appdetails.json()[appid]
    if json_data['success']:
        return json_data['data']['name']
    return appid

def find_current_steam_game_pid():
    """
    find current play game process id with GameOverlayUI.exe
    if not find return -1
    """
    target_pid = -1
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'GameOverlayUI.exe':
                cmds = proc.cmdline()
                for index, arg in enumerate(cmds):
                    if arg == '-pid':
                        target_pid = int(cmds[index+1])
                        break
                break
        except psutil.AccessDenied:
            print("Permission error or access denied on process")
    return target_pid

def main():
    """
    test
    """
    target_pid = find_current_steam_game_pid()
    if target_pid != -1:
        from . import process_helper 
        process_helper.wait_game_terminate(target_pid)
    else:
        print("no game start")

if __name__ == "__main__":
    main()
    