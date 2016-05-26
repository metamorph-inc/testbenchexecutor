'''
Build with:
setup.py bdist_wheel
or install in editable mode with
Scripts\pip install -e path\to\testbenchexecutor
'''
from __future__ import absolute_import
from setuptools import setup

setup(
    name='testbenchexecutor',
    version='0.1.3',
    author='MetaMorph Software, Inc',
    author_email='adam@metamorphsoftware.com',
    description='Executes the steps in a Test Bench manifest',
    packages=['testbenchexecutor'],
    package_dir={'testbenchexecutor': 'testbenchexecutor'},
    entry_points = {
        "console_scripts": [
            "testbenchexecutor = testbenchexecutor.__main__:main",
        ]
    }
)
