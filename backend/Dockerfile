FROM python:3.10-slim

ARG FOR_DEVELOPMENT=false
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl build-essential

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

WORKDIR /app
COPY ./backend /app/

# Allow installing dev dependencies to run tests
RUN bash -c "if [ $FOR_DEVELOPMENT == 'true' ] ; then poetry install; else poetry install --only main ; fi"