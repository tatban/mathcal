ARG BASE_IMAGE=python:3-slim-buster
FROM ${BASE_IMAGE} AS base


ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update \
    && apt-get install -y curl



# Create app directory
WORKDIR /app

# Copy the files
COPY requirements.txt /app/
COPY eval_logic.py /app/
COPY main.py /app/
# RUN cp -r ./* /app/

#install the dependecies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN cp ./eval_logic.py /app/
# RUN cp ./main.py /app/

# EXPOSE 38080
CMD ["uvicorn", "main:app", "--port", "38080", "--host", "0.0.0.0"]
