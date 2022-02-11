#!/bin/bash


isort app
black app
autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place app