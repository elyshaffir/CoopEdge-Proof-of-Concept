import os
import subprocess

from setuptools import setup, find_packages


data_files = []

if os.path.exists("/etc/default"):
    data_files.append(
        ('/etc/default', ['systemd/coop-edge']))

if os.path.exists("/lib/systemd/system"):
    data_files.append(
        ('/lib/systemd/system',
         ['systemd/coop-edge.service']))

setup(
    name='sawtooth-coop-edge',
    description='Sawtooth CoopEdge',
    author='Ely Shaffir',
    packages=find_packages(),
    install_requires=[
        "sawtooth-sdk"
    ],
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'coop-edge-cli = coop_edge.client.coop_edge_client:main',
            'coop-edge-tp = coop_edge.processor.transaction_processor:main'
        ]
    })
