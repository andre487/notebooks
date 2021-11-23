#!/usr/bin/env bash
set -eufo pipefail

cd "$(dirname "$0")"
export FLASK_APP=main
.venv/bin/python -m flask run
