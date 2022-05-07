#! /usr/bin/env sh

#let the DB start
sleep 10;
# Run migrations
alembic upgrade head