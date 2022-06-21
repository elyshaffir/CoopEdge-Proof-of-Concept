#!/bin/bash
sawtooth keygen my_key
sudo sawadm keygen
cat /etc/sawtooth/keys/validator.pub
