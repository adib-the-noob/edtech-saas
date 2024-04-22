# pull a base python image
FROM python:3.10-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install dependencies
COPY ./requirements_windows.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --cache-dir .pip-cache -r requirements_windows.txt && \
    rm -rf .pip-cache

# copy run.sh
COPY ./run.sh .
RUN chmod +x /app/run.sh

# copy project
COPY . .