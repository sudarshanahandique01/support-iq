import pandas as pd
import numpy as np
import time
import re

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
# STOP WORDS
# ==================================================

stop_words = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "in",
    "on",
    "at",
    "to",
    "for",
    "of",
    "and",
    "or",
    "my",
    "our",
    "their",
    "not",
    "it",
    "this",
    "that",
    "with",
    "from",
    "employee",
    "user",
    "issue",
    "problem"
}


# ==================================================
# EXTRACT IMPORTANT WORDS
# ==================================================

def get_keywords(text):

    text = str(text).lower()

    words = re.findall(
        r"[a-z0-9]+",
        text
    )

    keywords = set()

    for word in words:

        if word not in stop_words and len(word) > 2:

            keywords.add(word)

    return keywords


# ==================================================
# KEYWORD OVERLAP SCORE
# ==================================================

def calculate_keyword_score(question, issue):

    question_keywords = get_keywords(
        question
    )

    issue_keywords = get_keywords(
        issue
    )

    if len(question_keywords) == 0:

        return 0.0

    common_keywords = (
        question_keywords.intersection(
            issue_keywords
        )
    )

    score = (
        len(common_keywords)
        / len(question_keywords)
    )

    return score


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

    results = rag_df.copy()

    results["similarity_score"] = (
        similarity_scores
    )


    # ------------------------------------------
    # CALCULATE KEYWORD SCORES
    # ------------------------------------------

    keyword_scores = []

    for issue in results["issue_description"]:

        keyword_score = calculate_keyword_score(
            question,
            issue
        )

        keyword_scores.append(
            keyword_score
        )

    results["keyword_score"] = (
        keyword_scores
    )


    # ------------------------------------------
    # CREATE HYBRID SCORE
    # ------------------------------------------

    results["final_score"] = (
        results["similarity_score"] * 0.75
        +
        results["keyword_score"] * 0.25
    )


    # ------------------------------------------
    # SORT BY FINAL SCORE
    # ------------------------------------------

    results = results.sort_values(
        by="final_score",
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