#!/bin/bash
echo "Generating keys..."
kubectl apply -f sawtooth-create-pbft-keys.yaml
cp pbft-keys-configmap.yaml pbft-keys-configmap_with_keys.yaml
sleep 15
kubectl logs $(kubectl get pods | grep pbft-keys | awk -F"[ ',]+" '/pbft-keys-/{print $1}') | sed 's/^/  /' >>pbft-keys-configmap_with_keys.yaml
echo "Please copy the leader public key (just choose one) from pbft-keys-configmap_with_keys.yaml into sawtooth-poer/src/node.rs:105 and press enter."
read
kubectl apply -f pbft-keys-configmap_with_keys.yaml
kubectl delete jobs pbft-keys

echo "Building the POER engine..."
cd ~/prototype/sawtooth-poer
cargo build
cd -

echo "Copying build files..."
cp ~/prototype/sawtooth-poer/packaging/systemd/sawtooth-pbft-engine.service ~/prototype/kubernetes/poer-engine/packaging/systemd/
cp ~/prototype/sawtooth-poer/packaging/systemd/sawtooth-pbft-engine ~/prototype/kubernetes/poer-engine/packaging/systemd/
cp ~/prototype/sawtooth-poer/target/debug/pbft-engine ~/prototype/kubernetes/poer-engine/target/debug/

echo "Building the image..."
eval $(minikube -p minikube docker-env)
docker build ./poer-engine -t poer_engine:v1

echo "Starting the cluster..."
kubectl apply -f sawtooth-kubernetes-default-pbft.yaml
echo "Done. Use 'kubectl get pods' to check their status or through the web UI using 'minikube dashboard'."