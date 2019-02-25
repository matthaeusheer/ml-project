import os
import shutil
from git import Repo
import subprocess

from common import PROJECT_ROOT_PATH

"""
Small helper script which installs python dependencies that cannot be directly installed via pip
but need to be installed from source.
"""

DEPENDENCIES = {'pipelinehelper': 'https://github.com/bmurauer/pipelinehelper.git'}
DEPENDENCIES_DIR = os.path.join(PROJECT_ROOT_PATH, 'dependencies')


def setup_dependency_folder():

    shutil.rmtree(DEPENDENCIES_DIR)
    os.mkdir(DEPENDENCIES_DIR)


def clone_dependencies_from_git():

    setup_dependency_folder()

    for depend_name, git_url in DEPENDENCIES.items():

        print('Fetching dependency: {}...'.format(depend_name))

        Repo.clone_from(git_url, os.path.join(DEPENDENCIES_DIR, depend_name))


def install_python_dependencies():

    for dep_dir in os.listdir(DEPENDENCIES_DIR):

        try:
            dep_path = os.path.join(DEPENDENCIES_DIR, dep_dir)

            subprocess.call('pip install -e {}'.format(dep_path), shell=True)
        except:
            pass


if __name__ == '__main__':
    setup_dependency_folder()
    clone_dependencies_from_git()
    install_python_dependencies()
