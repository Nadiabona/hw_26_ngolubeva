FROM python:3.7-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

CMD ["gunicorn", "run:app", "-b", "0.0.0.0:25000", "-w", "4"]