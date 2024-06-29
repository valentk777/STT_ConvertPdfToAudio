from os import path
from typing import List

from source.file_services.file_service_base import FileServiceBase
from source.logging_utils import get_logger

logger = get_logger()


class TxtService(FileServiceBase):
    @staticmethod
    def read(file_path: str) -> str:
        logger.info("Started")

        if not path.exists(file_path):
            raise Exception(f"file not found. Path {file_path}")

        with open(file_path, 'r', encoding="utf-8") as f:
            text = f.read()

            logger.info("Completed")

            return text

    @staticmethod
    def read_lines(file_path: str) -> List[str]:
        logger.info("Started")

        if not path.exists(file_path):
            raise Exception(f"file not found. Path {file_path}")

        with open(file_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()

            logger.info("Completed")

            return lines
