#!/bin/bash
set -e

echo "🎵 AI Music Pipeline — Setup for macOS"
echo "========================================"

# Проверка Python 3.10
if ! command -v python3.10 &> /dev/null; then
    echo "❌ Python 3.10 не найден. Установите через pyenv или с официального сайта:"
    echo "   brew install python@3.10"
    exit 1
fi

echo "✅ Python 3.10 найден: $(python3.10 --version)"

# Создание виртуального окружения
if [ ! -d ".venv" ]; then
    echo "📦 Создаём виртуальное окружение..."
    python3.10 -m venv .venv
fi

# Активация
source .venv/bin/activate

# Обновление pip
echo "⬆️  Обновляем pip..."
python -m pip install --upgrade pip

# Установка зависимостей
echo "📥 Устанавливаем Python-зависимости..."
pip install -r requirements.txt

# Установка HeartMuLa (heartlib)
if [ ! -d "orchestrator/heartlib" ]; then
    echo "🫀 Клонируем HeartMuLa (heartlib)..."
    git clone https://github.com/HeartMuLa/heartlib.git orchestrator/heartlib
fi

echo "🔧 Устанавливаем heartlib в режиме editable..."
pip install -e orchestrator/heartlib

# Проверка FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg не найден. Установите:"
    echo "   brew install ffmpeg"
else
    echo "✅ FFmpeg найден"
fi

# Создание .env из примера
if [ ! -f ".env" ]; then
    echo "📝 Создаём .env из шаблона..."
    cp .env.example .env
fi

echo ""
echo "🚀 Установка завершена!"
echo "   Активируйте окружение: source .venv/bin/activate"
echo "   Запустите пайплайн:    ./run.sh"
