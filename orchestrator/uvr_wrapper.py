import os
from audio_separator.separator import Separator


class UVRWrapper:
    def __init__(self, model_dir: str = "./models", output_format: str = "wav"):
        self.model_dir = model_dir
        self.output_format = output_format
        self.separator = None

    def load(self, model_filename: str = "model_bs_roformer_ep_317_sdr_12.9755.ckpt"):
        print(f"🎛️  Загрузка UVR-модели: {model_filename}")
        self.separator = Separator(
            output_dir=None,
            output_format=self.output_format,
            model_file_dir=self.model_dir,
        )
        self.separator.load_model(model_filename=model_filename)

    def separate(self, input_path: str, output_dir: str) -> list[str]:
        if self.separator is None:
            self.load()

        self.separator.output_dir = output_dir
        print(f"🔪 Разделение стемов: {input_path}")
        output_files = self.separator.separate(input_path)
        print(f"✅ Стемы сохранены в: {output_dir}")
        return output_files
