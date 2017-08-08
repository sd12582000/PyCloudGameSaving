"""
process helper
"""
import psutil

def find_launch_game_pid(process_name):
    """
    find current play game process id with process_name
    if not find return -1
    """
    target_pid = -1
    for proc in psutil.process_iter():
        try:
            if proc.name() == process_name:
                return proc.pid
        except psutil.AccessDenied:
            print("Permission error or access denied on process")
    return target_pid

def wait_game_terminate(pid):
    """
    process waiting
    """
    game_process = psutil.Process(pid)
    print("waiting {} ({}) terminate".format(game_process.name(), pid))
    game_process.wait()
    print("game terminate")

def print_all_porcess():
    """
    print all current porcess name & pid
    """
    for proc in psutil.process_iter():
        print("[{}] - {}".format(proc.name(), proc.pid))

def main():
    """
    test
    """
    print_all_porcess()

if __name__ == "__main__":
    main()
