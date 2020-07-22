FROM python:3.7
LABEL maintainer="Dotkom <dotkom@online.ntnu.no>"

ENV POETRY_VIRTUALENVS_CREATE=false

# Install deps
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get remove -y curl && apt-get install -y --no-install-recommends \
    nodejs libjpeg-dev ghostscript && \
    npm install -g less && \
    npm install -g yarn && \
    pip install poetry

# Clean up
RUN rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
