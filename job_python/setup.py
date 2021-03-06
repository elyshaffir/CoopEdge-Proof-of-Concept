# Copyright 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

from __future__ import print_function

import os
import subprocess

from setuptools import setup, find_packages

conf_dir = "/etc/sawtooth"
abs_dir = "/home/job_python"

data_files = [
    (conf_dir, [f'{abs_dir}/packaging/job.toml.example'])
]

if os.path.exists("/etc/default"):
    data_files.append(
        ('/etc/default', [f'{abs_dir}/packaging/systemd/sawtooth-job-tp-python']))

if os.path.exists("/lib/systemd/system"):
    data_files.append(('/lib/systemd/system',
                       [f'{abs_dir}/packaging/systemd/sawtooth-job-tp-python.service']))

setup(
    name='sawtooth-job',
    # version=subprocess.check_output(
    #      ['./get_version']).decode('utf-8').strip(),
    description='Sawtooth JOB Example',
    author='Hyperledger Sawtooth',
    url='https://github.com/hyperledger/sawtooth-sdk-python',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'colorlog',
        'protobuf',
        'sawtooth-sdk',
        'PyYAML',
        'cbor',
        'psutil'
        'requests'
    ],
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'job = sawtooth_job.job_cli:main_wrapper',
            'job-tp-python = sawtooth_job.processor.main:main',
        ]
    })
