FROM mcr.microsoft.com/playwright/python:v1.60.0-noble

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

CMD ["poetry", "run", "pytest"]