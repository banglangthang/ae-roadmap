import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


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


def embed_sentence(sentence):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embedding = model.encode(sentence)

    return embedding


def embed_sentences(sentences):
    model = SentenceTransformer("all-mpnet-base-v2")

    # 3. Generate the embeddings
    # The model.encode() function transforms each sentence into a vector
    embeddings = model.encode(sentences)

    # Print the shape of the embeddings (e.g., 3 sentences, 768 dimensions each)
    print(f"Embeddings shape: {embeddings.shape}")
    return embeddings


def calculate_similarity(sentences, embeddings):
    # Convert single embeddings to 2D arrays for scikit-learn's function
    # which expects (n_samples, n_features)
    embedding_1 = embeddings[0].reshape(1, -1)
    embedding_2 = embeddings[1].reshape(1, -1)
    embedding_3 = embeddings[2].reshape(1, -1)

    # Calculate and print the similarity scores
    similarity_1_2 = cosine_similarity(embedding_1, embedding_2)[0][0]
    similarity_1_3 = cosine_similarity(embedding_1, embedding_3)[0][0]

    print(f"\nSimilarity ('{sentences[0]}' vs. '{sentences[1]}'): {similarity_1_2:.4f}")
    print(f"Similarity ('{sentences[0]}' vs. '{sentences[2]}'): {similarity_1_3:.4f}")

    # You can also compare all pairs using a single call if you use the original matrix
    # This computes a matrix where each cell (i, j) is the similarity between sentence i and j
    pairwise_similarities = cosine_similarity(embeddings)
    print("\nPairwise similarity matrix:")
    print(pairwise_similarities)
