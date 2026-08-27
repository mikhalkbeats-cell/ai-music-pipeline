#!/usr/bin/env python3
import os
import sys
import argparse

from config import JOBS_DIR, MODELS_DIR, DEVICE, DEFAULT_DURATION_MS
from utils import ensure_dir, write_meta, read_prompts
from heartmula_wrapper import HeartMuLaWrapper
from uvr_wrapper import UVRWrapper


def run_pipeline(job_name: str, duration_ms: int = DEFAULT_DURATION_MS):
    job_dir = os.path.join(JOBS_DIR, job_name)
    mixed_dir = os.path.join(job_dir, "mixed")
    source_dir = os.path.join(job_dir, "source")
    stems_dir = os.path.join(job_dir, "stems")

    ensure_dir(mixed_dir)
    ensure_dir(source_dir)
    ensure_dir(stems_dir)

    # Читаем промпты
    lyrics, tags = read_prompts(job_dir)

    if not lyrics:
        print(f"❌ Не найден lyrics.txt в {source_dir}")
        sys.exit(1)

    # 1. Генерация через HeartMuLa
    heartmula = HeartMuLaWrapper(model_path=MODELS_DIR, device=DEVICE)
    mixed_path = os.path.join(mixed_dir, f"{job_name}_mixed.wav")

    heartmula.generate(
        lyrics=lyrics,
        tags=tags,
        output_path=mixed_path,
        duration_ms=duration_ms,
    )

    # 2. Разделение на стемы через UVR
    uvr = UVRWrapper(model_dir=MODELS_DIR)
    uvr.separate(mixed_path, stems_dir)

    # 3. Сохраняем метаданные
    write_meta(job_dir, {
        "job_name": job_name,
        "duration_ms": duration_ms,
        "lyrics": lyrics[:200] + "..." if len(lyrics) > 200 else lyrics,
        "tags": tags,
        "mixed": mixed_path,
        "stems_dir": stems_dir,
    })

    print(f"\n🎉 Пайплайн завершён! Результаты в: {job_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Music Pipeline")
    parser.add_argument("job_name", help="Имя джобы (папка в ./jobs)")
    parser.add_argument("--duration", type=int, default=DEFAULT_DURATION_MS, help="Длительность в мс")
    args = parser.parse_args()

    run_pipeline(args.job_name, args.duration)
