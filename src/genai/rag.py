from src.genai.vector_search import search_similar_tickets


SIMILARITY_THRESHOLD = 0.50


def build_context(similar_tickets):

    context = ""

    for index, row in similar_tickets.iterrows():

        context = context + (
            f"\nHistorical Case:\n"
            f"Category: {row['category']}\n"
            f"Sub Category: {row['sub_category']}\n"
            f"Issue: {row['issue_description']}\n"
            f"Resolution: {row['resolution']}\n"
        )

    return context


def build_rag_prompt(question, context):

    prompt = f"""
You are SupportIQ, an AI customer support assistant.

Answer the user's question using ONLY the historical
support cases provided below.

IMPORTANT RULES:

1. Do not invent resolutions, teams, managers, procedures,
or escalation paths that are not mentioned in the
historical cases.

2. Base the recommended resolution only on the provided
historical resolutions.

3. If multiple historical resolutions are available,
summarize the most relevant ones.

4. Do not claim that a resolution will definitely fix
the issue.

5. If the historical cases do not provide enough information,
clearly state that further investigation is required.

6. Recommend escalation only when the historical cases
support escalation or when the available information
is insufficient.

User Question:
{question}

Historical Support Cases:
{context}

Provide the response in exactly this structure:

1. Likely Issue:
Explain the likely issue based on the historical cases.

2. Recommended Resolution:
Provide a resolution supported by the historical cases.

3. Escalation Recommendation:
State whether further investigation or escalation may be required.
"""

    return prompt


def prepare_rag(question):

    # Search similar historical tickets
    similar_tickets = search_similar_tickets(
        question,
        top_k=3
    )

    # Get highest similarity score
    highest_score = similar_tickets[
        "similarity_score"
    ].iloc[0]

    # Check relevance
    if highest_score < SIMILARITY_THRESHOLD:

        return None, similar_tickets

    # Build context
    context = build_context(
        similar_tickets
    )

    # Build prompt
    rag_prompt = build_rag_prompt(
        question,
        context
    )

    return rag_prompt, similar_tickets