import os

from setuptools import setup, find_packages

abs_dir = "/home/coop_edge"

data_files = []

if os.path.exists("/etc/default"):
    data_files.append(
        ('/etc/default', [f'{abs_dir}/systemd/coop_edge']))

if os.path.exists("/lib/systemd/system"):
    data_files.append(('/lib/systemd/system',
                       [f'{abs_dir}/systemd/coop_edge.service']))

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
