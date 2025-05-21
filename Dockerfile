FROM python:3.10-alpine

WORKDIR /kodekloud-twelve-factor-app

COPY requirements.txt /kodekloud-twelve-factor-app

RUN pip install -r requirements.txt --no-cache-dir

COPY . /kodekloud-twelve-factor-app

CMD python app.py
