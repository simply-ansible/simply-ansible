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
import sys
from glob import glob

from flas import Flask

from playbooks import _Playbook

