#!/bin/bash



isort --check-only app
black app --check
flake8 app
vulture app --min-confidence 70
mypy app
