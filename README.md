# Introduction
This repository is a proof-of-concept for the CoopEdge research project.
It is a refined and reusable version of the [original prototype](https://github.com/coopedge/prototype).

# Usage Guide
This project is based on Hyperledger Sawtooth and is run on Kubernetes.
First, follow [this guide](https://sawtooth.hyperledger.org/docs/1.2/app_developers_guide/creating_sawtooth_network.html#using-kubernetes-for-a-sawtooth-test-network) and make sure everything works before proceeding.

You have several scripts at your disposal:
* `prepare.sh` - One time use before starting your first cluster. It prepares your environment.
* `upgrade_python.sh` - Upgrades the environment's python version from 3.6 to 3.7. Use only in case the environment's Python version is <3.7.
* `start_cluster.sh` - Starts the cluster.
* `shutdown.sh` - Shuts down the cluster.
* `sawtooth_shell.sh` - Launches a shell on one of the pods (pass an index parameter to choose which pod, 0 by default).

Apart from `sawtooth_shell.sh` and `upgrade_python.sh`, all scripts are idempotent.

This repository is currently a work-in-progress - it works but still very rough around the edges.

Before running any script be sure to modify any hard-coded paths.