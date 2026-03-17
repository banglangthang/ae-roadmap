from chunker import split_text
from document_loader import extract_content


def main():
    print("Load pdf")
    pdf_filename = "files/pdf.pdf"
    pdf_content = extract_content(filename=pdf_filename)
    print(pdf_content)
    print("------------pdf chunk --------------")
    pdf_chunk = split_text(pdf_content)
    for i, chunk in enumerate(pdf_chunk):
        print(f"Chunk {i + 1}: {chunk.page_content}")
    print("------------pdf chunk with overlap--------------")
    pdf_chunk_overlap = split_text(pdf_content, chunk_overlap=10)
    for i, chunk in enumerate(pdf_chunk_overlap):
        print(f"Chunk {i + 1}: {chunk.page_content}")

    print("Load txt")
    txt_filename = "files/txt.txt"
    txt_content = extract_content(filename=txt_filename)
    print(txt_content)


main()
