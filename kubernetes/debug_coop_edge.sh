#!/bin/bash
docker build ~/prototype/coop_edge -t coop_edge:v1
docker run -it coop_edge:v1 bash
