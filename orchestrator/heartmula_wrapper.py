import os
import sys
import torch

# Добавляем heartlib в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "heartlib", "src"))

# Импорт будет работать после установки heartlib через setup.sh
# from heartlib.inference import HeartMuLaInference


class HeartMuLaWrapper:
    def __init__(self, model_path: str, device: str = "mps", version: str = "3B"):
        self.device = device
        self.model_path = model_path
        self.version = version

        # Для macOS MPS может быть нестабильным с большими моделями
        if device == "mps" and not torch.backends.mps.is_available():
            print("⚠️  MPS недоступен, переключаемся на CPU")
            self.device = "cpu"

        self.model = None

    def load(self):
        print(f"🫀 Загрузка HeartMuLa {self.version} на {self.device}...")
        # TODO: адаптируй под реальный API heartlib после установки
        # self.model = HeartMuLaInference(
        #     model_path=self.model_path,
        #     device=self.device,
        #     version=self.version,
        # )
        print("⚠️  Заглушка: замени на реальный вызов heartlib после установки")

    def generate(
        self,
        lyrics: str,
        tags: str,
        output_path: str,
        duration_ms: int = 30000,
    ):
        if self.model is None:
            self.load()

        print(f"🎶 Генерация трека: {duration_ms}ms")
        # TODO: замени на реальный вызов
        # self.model.generate(
        #     lyrics=lyrics,
        #     tags=tags,
        #     output_path=output_path,
        #     duration_ms=duration_ms,
        # )
        print(f"✅ Сохранено: {output_path}")
        return output_path
