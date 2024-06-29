from os import path

import fitz

from source.file_services.file_service_base import FileServiceBase
from source.logging_utils import get_logger

logger = get_logger()


class PdfService(FileServiceBase):
    @staticmethod
    def read(file_path: str) -> str:
        logger.info("Started")

        if not path.exists(file_path):
            raise Exception("file not found")

        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            text += page.get_text()

        logger.info("Completed")

        return text
