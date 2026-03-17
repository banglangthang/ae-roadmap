from document_loader import extract_content


def main():
    print("Load pdf")
    pdf_filename = "files/pdf.pdf"
    pdf_content = extract_content(filename=pdf_filename)
    print(pdf_content)

    print("Load txt")
    txt_filename = "files/txt.txt"
    txt_content = extract_content(filename=txt_filename)
    print(txt_content)


main()
