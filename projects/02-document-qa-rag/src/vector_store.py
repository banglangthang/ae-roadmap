import uuid

import chromadb

from embeddings import embed_sentence


class ChromaVectorStore:
    def store_document(self, collection, document):
        embedding = embed_sentence(document)
        collection.add(
            ids=[str(uuid.uuid4())], documents=[document], embeddings=[embedding]
        )

    def retrieve_by_document(self, collection, document):
        return collection.query(query_texts=[document])

    def retrieve_by_embedding(self, collection, document):
        embedding = embed_sentence(document)
        return collection.query(query_embeddings=[embedding], n_results=10)


if __name__ == "__main__":
    chroma_client = chromadb.PersistentClient()
    collection = chroma_client.get_collection(name="my_collection")
    if not collection:
        collection = chroma_client.create_collection(name="my_collection")
    chroma_vector_store = ChromaVectorStore()

    chroma_vector_store.store_document(collection, "Bang is a software engineer")
    chroma_vector_store.store_document(collection, "I love travel")

    document_query = chroma_vector_store.retrieve_by_document(
        collection, "What does Bang do?"
    )
    print("----------document query----------------")
    print(document_query)
    embedding_query = chroma_vector_store.retrieve_by_embedding(
        collection, "What does Bang do?"
    )
    print("----------embedding query---------------")
    print(embedding_query)
