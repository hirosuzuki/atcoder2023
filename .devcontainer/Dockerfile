FROM python:3.8-slim

RUN apt -y update && apt install -y git
RUN python -m pip install -U flake8 && python -m pip install -U black

ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID dev && useradd -m -u $UID -g $GID dev
USER dev
