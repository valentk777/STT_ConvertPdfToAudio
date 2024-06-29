from logging_utils import get_logger
from source.file_services.txt_service import TxtService
from source.tts_services.pyttsx3_service import Pyttsx3Service
from source.tts_services.tts_service import TTSService

LANGUAGE = "en"
INPUT_FILE_PATH = "data/quotes.txt"

logger = get_logger()

# fails: 11, 15
START_FROM = 109
RUN_OLD = False
RUN_NEW = True


def start_stt():
    logger.info("Starting application")
    data = TxtService.read(INPUT_FILE_PATH)
    text_files = TxtService.split_text_to_parts(data)

    if RUN_NEW:
        new_quotes = TxtService.text_to_quotes(text_files, "Quote", "data/New_Quotes")
        new_quotes = list(filter(lambda x: x.number >= START_FROM, new_quotes))
        TTSService.synthesize_and_save_to_file(new_quotes)

    if RUN_OLD:
        old_quotes = TxtService.text_to_quotes(text_files, "Quote", "data/Old_Quotes")
        old_quotes = list(filter(lambda x: x.number >= START_FROM, old_quotes))
        Pyttsx3Service.synthesize_and_save_to_file(old_quotes)

    logger.info("Application stopped")


if __name__ == "__main__":
    start_stt()
