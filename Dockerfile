FROM  python:3.11.1-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

RUN apt-get -y update; apt-get -y install curl && \
    curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml /app/

RUN /root/.local/bin/poetry config virtualenvs.create false \
    && /root/.local/bin/poetry install --only main --no-ansi --no-interaction

COPY . .
