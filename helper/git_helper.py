"""
run git command
"""
import subprocess
def call_git_status(dir_path):
    """
    run git status
    return code
    """
    return subprocess.call(["git", "-C", dir_path, "status"], shell=True)

def call_git_init(dir_path):
    """
    run init
    """
    return subprocess.call(["git", "-C", dir_path, "init"], shell=True)

def call_git_add_all(dir_path):
    """
    run git add .
    don't do this in real world
    """
    return subprocess.call(["git", "-C", dir_path, "add", "."], shell=True)

def call_git_commit(dir_path, commit_message):
    """
    run git commit -m commit_message
    """
    return subprocess.call(["git", "-C", dir_path, "commit", "-m", commit_message], shell=True)

def main():
    """
    test
    """
    import datetime
    dir_path = "D:\\git\\test\\save"
    status_code = call_git_status(dir_path)
    print(status_code)
    if status_code != 0:
        call_git_init(dir_path)
    else:
        print("ok")
    add_message = call_git_add_all(dir_path)
    print(add_message)
    print(call_git_commit(dir_path, "commit message {0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())))

if __name__ == "__main__":
    main()
