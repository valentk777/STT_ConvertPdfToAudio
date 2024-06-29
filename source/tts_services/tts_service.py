# -------------------------------------------------------
# This is a new version of TTS using TTS lib
# -------------------------------------------------------
from time import sleep
from typing import List

from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

from source.logging_utils import get_logger
from source.models import TextPart
from source.tts_services.tts_service_base import TtsServiceBase

logger = get_logger()

path = r"C:\Users\Valentinas\AppData\Local\Programs\Python\Python311\Lib\site-packages\TTS\.models.json"
model = "tts_models/en/ljspeech/tacotron2-DDC"

model_manager = ModelManager(path)


class TTSService(TtsServiceBase):
    @staticmethod
    def synthesize_and_save_to_file(quotes: List[TextPart]) -> None:
        logger.info("Started")

        for quote in quotes:
            try:
                model_path, config_path, model_item = model_manager.download_model(model)
                voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

                syn = Synthesizer(
                    tts_checkpoint=model_path,
                    tts_config_path=config_path,
                    vocoder_checkpoint=voc_path,
                    vocoder_config=voc_config_path
                )

                file_path = f"{quote.output_file_path}/{quote.file_name}.wav"

                logger.info(f"saving file {file_path}")

                outputs = syn.tts(quote.text)
                syn.save_wav(outputs, file_path)

                sleep(3)
            except Exception as err:
                logger.error(f"Get exception. Sleep and retry: {err}")
                logger.info("we need to wait about 1-2 h and continue.")
                sleep(60 * 60)

        logger.info("Completed")
