#!/bin/bash
echo "Generating keys..."
kubectl apply -f sawtooth-create-pbft-keys.yaml
cp pbft-keys-configmap.yaml pbft-keys-configmap_with_keys.yaml
echo "Waiting until the newly created keys pod starts running..."
sleep 10
kubectl logs $(kubectl get pods | grep pbft-keys | awk -F"[ ',]+" '/pbft-keys-/{print $1}') | sed 's/^/  /' >>pbft-keys-configmap_with_keys.yaml
echo "Please copy the leader public key (just choose one) from pbft-keys-configmap_with_keys.yaml into sawtooth-poer/src/node.rs:105 and press enter."
read
kubectl apply -f pbft-keys-configmap_with_keys.yaml
kubectl delete jobs pbft-keys

echo "Building the POER engine..."
cd ~/prototype/sawtooth-poer
cargo build
cd -

echo "Copying POER build files..."
cp ~/prototype/sawtooth-poer/packaging/systemd/sawtooth-pbft-engine.service ~/prototype/kubernetes/poer-engine/packaging/systemd/
cp ~/prototype/sawtooth-poer/packaging/systemd/sawtooth-pbft-engine ~/prototype/kubernetes/poer-engine/packaging/systemd/
cp ~/prototype/sawtooth-poer/target/debug/pbft-engine ~/prototype/kubernetes/poer-engine/target/debug/

echo "Copying job-python files..."
cp -R ~/prototype/job_python ~/prototype/kubernetes/job-python/
cp -R ~/prototype/job_python ~/prototype/kubernetes/poer-engine/

echo "Building the POER engine image..."
eval $(minikube -p minikube docker-env)
docker build ~/prototype/kubernetes/poer-engine -t poer_engine:v1

echo "Building the job-python image..."
docker build ~/prototype/kubernetes/job-python -t job_python:v1

echo "Building the client image..."
docker build ~/prototype/kubernetes/client_docker -t job_python_client:v1

echo "Building the server image..."
docker build ~/prototype/kubernetes/server_docker -t job_python_server:v1

echo "Starting the cluster..."
kubectl apply -f sawtooth-kubernetes-default-pbft.yaml
echo "Done. Use 'kubectl get pods' to check their status or through the web UI using 'minikube dashboard'."
