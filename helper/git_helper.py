"""
run git command
"""
import subprocess
def call_git_status(dir_path, shell=True):
    """
    run git status
    return code
    """
    return subprocess.call(["git", "-C", dir_path, "status"], shell=shell)

def call_git_fetch(dir_path, shell=True):
    """
    run git fetch
    return code
    """
    return subprocess.call(["git", "-C", dir_path, "fetch"], shell=shell)

def call_git_init(dir_path, shell=True):
    """
    run init
    """
    return subprocess.call(["git", "-C", dir_path, "init"], shell=shell)

def call_git_add_all(dir_path, shell=True):
    """
    run git add .
    don't do this in real world
    """
    return subprocess.call(["git", "-C", dir_path, "add", "."], shell=shell)

def call_git_remote_add(dir_path, remote_url, repo_name="origin", shell=True):
    """
    run git remote add repo_name remote_url
    """
    return subprocess.call(["git", "-C", dir_path
                            , "remote", "add", repo_name, remote_url], shell=shell)

def call_git_clone_inplace(dir_path, remote_url, shell=True):
    """
    run git clone remote_url .
    """
    return subprocess.call(["git", "-C", dir_path
                            , "clone", remote_url, '.'], shell=shell)


def call_git_pull(dir_path, remote="origin", branch="master", force=False, shell=True):
    """
    run git pull remote branch
    """
    result = -1
    if force:
        result = subprocess.call(["git", "-C", dir_path
                                  , "pull", '-f', remote, branch], shell=shell)
    else:
        result = subprocess.call(["git", "-C", dir_path
                                  , "pull", remote, branch], shell=shell)
    return result

def call_git_push(dir_path, remote="origin", branch="master", force=False, shell=True):
    """
    run git push remote branch
    """
    result = -1
    if force:
        result = subprocess.call(["git", "-C", dir_path
                                  , "push", '-f', remote, branch], shell=shell)
    else:
        result = subprocess.call(["git", "-C", dir_path
                                  , "push", remote, branch], shell=shell)
    return result

def call_git_clean(dir_path, force=False, shell=True):
    """
    run git clean [-f -d]
    """
    result = -1
    if force:
        result = subprocess.call(["git", "-C", dir_path, "clean", '-f', '-d'], shell=shell)
    else:
        result = subprocess.call(["git", "-C", dir_path, "clean"], shell=shell)
    return result

def call_git_commit(dir_path, commit_message, shell=True):
    """
    run git commit -m commit_message
    """
    return subprocess.call(["git", "-C", dir_path, "commit", "-m", commit_message], shell=shell)

def main():
    """
    test
    """
    import datetime
    dir_path = "/Users/OldNick/test_s"
    status_code = call_git_init(dir_path,shell=False)
    print(status_code)
    if status_code != 0:
        print("not code")
        #call_git_init(dir_path)
    else:
        print("ok")
    #add_message = call_git_add_all(dir_path)
    #print(add_message)
    #print(call_git_commit(dir_path, "commit message {0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())))

if __name__ == "__main__":
    main()
