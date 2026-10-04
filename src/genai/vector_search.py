import pandas as pd
import numpy as np
import time

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ==================================================
# LOAD RAG KNOWLEDGE DATA
# ==================================================

rag_path = "data/rag/supportiq_embeddings.parquet"

rag_df = pd.read_parquet(
    rag_path
)


# ==================================================
# CREATE EMBEDDING MATRIX
# ==================================================

embedding_matrix = np.array(
    rag_df["embedding"].tolist()
)


# ==================================================
# LOAD EMBEDDING MODEL
# ==================================================

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# ==================================================
# VECTOR SEARCH FUNCTION
# ==================================================

def search_similar_tickets(question, top_k=3):

    retrieval_start = time.time()


    # ------------------------------------------
    # CREATE QUERY EMBEDDING
    # ------------------------------------------

    embedding_start = time.time()

    query_embedding = embedding_model.encode(
        question
    )

    embedding_end = time.time()

    print(
        f"Query embedding: "
        f"{embedding_end - embedding_start:.2f} seconds"
    )


    # ------------------------------------------
    # VECTOR SIMILARITY SEARCH
    # ------------------------------------------

    search_start = time.time()

    similarity_scores = cosine_similarity(
        [query_embedding],
        embedding_matrix
    )[0]


    # IMPORTANT:
    # Use rag_df because that is our DataFrame
    results = rag_df.copy()

    results["similarity_score"] = similarity_scores


    # ------------------------------------------
    # SORT BY SIMILARITY
    # ------------------------------------------

    results = results.sort_values(
        by="similarity_score",
        ascending=False
    )


    # ------------------------------------------
    # GET TOP K RESULTS
    # ------------------------------------------

    results = results.head(
        top_k
    )


    # ------------------------------------------
    # VECTOR SEARCH TIME
    # ------------------------------------------

    search_end = time.time()

    print(
        f"Vector search: "
        f"{search_end - search_start:.2f} seconds"
    )


    # ------------------------------------------
    # TOTAL RETRIEVAL TIME
    # ------------------------------------------

    retrieval_end = time.time()

    print(
        f"Total retrieval: "
        f"{retrieval_end - retrieval_start:.2f} seconds"
    )


    return results