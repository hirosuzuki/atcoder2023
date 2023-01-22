FROM python:3.8-slim

RUN apt -y update && apt install -y git curl bzip2
RUN python -m pip install -U flake8 && python -m pip install -U black

RUN curl -L https://downloads.python.org/pypy/pypy3.6-v7.3.0-linux64.tar.bz2 | tar xvjf - -C /opt && ln -s /usr/lib/x86_64-linux-gnu/libffi.so.7 /usr/lib/x86_64-linux-gnu/libffi.so.6 && ln -s /lib/x86_64-linux-gnu/libtinfo.so.6 /usr/lib/x86_64-linux-gnu/libtinfo.so.5 && ln -s /opt/pypy3.6-v7.3.0-linux64/bin/pypy3 /usr/local/bin/pypy3

ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID dev && useradd -m -u $UID -g $GID dev
USER dev
