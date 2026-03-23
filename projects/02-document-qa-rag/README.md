# Project 2: Chat with Your Documents (RAG)

## Phase: 2 - Core AI Engineering (4-6 weeks)

## Overview
Build a Retrieval-Augmented Generation (RAG) system that allows users to upload documents and ask questions about them. The AI will search through your documents and provide accurate, contextual answers.

---

## Prerequisites
- [x] Completed Project 1 (AI Chatbot CLI)
- [x] Understanding of API calls and conversation management

---

## Learning Objectives
- [x] Understanding RAG architecture
- [x] Text embeddings and vector representations
- [x] Vector databases (ChromaDB, Pinecone)
- [ ] Document processing and chunking
- [ ] Semantic search
- [ ] Retrieval strategies

---

## What You Will Build

### Core Features
1. **Document Ingestion** - Load and process PDF/TXT files
2. **Embeddings** - Convert text to vectors
3. **Vector Storage** - Store and search embeddings
4. **Question Answering** - Answer questions using document context

### Stretch Goals
- Multiple document collections
- Hybrid search (semantic + keyword)
- Web UI with Streamlit

---

# STEP-BY-STEP IMPLEMENTATION GUIDE

## Step 1: Understand RAG Conceptually

### Tasks
- [x] Read about RAG architecture
- [x] Understand why RAG is needed
- [x] Learn the RAG pipeline

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| What is RAG? | https://www.pinecone.io/learn/retrieval-augmented-generation/ | Core RAG concepts |
| RAG Overview | https://docs.llamaindex.ai/en/stable/getting_started/concepts/ | RAG pipeline explained |
| Why RAG? | https://www.anthropic.com/news/contextual-retrieval | Why we need RAG |

### Key Concept: The RAG Pipeline
```
1. INGEST:    Document → Chunks → Embeddings → Vector DB
2. RETRIEVE:  Question → Embedding → Search Vector DB → Relevant Chunks
3. GENERATE:  Question + Relevant Chunks → LLM → Answer
```

