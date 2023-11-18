FROM debian:latest

LABEL image.author.name "ThankGod Ebenezer"
LABEL image.author.email "tee25@cam.ac.uk"

MAINTAINER "ThankGod Ebenezer"

# define environment variables
ENV MINICONDA_DIR /opt/miniconda/
ENV BIN_LOCAL /usr/local/bin/


# Add environment variable to path
ENV PATH=$MINICONDA_DIR/bin:$PATH
ENV PATH=$BIN_LOCAL/bin/:$PATH

# Install base utilities for
RUN apt update && \
    apt install -y build-essential  && \
    apt install -y wget && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Install anaconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/miniconda/

# install python
RUN apt update && \
    apt install -y python3
#
## install pip
#RUN conda update conda
#RUN conda install -c anaconda pip

#creating a working directory
WORKDIR /my_directory

## install python packages or dependencies
#RUN source /home/tee25/Desktop/assessment/naturemetrics/read_mapping_validation/mapping_validation_python/venv/bin/activate
