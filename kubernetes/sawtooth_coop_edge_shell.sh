kubectl exec -it $(kubectl get pods | grep pbft-$1 | awk '{print $1}') --container sawtooth-coop-edge -- bash
