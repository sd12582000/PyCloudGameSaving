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

def call_git_fetch(dir_path):
    """
    run git fetch
    return code
    """
    return subprocess.call(["git", "-C", dir_path, "fetch"], shell=True)

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

def call_git_remote_add(dir_path, remote_url, repo_name="origin"):
    """
    run git remote add repo_name remote_url
    """
    return subprocess.call(["git", "-C", dir_path
                            , "remote", "add", repo_name, remote_url], shell=True)

def call_git_clone_inplace(dir_path, remote_url):
    """
    run git clone remote_url .
    """
    return subprocess.call(["git", "-C", dir_path
                            , "clone", remote_url, '.'], shell=True)


def call_git_pull(dir_path, remote="origin", branch="master", force=False):
    """
    run git pull remote branch
    """
    result = -1
    if force:
        result = subprocess.call(["git", "-C", dir_path
                                  , "pull", '-f', remote, branch], shell=True)
    else:
        result = subprocess.call(["git", "-C", dir_path
                                  , "pull", remote, branch], shell=True)
    return result

def call_git_push(dir_path, remote="origin", branch="master", force=False):
    """
    run git push remote branch
    """
    result = -1
    if force:
        result = subprocess.call(["git", "-C", dir_path
                                  , "push", '-f', remote, branch], shell=True)
    else:
        result = subprocess.call(["git", "-C", dir_path
                                  , "push", remote, branch], shell=True)
    return result

def call_git_clean(dir_path, force=False):
    """
    run git clean [-f -d]
    """
    result = -1
    if force:
        result = subprocess.call(["git", "-C", dir_path, "clean", '-f', '-d'], shell=True)
    else:
        result = subprocess.call(["git", "-C", dir_path, "clean"], shell=True)
    return result

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
    dir_path = "D:\\git\\testGit"
    status_code = call_git_push(dir_path)
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
