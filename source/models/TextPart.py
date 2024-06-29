class TextPart:
    def __init__(self, text: str, file_name: str = "", output_file_path: str = ""):
        self.text = (text
                     .replace("“", "")
                     .replace("”", "")
                     .replace("―", "-")
                     .replace("—", "-")
                     .replace('"', "")
                     )
        self.file_name = file_name
        self.output_file_path = output_file_path
