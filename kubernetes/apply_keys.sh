#!/bin/bash
kubectl apply -f sawtooth-create-pbft-keys.yaml
cp pbft-keys-configmap.yaml pbft-keys-configmap_with_keys.yaml
sleep 5
kubectl logs $(kubectl get pods | grep pbft-keys | awk -F"[ ',]+" '/pbft-keys-/{print $1}') | sed 's/^/  /' >>pbft-keys-configmap_with_keys.yaml
kubectl apply -f pbft-keys-configmap_with_keys.yaml
kubectl delete jobs pbft-keys
rm pbft-keys-configmap_with_keys.yaml
