from typing import List

from source.logging_utils import get_logger
from source.models import TextPart

logger = get_logger()


class TtsServiceBase:
    @staticmethod
    def synthesize_and_save_to_file(text_parts: List[TextPart]) -> None:
        raise Exception("Implement in concrete file extension service.")
