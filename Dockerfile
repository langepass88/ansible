FROM python:3.8.5-slim-buster

# Install new packages
RUN apt-get update && apt-get install -y ssh sshpass
# Upgrade pip
RUN pip install --upgrade pip
# Install ansible
ARG ANSIBLE_VERSION=2.10.5

RUN pip install ansible==$ANSIBLE_VERSION

# Change LIBRARY_PATHH environment variable because of error in building zlib
ENV LIBRARY_PATHH=/lib:/usr/lib

# Set Workdir
WORKDIR /ansible
COPY ./ /ansible
#Define volumes
VOLUME [ "/ansible" ]
