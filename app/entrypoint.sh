#!/bin/sh
cd ./app/src/internal/database
alembic  upgrade head

cd ../..
python create_roles.py

cd ../..
echo "Starting FastAPI application"
uvicorn app:create_app --host 0.0.0.0 --port 8000 --reload
