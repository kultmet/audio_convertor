FROM python:3.11-slim
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN apt-get update && apt-get install -y ffmpeg