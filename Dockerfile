FROM python:3.10-buster

WORKDIR /app

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin::$PATH"

COPY poetry.lock pyproject.toml ./
RUN apt-get update && apt-get install --no-install-recommends -y sudo curl && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -U pip && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev
