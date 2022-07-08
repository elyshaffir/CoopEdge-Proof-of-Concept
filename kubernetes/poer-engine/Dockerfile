FROM ubuntu:bionic
#ADD file:e80ae8d359b484dac5346f98c549abc694e1d0c87e1d9753d495aed4d9c8b2b3 in /
RUN set -xe \
   &&  echo '#!/bin/sh' > /usr/sbin/policy-rc.d \
   &&  echo 'exit 101' >> /usr/sbin/policy-rc.d \
   &&  chmod +x /usr/sbin/policy-rc.d \
   &&  dpkg-divert --local --rename --add /sbin/initctl \
   &&  cp -a /usr/sbin/policy-rc.d /sbin/initctl \
   &&  sed -i 's/^exit.*/exit 0/' /sbin/initctl \
   &&  echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup \
   &&  echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean \
   &&  echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean \
   &&  echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean \
   &&  echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages \
   &&  echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
   &&  echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests
RUN [ -z "$(apt-get indextargets)" ]
RUN mkdir -p /run/systemd \
   &&  echo 'docker' > /run/systemd/container
LABEL install-type=repo
RUN apt-get update \
   &&  apt-get install software-properties-common -y \
   &&  add-apt-repository ppa:deadsnakes/ppa -y \
   &&  apt-get update \
   &&  apt-get install python3.7 -y \
   &&  apt-get install python3-pip -y \
   &&  update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1 \
   &&  update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2 \
   &&  apt-get install python3.7-dev -y \
   &&  apt-get install libpython3.7-dev -y \
   &&  apt-get install libffi-dev -y \
   &&  apt-get install gnupg -y \
   &&  pip3 install aiohttp colorlog protobuf sawtooth-sdk PyYAML cbor psutil requests
RUN echo "deb [arch=amd64] http://repo.sawtooth.me/ubuntu/nightly bionic universe" >> /etc/apt/sources.list \
   &&  (apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 44FC67F19B2466EA || apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 44FC67F19B2466EA) \
   &&  apt-get update \
   &&  apt-get install -y -q sawtooth-pbft-engine \
   &&  apt-get install vim curl -y \
   &&  apt-get clean \
   &&  rm -rf /var/lib/apt/lists/*
ENV PYTHONPATH="${PYTHONPATH}:/home/job_python"
WORKDIR /home/job_python/sawtooth_job/
COPY development /home/development
COPY job_python /home/job_python
COPY packaging/systemd/sawtooth-pbft-engine.service /lib/systemd/system
COPY packaging/systemd/sawtooth-pbft-engine /etc/default
COPY reputation.log /home
COPY target/debug/pbft-engine /usr/bin
