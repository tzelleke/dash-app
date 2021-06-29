FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

COPY pyproject.toml /app
RUN pip3 install --upgrade pip \
    && pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev