import os
import sys
from glob import glob
from .repo import Repo
from ._formatter import Formatter
from flask_restful import Resource

class SA_Playbook(Resource):
    def __init__(self, repo_path, work_dir, branch=''):
        '''
        repo_path: path to the ansible playbooks. Root folder of the playbooks.
        '''
        self.work_dir = work_dir
        self._Repo = Repo(repo_path, work_dir, branch)

    def get(self):
        '''
        GET method for SA_playbook

        returns: a list of playbooks for ex. ['playbook1.yml','playbook2.yml']
        '''

        play_list = glob(self.work_dir + '/*.y*ml')

        if play_list == []:
            try:
                self._Repo.sync()
            except:
                return Formatter(success=False, status_code=500, data=[]).print()
            else:
                return Formatter(success=True, status_code=200, data=glob(self.work_dir + '/*.y*ml')).print()
        else: 
            return Formatter(success=True, status_code=200, data=play_list).print()

    def post(self, **kwargs):
        '''
        Run the playbook. 
        '''
        playbook_params = []
        pass