# Introduction
This repository is a proof-of-concept for the CoopEdge research project.
It is a refined and reusable version of the [original prototype](https://github.com/coopedge/prototype).

# Usage Guide
This project is based on Hyperledger Sawtooth and is run on Kubernetes.
First, follow [this guide](https://sawtooth.hyperledger.org/docs/1.2/app_developers_guide/creating_sawtooth_network.html#using-kubernetes-for-a-sawtooth-test-network) and make sure everything works before proceeding.

You have several scripts at your disposal:
* `prepare.sh` - One time use before starting your first cluster. It prepares your environment.
* `start_cluster.sh` - Starts the cluster.
* `shutdown.sh` - Shuts down the cluster.
* `sawtooth_shell.sh` - Launches a shell on one of the pods (pass an index parameter to choose which pod, 0 by default).

Apart from `sawtooth_shell.sh`, all scripts are idempotent.