### Why RAG Matters
- LLMs have **knowledge cutoff dates** (don't know recent info)
- LLMs can **hallucinate** (make up facts)
- LLMs have **token limits** (can't read entire books)
- RAG solves these by **retrieving relevant context** at query time

### Self-Check
Can you explain RAG to someone in 2 sentences?

---

## Step 2: Document Loading

### Tasks
- [x] Load text files (.txt, .md)
- [x] Load PDF files
- [x] Extract clean text from documents

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| PyPDF2 | https://pypdf2.readthedocs.io/en/latest/ | Reading PDFs in Python |
| pypdf | https://pypdf.readthedocs.io/en/latest/ | Modern PDF library |
| LangChain Loaders | https://python.langchain.com/docs/how_to/#document-loaders | Various document loaders |
| Unstructured | https://docs.unstructured.io/welcome | Advanced document parsing |

### What to Implement
Create `src/document_loader.py`:
- Function to load a text file and return content
- Function to load a PDF and return content
- Function that detects file type and uses correct loader

### Tips
- Start simple with `.txt` files
- PDFs can be tricky - some are scanned images (need OCR)
- Handle encoding issues (UTF-8)

### Checkpoint
You should be able to load any document and print its text content.

---

## Step 3: Text Chunking

### Tasks
- [x] Understand why we chunk documents
- [x] Implement basic chunking
- [x] Add chunk overlap

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Chunking Strategies | https://www.pinecone.io/learn/chunking-strategies/ | Different ways to chunk |
| LangChain Splitters | https://python.langchain.com/docs/how_to/#text-splitters | Text splitting tools |
| Chunk Size Guide | https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5 | Choosing chunk size |

### Key Concept: Why Chunk?
- Documents are too large to fit in LLM context
- We need to find **relevant parts**, not send everything
- Smaller chunks = more precise retrieval

### Key Concept: Chunk Overlap
```
Document: "The quick brown fox jumps over the lazy dog."

Without overlap:
  Chunk 1: "The quick brown fox"
  Chunk 2: "jumps over the lazy dog."  ← Context lost!

With overlap:
  Chunk 1: "The quick brown fox jumps"
  Chunk 2: "fox jumps over the lazy dog."  ← Better context!
```

### What to Implement
Create `src/chunker.py`:
- Function to split text into chunks of N characters
- Add overlap between chunks
- Return list of chunks with metadata (position, source file)

### Parameters to Experiment With
- `chunk_size`: 500-2000 characters (start with 1000)
- `chunk_overlap`: 10-20% of chunk size (start with 100)

### Checkpoint
Given a document, you should get a list of overlapping text chunks.

---

## Step 4: Understanding Embeddings

### Tasks
- [x] Understand what embeddings are
- [x] Learn about vector similarity
- [x] Generate your first embeddings

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| What are Embeddings? | https://www.pinecone.io/learn/vector-embeddings/ | Core embedding concepts |
| OpenAI Embeddings | https://platform.openai.com/docs/guides/embeddings | How to generate embeddings |
| Embedding Models | https://platform.openai.com/docs/guides/embeddings#embedding-models | Available models |
| Sentence Transformers | https://www.sbert.net/docs/quickstart.html | Free local embeddings |

### Key Concept: What is an Embedding?
An embedding converts text into a **list of numbers** (vector) that captures meaning:
```
"king" → [0.2, -0.5, 0.8, ...]  (1536 numbers for OpenAI)
"queen" → [0.3, -0.4, 0.7, ...]  (similar to "king"!)
"banana" → [-0.1, 0.9, -0.2, ...]  (very different)
```

### Key Concept: Similarity
Similar texts have similar vectors. We measure with **cosine similarity**:
- `similarity("king", "queen")` → 0.85 (high = similar)
- `similarity("king", "banana")` → 0.12 (low = different)

### What to Implement
Create `src/embeddings.py`:
- Function to generate embedding for a single text
- Function to generate embeddings for a list of texts (batch)
- Test by comparing similarity of related vs unrelated texts

### Checkpoint
You should be able to generate embeddings and see that similar texts have similar vectors.

---

## Step 5: Vector Database Setup

### Tasks
- [x] Choose a vector database
- [x] Set up ChromaDB locally
- [x] Store and retrieve embeddings

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| ChromaDB Quickstart | https://docs.trychroma.com/getting-started | Local vector DB setup |
| ChromaDB Collections | https://docs.trychroma.com/guides | Working with collections |
| Pinecone (cloud) | https://docs.pinecone.io/docs/quickstart | Alternative: Cloud vector DB |
| Vector DB Comparison | https://www.superannotate.com/blog/vector-databases-comparison | Choosing a vector DB |

### Key Concept: What is a Vector Database?
A specialized database for storing and searching embeddings:
- **Store**: Save embedding + metadata + original text
- **Search**: Find most similar embeddings to a query
- **Fast**: Optimized for similarity search (not exact match)

### What to Implement
Create `src/vector_store.py`:
- Function to initialize ChromaDB collection
- Function to add documents (text + embedding + metadata)
- Function to search by query embedding
- Function to delete/clear collection

### Checkpoint
You should be able to store chunks and search for similar ones.

---

## Step 6: Build the Retrieval Pipeline

### Tasks
- [ ] Connect all pieces together
- [ ] Query → Embed → Search → Return chunks
- [ ] Test with sample questions

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| LangChain Retrieval | https://python.langchain.com/docs/tutorials/rag/ | Full RAG tutorial |
| Retrieval Strategies | https://python.langchain.com/docs/how_to/#retrievers | Different retrieval methods |

### What to Implement
Create `src/retriever.py`:
- Function that takes a question string
- Generates embedding for the question
- Searches vector DB for similar chunks
- Returns top K relevant chunks

### Parameters to Tune
- `k`: Number of chunks to retrieve (start with 3-5)
- `score_threshold`: Minimum similarity score (optional)

### Checkpoint
Given a question, you should get back the most relevant chunks from your documents.

---

## Step 7: Question Answering with Context

### Tasks
- [ ] Build the QA prompt
- [ ] Send context + question to LLM
- [ ] Add source citations

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| RAG Prompting | https://www.promptingguide.ai/techniques/rag | RAG prompt templates |
| LangChain QA | https://python.langchain.com/docs/tutorials/rag/#retrieval-and-generation-generate | QA chain |

### Key Concept: RAG Prompt Template
```
You are a helpful assistant. Answer the question based ONLY on the following context.
If the context doesn't contain the answer, say "I don't have enough information."

Context:
{retrieved_chunks}

Question: {user_question}

Answer:
```

### What to Implement
Create `src/qa_chain.py`:
- Function to build prompt with context and question
- Function to call LLM with the prompt
- Extract and format the answer
- Include source citations (which document/chunk)

### Checkpoint
Ask a question about your documents and get an accurate answer with sources!

---

## Step 8: Build the Complete Pipeline

### Tasks
- [ ] Create main entry point
- [ ] Ingest documents command
- [ ] Query interface
- [ ] Show sources with answers

### What to Implement
Create `src/main.py`:
- Command to ingest documents: `python main.py ingest ./documents/`
- Interactive query mode: `python main.py query`
- Display answers with source citations

### Workflow
```bash
# 1. Add documents to folder
cp my_documents/* documents/

# 2. Ingest (process and store)
python main.py ingest

# 3. Ask questions
python main.py query
> What is mentioned about X?
Answer: Based on document.pdf (page 5), X is...
```

### Checkpoint
Full working RAG system!

---

## Step 9: Evaluation and Improvement

### Tasks
- [ ] Test with different questions
- [ ] Identify failure cases
- [ ] Improve chunking/retrieval

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| RAG Evaluation | https://docs.ragas.io/en/latest/ | Evaluating RAG quality |
| Improving RAG | https://www.pinecone.io/learn/advanced-rag-techniques/ | Advanced techniques |

### Common Issues and Fixes
| Problem | Possible Cause | Fix |
|---------|---------------|-----|
| Wrong answers | Chunks too small | Increase chunk size |
| Missing info | Not enough chunks | Increase k in retrieval |
| Irrelevant chunks | Bad embeddings | Try different embedding model |
| Slow queries | Large vector DB | Add indexing, use cloud DB |

---

## Stretch Goals

### Hybrid Search
- [ ] Combine semantic search with keyword search
- **Docs**: https://docs.trychroma.com/docs/collections/configure#using-with-where-filters

### Web UI
- [ ] Build interface with Streamlit or Gradio
- **Docs**: https://docs.streamlit.io/ or https://www.gradio.app/docs

### Multiple Collections
- [ ] Separate collections for different document sets
- [ ] Let user choose which collection to query

---

## Final Project Structure

```
02-document-qa-rag/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── main.py              # Entry point
│   ├── document_loader.py   # Load PDF, TXT, MD
│   ├── chunker.py           # Text chunking
│   ├── embeddings.py        # Generate embeddings
│   ├── vector_store.py      # ChromaDB operations
│   ├── retriever.py         # Search and retrieve
│   └── qa_chain.py          # Question answering
├── documents/               # Your documents go here
│   └── .gitkeep
└── data/
    └── chroma/              # Vector DB storage
```

---

## Self-Check Questions

After completing this project, you should be able to answer:

1. What is the difference between semantic search and keyword search?
2. Why do we chunk documents? What happens if chunks are too big/small?
3. What is an embedding? How does similarity search work?
4. What is a vector database and why is it needed?
5. How do you evaluate if your RAG system is working well?

---

## Notes
_Add your learning notes here as you progress_

---

**Status**: Not Started  
**Started**: -  
**Completed**: -
