FROM ubuntu:bionic

RUN apt update \
    && apt install gnupg -y

RUN echo "deb http://repo.sawtooth.me/ubuntu/nightly bionic universe" >> /etc/apt/sources.list \
    && (apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 44FC67F19B2466EA \
    || apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 44FC67F19B2466EA) \
    && apt update

RUN apt install -y -q \
    git \
    python3 \
    python3-stdeb \
    vim \
    curl \
    python3-grpcio \
    python3-grpcio-tools \
    python3-protobuf \
    python3-cbor \
    python3-colorlog \
    python3-secp256k1 \
    python3-toml \
    python3-yaml \
    python3-zmq \
    python3-pip

RUN python3 -m pip install sawtooth-sdk cbor colorlog

COPY coop_edge /home/coop_edge

WORKDIR /home

CMD python3 -u -m coop_edge.processor.transaction_processor