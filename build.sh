#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

echo "==> Setting build flags to prevent memory exhaustion..."
export CMAKE_BUILD_PARALLEL_LEVEL=1

echo "==> Upgrading pip and wheel, pinning setuptools<70.0.0..."
python -m pip install --upgrade pip wheel
python -m pip install "setuptools<70.0.0"

echo "==> Pre-installing cmake..."
python -m pip install cmake

echo "==> Installing dependencies..."
python -m pip install -r requirements.txt

echo "==> Verifying face_recognition and models installation..."
python -c "import face_recognition; print('==> face_recognition and models loaded successfully!')"

echo "==> Build process completed successfully."
