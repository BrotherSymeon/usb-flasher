#!/bin/bash
set -euxo pipefail

poetry run isort usb-flasher/ tests/
poetry run black usb-flasher/ tests/
