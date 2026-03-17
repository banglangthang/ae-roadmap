from pathlib import Path

from pdfminer.high_level import extract_text

from exceptions import FileExtensionNotSupportedException, FileNotFoundException


def load_txt_file_content(filename: str) -> str:
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError as _:
        raise FileNotFoundException(f"{filename} not found")


def load_pdf_file_content(filename: str) -> str:
    try:
        content = extract_text(filename)
        return content
    except FileNotFoundError as _:
        raise FileNotFoundException(f"{filename} not found")


def extract_content(filename: str) -> str:
    file_path = Path(filename)
    suffix = file_path.suffix.lower()

    if suffix not in [".pdf", ".txt"]:
        raise FileExtensionNotSupportedException(f"{suffix} not supported")
    if suffix == ".txt":
        return load_txt_file_content(filename=filename)
    if suffix == ".pdf":
        return load_pdf_file_content(filename=filename)

    return ""
