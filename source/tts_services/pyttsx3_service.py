# -------------------------------------------------------
# This is old version of TTS using pyttsx3 lib
# -------------------------------------------------------
from time import sleep
from typing import List

import pyttsx3

from source.logging_utils import get_logger
from source.models import TextPart
from source.tts_services.tts_service_base import TtsServiceBase

logger = get_logger()
engine = pyttsx3.init()


class Pyttsx3Service(TtsServiceBase):
    @staticmethod
    def synthesize_and_save_to_file(quotes: List[TextPart]) -> None:
        logger.info("Started")

        for quote in quotes:
            try:
                file_path = f"{quote.output_file_path}/{quote.file_name}.mp3"

                logger.info(f"saving file {file_path}")

                engine.save_to_file(quote.text, file_path)
                engine.runAndWait()

                sleep(10)
            except Exception as err:
                logger.error(f"Get exception. Sleep and retry: {err}")
                logger.info("we need to wait about 1-2 h and continue.")
                sleep(60 * 60 * 1)

        logger.info("Completed")
