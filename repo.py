import os
import sys
import subprocess

class Repo ():
    def __init__(self, git_repo, work_dir, branch=''):
        '''
        Initialize the Git Repo.

        git_repo: URI for the git repository
        work_dir: directory where the playbooks will be cloned to.
        branch: branch of the project to work on
        '''
        self.repo = git_repo
        self.work_dir = work_dir
        self.branch = branch

        # setup git repo
        try:
            output = subprocess.run(
                [ "./scm-git.sh", "setup", self.repo, self.work_dir, self.branch], 
                check_output=True
            )
            print (output.stdout.decode("ascii"))
            print (output.stderr.decode("ascii"))
        except:
            raise

    def sync(self):
        '''
        Sync the git repo, by performin a pull operation.

        '''
        try:
            output = subprocess.run(
                [ "./scm-git.sh", "sync", self.repo, self.work_dir, self.branch], 
                check_output=True
            )
            print (output.stdout.decode("ascii"))
            print (output.stderr.decode("ascii"))
        except:
            raise
        