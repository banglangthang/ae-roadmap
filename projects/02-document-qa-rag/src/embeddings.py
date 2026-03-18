from sentence_transformers import SentenceTransformer


def embed_content():
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # The text you want to embed
    sentences = ["This is an example sentence", "Each sentence is converted."]

    # Generate embeddings
    embeddings = model.encode(sentences)

    # Print the embeddings
    for sentence, embedding in zip(sentences, embeddings):
        print(f"Sentence: {sentence}")
        print(f"Embedding shape: {embedding.shape}")
        print(f"Embedding sample: {embedding[:5]}")  # Print first 5 dimensions


embed_content()
