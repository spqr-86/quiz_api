#!/bin/sh
sleep 3
docker-compose run web alembic revision -m "Initial migration"
docker-compose run web alembic upgrade head
docker-compose run web alembic revision --autogenerate -m "Initial migration"
exec "$@"
