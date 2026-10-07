FROM python:3.13-slim

WORKDIR /parking_service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update

RUN apt install -y \
    libasound2t64 \
    libatk1.0-0t64 \
    libcairo2 \
    libcups2t64 \
    libfontconfig1 \
    libgdk-pixbuf-2.0-0 \
    libgtk-3-0t64 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libxss1 \
    fonts-liberation \
    lsb-release \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install

EXPOSE 8000

# CMD 