import os
import json
from pathlib import Path


def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)


def write_meta(job_dir: str, data: dict):
    ensure_dir(job_dir)
    with open(os.path.join(job_dir, "meta.json"), "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def read_prompts(job_dir: str) -> tuple[str, str]:
    lyrics_path = os.path.join(job_dir, "source", "lyrics.txt")
    tags_path = os.path.join(job_dir, "source", "tags.txt")

    lyrics = ""
    tags = ""

    if os.path.exists(lyrics_path):
        with open(lyrics_path, "r") as f:
            lyrics = f.read().strip()

    if os.path.exists(tags_path):
        with open(tags_path, "r") as f:
            tags = f.read().strip()

    return lyrics, tags
