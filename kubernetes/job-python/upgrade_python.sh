#!/bin/bash
# This script should be used in case the python version in the host machine is lower than 3.7.
add-apt-repository ppa:deadsnakes/ppa -y
apt-get update
apt-get install python3.7 -y
apt install python3-pip -y
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
