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
    # STEP 3: TRY LOCAL OLLAMA
    # ==============================================

    try:

        llm_start = time.time()

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

        llm_end = time.time()

        llm_time = llm_end - llm_start

        print(
            f"Ollama generation: "
            f"{llm_time:.2f} seconds"
        )

        answer = response["message"]["content"]

        return answer


    # ==============================================
    # STEP 4: ONLINE FREE FALLBACK
    # ==============================================

    except Exception:

        print(
            "Ollama is not available. "
            "Using retrieval-based response."
        )


        # ==========================================
        # GET MOST RELEVANT HISTORICAL CASE
        # ==========================================

        best_case = similar_tickets.iloc[0]

        category = str(best_case["category"])
        sub_category = str(best_case["sub_category"])
        product = str(best_case["product"])
        historical_issue = str(
            best_case["issue_description"]
        )
        historical_resolution = str(
            best_case["resolution"]
        )


        # ==========================================
        # BUILD LIKELY ISSUE
        # ==========================================

        likely_issue = (
            f"The reported issue is most closely related to "
            f"**{category} - {sub_category}** in the "
            f"**{product}** product. A similar historical case "
            f'reported: "{historical_issue}".'
        )


        # ==========================================
        # PREPARE CATEGORY VALUES
        # ==========================================

        category_lower = category.lower()

        sub_category_lower = sub_category.lower()


        # ==========================================
        # PAYROLL
        # ==========================================

        if category_lower == "payroll":

            if sub_category_lower == "overtime":

                next_steps = (
                    "1. Review the employee's submitted time "
                    "and overtime entries.\n\n"

                    "2. Verify that the overtime information "
                    "has been approved and transferred correctly "
                    "to payroll.\n\n"

                    f"3. Apply the historical resolution where "
                    f"applicable: **{historical_resolution}.**\n\n"

                    "4. Recheck the payroll result and confirm "
                    "that the overtime information is now "
                    "reflected correctly."
                )


            elif sub_category_lower == "tax":

                next_steps = (
                    "1. Review the employee's payroll and "
                    "tax-related configuration.\n\n"

                    "2. Verify that the relevant payroll "
                    "information is available and correctly "
                    "configured in the HCM system.\n\n"

                    f"3. Apply the historical resolution where "
                    f"applicable: **{historical_resolution}.**\n\n"

                    "4. Ask the employee to verify the payroll "
                    "information again."
                )


            else:

                next_steps = (
                    "1. Review the employee's payroll "
                    "configuration and recent payroll "
                    "processing results.\n\n"

                    "2. Verify the data related to the reported "
                    "payroll issue.\n\n"

                    f"3. Apply the historical resolution where "
                    f"applicable: **{historical_resolution}.**\n\n"

                    "4. Validate the payroll result with "
                    "the employee."
                )


        # ==========================================
        # BENEFITS
        # ==========================================

        elif category_lower == "benefits":

            next_steps = (
                "1. Review the employee's current benefit "
                "enrollment and eligibility information.\n\n"

                "2. Verify that the relevant benefit plan and "
                "employee data are correctly configured.\n\n"

                f"3. Apply the historical resolution where "
                f"applicable: **{historical_resolution}.**\n\n"

                "4. Ask the employee to verify the benefit "
                "information again."
            )


        # ==========================================
        # TIME MANAGEMENT
        # ==========================================

        elif category_lower == "time management":

            next_steps = (
                "1. Review the employee's time, attendance, "
                "or leave information related to the "
                "reported issue.\n\n"

                "2. Verify that the relevant time entry or "
                "request was submitted and processed "
                "correctly.\n\n"

                f"3. Apply the historical resolution where "
                f"applicable: **{historical_resolution}.**\n\n"

                "4. Ask the employee to retry the affected "
                "time-management action."
            )


        # ==========================================
        # RECRUITMENT
        # ==========================================

        elif category_lower == "recruitment":

            next_steps = (
                "1. Review the candidate or recruitment record "
                "related to the reported issue.\n\n"

                "2. Verify that the recruitment workflow and "
                "required information are complete and "
                "correctly configured.\n\n"

                f"3. Apply the historical resolution where "
                f"applicable: **{historical_resolution}.**\n\n"

                "4. Recheck the candidate or recruitment "
                "process after the update."
            )


        # ==========================================
        # PERFORMANCE
        # ==========================================

        elif category_lower == "performance":

            next_steps = (
                "1. Review the employee's performance record "
                "and the affected performance process.\n\n"

                "2. Verify that the required performance "
                "information and workflow steps are "
                "complete.\n\n"

                f"3. Apply the historical resolution where "
                f"applicable: **{historical_resolution}.**\n\n"

                "4. Ask the user to verify the performance "
                "information again."
            )


        # ==========================================
        # CORE HR
        # ==========================================

        elif category_lower == "core hr":

            next_steps = (
                "1. Review the employee's Core HR record "
                "related to the reported issue.\n\n"

                "2. Verify that the employee information is "
                "complete and correctly configured in the "
                "HCM system.\n\n"

                f"3. Apply the historical resolution where "
                f"applicable: **{historical_resolution}.**\n\n"

                "4. Ask the employee to verify the updated "
                "information."
            )


        # ==========================================
        # GENERAL FALLBACK
        # ==========================================

        else:

            next_steps = (
                f"1. Review the retrieved "
                f"**{category} - {sub_category}** "
                f"support scenario.\n\n"

                "2. Validate the relevant employee and "
                "system information.\n\n"

                f"3. Apply the historical resolution where "
                f"applicable: **{historical_resolution}.**\n\n"

                "4. Ask the user to verify whether the issue "
                "has been resolved."
            )


        # ==========================================
        # BUILD RECOMMENDED RESOLUTION
        # ==========================================

        recommended_resolution = (
            f"Based on a similar historical "
            f"**{category} - {sub_category}** case, "
            f"the recorded resolution was: "
            f"**{historical_resolution}.**\n\n"

            f"**Recommended next steps:**\n\n"

            f"{next_steps}"
        )


        # ==========================================
        # BUILD ESCALATION RECOMMENDATION
        # ==========================================

        escalation = (
            f"If the issue continues after applying the "
            f"historical resolution, escalate the ticket "
            f"to the appropriate **{category} / {product} "
            f"support team** with the troubleshooting "
            f"details and actions already performed."
        )


        # ==========================================
        # BUILD FINAL ANSWER
        # ==========================================

        answer = (
            "### Likely Issue\n\n"
            f"{likely_issue}\n\n"

            "### Recommended Resolution\n\n"
            f"{recommended_resolution}\n\n"

            "### Escalation Recommendation\n\n"
            f"{escalation}"
        )


        # ==========================================
        # RETURN ANSWER
        # ==========================================

        return answer