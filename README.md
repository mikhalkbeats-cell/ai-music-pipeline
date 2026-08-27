# AI Music Pipeline — macOS Version

## Установка

```bash
# 1. Клонируй репозиторий
git clone https://gitlab.com/mikhalkbeats/hse.git
cd hse

# 2. Запусти установку (требуется Python 3.10)
./setup.sh

# 3. Активируй окружение
source .venv/bin/activate
```

## Запуск

Создай jobs в папке `jobs/`:

```
jobs/my_track/
├── source/
│   ├── lyrics.txt      # текст песни
│   └── tags.txt        # теги (например: piano,happy,wedding)
├── mixed/              # сгенерированный трек (создаётся автоматически)
└── stems/              # разделённые стемы (создаются автоматически)
```

Запуск:
```bash
./run.sh my_track
# или с кастомной длительностью:
./run.sh my_track --duration 45000
```

## Зависимости

- **HeartMuLa** — генерация музыки: https://github.com/HeartMuLa/heartlib
- **UVR** — разделение стемов через `audio-separator`: https://github.com/nomadkaraoke/python-audio-separator

## macOS-специфика

- Используется `mps` (Metal Performance Shaders) для Apple Silicon
- Для Intel Mac автоматически fallback на `cpu`
- Модели скачиваются автоматически при первом запуске
