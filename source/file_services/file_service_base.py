from typing import List

from source.logging_utils import get_logger
from source.models.QuoteTextPart import QuoteTextPart
from source.models.TextPart import TextPart

logger = get_logger()


class FileServiceBase:
    @staticmethod
    def read(file_path: str) -> str:
        raise Exception("Implement in concrete file extension service.")

    @staticmethod
    def split_text_to_parts(text: str, symbol: str = "$$$") -> List[str]:
        logger.info("Started")

        parts = text.strip().split(symbol)

        logger.info("Completed")

        return parts

    @staticmethod
    def text_to_parts(texts: List[str], file_name: str = "", output_file_path: str = "") -> List[TextPart]:
        return list(map(lambda x: TextPart(x, file_name, output_file_path), texts))

    @staticmethod
    def text_to_quotes(texts: List[str], file_name: str = "", output_file_path: str = "") -> List[QuoteTextPart]:
        return list(map(lambda x: QuoteTextPart(x[0] + 1, x[1], file_name, output_file_path), enumerate(texts)))
