#!/usr/bin/env bash

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-4444}

uvicorn app.main:app --host $HOST --port $PORT --reload
