FROM debian:latest

LABEL image.author.name "ThankGod Ebenezer"
LABEL image.author.email "tee25@cam.ac.uk"

MAINTAINER "ThankGod Ebenezer"

# Install base utilities for
RUN apt update && \
    apt install -y build-essential  && \
    apt install -y wget && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# install python
RUN apt update && \
    apt install -y python3 && \
    apt install -y python3-pip && \
    apt install -y python3.11-venv






