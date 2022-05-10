# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
COPY requirements.txt /code
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/
COPY docker-compose.yml /code/
COPY entrypoint.sh /code/
ENTRYPOINT ["sh", "entrypoint.sh"]

EXPOSE 8000