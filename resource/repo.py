import os
import sys
import subprocess

from flask_restful import Resource

from ._formatter import Formatter

class Repo(Resource):
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
        # try:
        #     output = subprocess.run(
        #         [ "./bin/scm-git.sh", "status", self.repo, self.work_dir, self.branch ], 
        #         capture_output=True
        #     )
        #     print (output.stdout.decode("ascii"))
        #     print (output.stderr.decode("ascii"))
        #     if output.returncode == 1:
        #         output = subprocess.run(
        #             [ "./bin/scm-git.sh", "setup", self.repo, self.work_dir, self.branch ], 
        #             capture_output=True
        #         )
        #         print (output.stdout.decode("ascii"))
        #         print (output.stderr.decode("ascii"))
        # except:
        #     raise

    def sync(self):
        '''
        Sync the git repo, by performin a pull operation.

        '''
        try:
            output = subprocess.run(
                [ "./bin/scm-git.sh", "sync", self.repo, self.work_dir, self.branch], 
                capture_output=True
            )
            print (output.stdout.decode("ascii"))
            print (output.stderr.decode("ascii"))
        except:
            raise
    
    def post(self):
        try:
            self.sync()
        except:
            return (Formatter(success=False, status_code=500, data=[ "Sync failure" ]).print())
        else:
            return (Formatter(success=True, status_code=201, data=[ "Sync success" ]).print())
    get = post