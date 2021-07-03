#! /bin/sh

uvicorn app.main:app --reload --port `echo $HTTP_PORT` --host 0.0.0.0