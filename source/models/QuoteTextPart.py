from source.models.TextPart import TextPart


class QuoteTextPart(TextPart):
    def __init__(self, number: int, text: str, file_name: str = "", output_file_path: str = ""):
        super().__init__(text, file_name, output_file_path)
        self.number = number
        self.file_name = f"{file_name}-{number}"
        self.output_file_path = output_file_path
