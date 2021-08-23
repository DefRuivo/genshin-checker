FROM python:3.8-buster

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

# Install pipenv and compilation dependencies
RUN apt-get update && apt-get install -y \
    bash \
    build-essential \
    default-libmysqlclient-dev \
    libmariadb-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    python3-dev \
    python3-pip

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

CMD ["/app/commands/run-prod.sh"]
