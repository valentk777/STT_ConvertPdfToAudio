from time import sleep
from typing import List

import pyttsx3
from gtts import gTTS

from source.logging_utils import get_logger

logger = get_logger()
engine = pyttsx3.init()

class AudioService:
    @staticmethod
    def write_one_file(audio: gTTS, audio_file_path: str, audio_file_name: str) -> None:
        logger.info("Started")

        audio.save(f"{audio_file_path}/{audio_file_name}.mp3")

        logger.info("Completed")

    @staticmethod
    def write_list_of_files(audio_files: List[gTTS], audio_file_path: str, audio_file_name: str) -> None:
        logger.info("Started")
        total = len(audio_files)
        current = 0

        while current < total:
            try:
                file_name = f"{audio_file_name}-{current + 1}"
                logger.info(f"saving file {file_name}")
                AudioService.write_one_file(audio_files[current], audio_file_path, file_name)
                current += 1
                sleep(20)
            except Exception as err:
                logger.error(f"Get exception. Sleep and retry: {err}")
                logger.info("we need to wait about 1-2 h and continue.")
                sleep(60 * 60 * 1)

        logger.info("Completed")

    @staticmethod
    def write_list_of_files_with_TTS(text_files: List[str], audio_file_path: str, audio_file_name: str) -> None:
        logger.info("Started")
        total = len(text_files)
        start_from = 63

        for i in range(1, total + 1):
            if i < start_from:
                continue

            try:
                file_name = f"{audio_file_name}-{i}"
                file_path = f"{audio_file_path}/{file_name}.mp3"

                logger.info(f"saving file {file_path}")

                engine.save_to_file(text_files[i - 1], file_path)
                engine.runAndWait()

                sleep(10)
            except Exception as err:
                logger.error(f"Get exception. Sleep and retry: {err}")
                logger.info("we need to wait about 1-2 h and continue.")
                sleep(60 * 60 * 1)

        logger.info("Completed")
