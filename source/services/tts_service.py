import subprocess
from typing import List
import pyttsx3
from gtts import gTTS

from source.logging_utils import get_logger

logger = get_logger()

class TtsService:
    @staticmethod
    def execute_unix(inputcommand):
        p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        return output

    @staticmethod
    def split_text_to_parts(text: str, symbol: str = "$$$") -> List[str]:
        logger.info("Started")

        parts = text.strip().split(symbol)

        logger.info("Completed")

        return parts

    @staticmethod
    def convert_to_audio_1(text: str, language: str) -> gTTS:
        logger.info("Started")

        audio = gTTS(text=text, lang=language, slow=False)

        logger.info("Completed")

        return audio

    @staticmethod
    def convert_list_to_audio_list(text_parts: List[str], language: str) -> List[gTTS]:
        logger.info("Started")

        audio_files = []

        # for current, text in enumerate([
        #     "Samantha sat back. “I have to say that I’m impressed with both your experiment and your thought process. You really threw yourself into it and you were fearless about interacting with customers and being honest about your ideas.",
        #     "Samantha sat back. \n“I have to say that I’m impressed with both your experiment and your thought process. \nYou really threw yourself into it and you were fearless about interacting with customers and being honest about your ideas.",
        #     "Samantha sat back\nI have to say that I’m impressed with both your experiment and your thought process\nYou really threw yourself into it and you were fearless about interacting with customers and being honest about your ideas",
        #     "Samantha sat back I have to say that I’m impressed with both your experiment and your thought process You really threw yourself into it and you were fearless about interacting with customers and being honest about your ideas",
        # ]):
        for current, text in enumerate(text_parts):
            # if current < 3:
            #     continue

            # fine_name = f"output-{current + 1}"
            # tts.tts_to_file(
            #     text=text, speaker=tts.speakers[0], language=language,
            #     file_path=f"{fine_name}.wav", speed=2)
            # text = tts.tts(text=text, speaker=tts.speakers[0], language=language)

            audio = TtsService.convert_to_audio_1(text, language)
            audio_files.append(audio)

        logger.info("Completed")

        return audio_files
