#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

echo "==> Setting build flags to prevent memory exhaustion..."
export CMAKE_BUILD_PARALLEL_LEVEL=1

echo "==> Upgrading pip, setuptools, and wheel..."
python -m pip install --upgrade pip setuptools wheel

echo "==> Pre-installing cmake..."
python -m pip install cmake

echo "==> Installing dependencies..."
python -m pip install -r requirements.txt

echo "==> Ensuring face_recognition_models is installed..."
python -m pip install git+https://github.com/ageitgey/face_recognition_models.git

echo "==> Build process completed successfully."
