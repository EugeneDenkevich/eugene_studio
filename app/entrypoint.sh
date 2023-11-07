#!/bin/sh
echo "Running create_roles.py"
python app/src/create_roles.py

echo "Starting FastAPI application"
uvicorn app:create_app --host 0.0.0.0 --port 8000 --reload