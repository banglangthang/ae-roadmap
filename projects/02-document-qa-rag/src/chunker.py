from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(content, chunk_overlap=0):
    if chunk_overlap:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100, chunk_overlap=chunk_overlap, length_function=len
        )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100, chunk_overlap=20, length_function=len
    )

    chunks = text_splitter.create_documents([content])
    return chunks
