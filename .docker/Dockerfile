FROM python:3.9-slim-buster

ENV RT_DIR=/photos_mng

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV POETRY_VERSION=1.2.2 \
    POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"
RUN mkdir -p $RT_DIR
WORKDIR $RT_DIR

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml /photos_mng/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
