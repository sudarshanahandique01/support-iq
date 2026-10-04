import ollama
import time

from src.genai.rag import prepare_rag


def generate_support_answer(question):

    # ==============================================
    # STEP 1: PREPARE RAG PROMPT
    # ==============================================

    rag_prompt, similar_tickets = prepare_rag(
        question
    )


    # ==============================================
    # STEP 2: CHECK RELEVANT CASES
    # ==============================================

    if rag_prompt is None:

        return (
            "I could not find sufficiently relevant historical "
            "support cases for this question. "
            "Further investigation may be required."
        )


    # ==============================================
    # STEP 3: START LLM TIMER
    # ==============================================

    llm_start = time.time()


    # ==============================================
    # STEP 4: SEND PROMPT TO OLLAMA
    # ==============================================

    response = ollama.chat(
        model="llama3.2:1b",

        messages=[
            {
                "role": "user",
                "content": rag_prompt
            }
        ],

        options={
            "num_predict": 180,
            "temperature": 0.2
        },

        keep_alive="30m"
    )


    # ==============================================
    # STEP 5: STOP LLM TIMER
    # ==============================================

    llm_end = time.time()

    llm_time = llm_end - llm_start

    print(
        f"Ollama generation: "
        f"{llm_time:.2f} seconds"
    )


    # ==============================================
    # STEP 6: EXTRACT GENERATED ANSWER
    # ==============================================

    answer = response["message"]["content"]


    # ==============================================
    # STEP 7: RETURN ANSWER
    # ==============================================

    return answer