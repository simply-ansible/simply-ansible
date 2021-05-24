import os
import sys
from glob import glob
from .repo import Repo

class SA_Playbook():
    def __init__(self, repo_path, work_dir, branch=''):
        '''
        repo_path: path to the ansible playbooks. Root folder of the playbooks.
        '''
        self.repo_path = repo_path
        self._Repo = Repo(repo_path, work_dir, branch)
        try:
            self._Repo.sync()
        except:
            raise

    def get(self):
        '''
        GET method for SA_playbook

        returns: a list of playbooks for ex. ['playbook1.yml','playbook2.yml']
        '''

        return glob(self.repo_path + '/*.y*ml')

    def post(self, **kwargs):
        '''
        Run the playbook. 
        '''
        playbook_params = []
        pass