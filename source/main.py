from logging_utils import get_logger
from services.audio_service import AudioService
from services.tts_service import TtsService
from services.txt_service import TxtService

LANGUAGE = "en"
INPUT_FILE_PATH = "data/quotes.txt"

logger = get_logger()


def start_stt():
    logger.info("Starting application")
    data = TxtService.read(INPUT_FILE_PATH)
    text_files = TtsService.split_text_to_parts(data)
    # audio_files = TtsService.convert_list_to_audio_list(text_files, language=LANGUAGE)
    AudioService.write_list_of_files_with_TTS(text_files, "data", "Quote")
    logger.info("Application stopped")


if __name__ == "__main__":
    start_stt()
