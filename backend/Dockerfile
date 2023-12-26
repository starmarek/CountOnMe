FROM python:3.12

WORKDIR /app

COPY Pipfile .
COPY .env .
COPY Pipfile.lock .
COPY src .

RUN pip install pipenv
RUN pipenv sync

CMD [ "pipenv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0",  "--reload" ] 