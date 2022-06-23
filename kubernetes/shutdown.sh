#!/bin/bash
kubectl delete -f sawtooth-kubernetes-default-pbft.yaml
kubectl delete jobs pbft-keys
