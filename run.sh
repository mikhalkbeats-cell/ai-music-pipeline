#!/bin/bash
set -e

# Активация окружения
source .venv/bin/activate

# Запуск пайплайна
echo "🎵 Запуск AI Music Pipeline..."
python orchestrator/pipeline.py "$@"
