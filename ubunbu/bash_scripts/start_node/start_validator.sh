#!/bin/bash
# TODO replace with actual values
sudo -u sawtooth sawtooth-validator \
    --bind component:{component-bind-string} \
    --bind network:{network-bind-string} \
    --bind consensus:{consensus-bind-string} \
    --endpoint {public-endpoint-string} \
    --peers {peer-list} # TODO does this replace step 4?
