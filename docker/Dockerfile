# syntax=docker/dockerfile:experimental

FROM centos:centos7.9.2009

# NOTE(crag): NB_USER ARG for mybinder.org compat:
#             https://mybinder.readthedocs.io/en/latest/tutorials/dockerfile.html
ARG NB_USER=notebook-user
ARG NB_UID=1000
ARG PIP_VERSION
ARG PIPELINE_FAMILY

ENV DEBIAN_FRONTEND=noninteractive

RUN yum update -y
RUN yum upgrade -y

RUN yum install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev git mesa-libGL

RUN yum -y install gcc openssl-devel bzip2-devel libffi-devel make git sqlite-devel && \
  curl -O https://www.python.org/ftp/python/3.8.15/Python-3.8.15.tgz && tar -xzf Python-3.8.15.tgz && \
  cd Python-3.8.15/ && ./configure --enable-shared --enable-optimizations && make altinstall && \
  cd .. && rm -rf Python-3.8.15* && \
  ln -s /usr/local/bin/python3.8 /usr/local/bin/python3

COPY lib/libstdc++.so.6 /usr/lib64

# create user with a home directory
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN groupadd --gid ${NB_UID} ${NB_USER}
RUN useradd --uid ${NB_UID}  --gid ${NB_UID} ${NB_USER}
USER ${NB_USER}
WORKDIR ${HOME}
ENV PYTHONPATH="${PYTHONPATH}:${HOME}"
ENV PATH="/home/${NB_USER}/.local/bin:${PATH}"
ENV LD_LIBRARY_PATH=/usr/local/lib
ENV LD_LIBRARY_PATH=/usr/lib64:$LD_LIBRARY_PATH

COPY requirements/dev.txt requirements-dev.txt
COPY requirements/base.txt requirements-base.txt
COPY prepline_${PIPELINE_FAMILY}/ prepline_${PIPELINE_FAMILY}/
COPY exploration-notebooks exploration-notebooks
COPY pipeline-notebooks pipeline-notebooks
COPY img/ img/

#RUN echo 'export LD_LIBRARY_PATH=/usr/local/lib' >> ~/.bashrc

RUN python3 -m pip install --no-cache -r requirements-base.txt \
  && python3 -m pip install --no-cache -r requirements-dev.txt

