#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports usb-flasher/
poetry run isort --check --diff usb-flasher/ tests/
poetry run black --check usb-flasher/ tests/
poetry run flake8 usb-flasher/ tests/
poetry run safety check -i 39462 -i 40291
poetry run bandit -r usb-flasher/
