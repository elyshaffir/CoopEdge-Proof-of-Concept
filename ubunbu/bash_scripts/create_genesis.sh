#!/bin/bash
cd /tmp
sawset genesis --key $HOME/.sawtooth/keys/my_key.priv \
    -o config-genesis.batch
sawset proposal create --key $HOME/.sawtooth/keys/my_key.priv \
    -o config-consensus.batch \
    sawtooth.consensus.algorithm.name=pbft \
    sawtooth.consensus.algorithm.version=1.0 \
    sawtooth.consensus.pbft.members='["VAL1KEY","VAL2KEY",...,"VALnKEY"]'
# TODO replace with outputs of create_keys.sh of all nodes including this one

# TODO is this necessary? this was collected from sawtooth_settings.txt
# sawset proposal create --key $HOME/.sawtooth/keys/vy.priv \
# -o pbft-settings.batch \
# sawtooth.consensus.pbft.forced_view_change_interval=1000

sudo -u sawtooth sawadm genesis \
    config-genesis.batch config-consensus.batch pbft-settings.batch
