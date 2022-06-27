#!/bin/bash
cp -R ~/prototype/job_python ~/prototype/kubernetes/job-python/
docker build ~/prototype/kubernetes/job-python -t job_python:v1
docker run -it job_python:v1 bash
