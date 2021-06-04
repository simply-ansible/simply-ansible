'''
Copyright (c) 2021 Kosala Atapattu (@kosalaat)

This is a Flask app to provide a simple GUI and RestAPI for ansible playbooks. This 
script implements the following endpoints:

- GET /playbooks/

List the playbooks. Lists the root of the repo folder for *.yml or *.yaml files (*.y*ml).  

- GET /templates/

Get the parameter 
'''

import os
# from simply_ansible.resource.repo import Repo
import sys
from glob import glob

from flask import Flask
from flask_restful import Api

from resource import SA_Playbook, Repo


app = Flask(__name__,
    static_folder="./static/",
    template_folder="./templates/"
)

func_api = Api(app,)

work_dir = os.environ["WORK_DIR"]
git_repo = os.environ["GIT_REPO"]
branch = os.environ["GIT_BRANCH"]

func_api.add_resource(
    SA_Playbook, 
    "/playbook", 
    "/playbook", 
    resource_class_kwargs={ 
        'work_dir': work_dir, 
        'repo_path': git_repo, 
        'branch': branch
    }
)
func_api.add_resource(
    Repo, 
    "/sync", 
    "/sync", 
    resource_class_kwargs={ 
        'git_repo': git_repo, 
        'work_dir': work_dir, 
        'branch': branch 
    }
)

if __name__ == "__main__":
    app.run(host='0.0.0.0')