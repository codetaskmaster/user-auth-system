FROM python:3.12.3-slim

WORKDIR /app

# install required packages for system
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install mysqlclient
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_APP=run.py

CMD ["python", "run.py"]