import streamlit as st
import time

from src.genai.llm import generate_support_answer
from src.genai.vector_search import (
    search_similar_tickets,
    rag_df
)

# ==================================================
# CHAT SESSION STATE
# ==================================================

if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []    

if "clear_overview_input" not in st.session_state:
    st.session_state["clear_overview_input"] = False  

# ==================================================
# AI ASSISTANT CHAT HISTORY
# ==================================================

if "assistant_chat_messages" not in st.session_state:
    st.session_state["assistant_chat_messages"] = []

if "clear_assistant_input" not in st.session_state:
    st.session_state["clear_assistant_input"] = False      



# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="SupportIQ",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# LOAD CSS
# ==================================================

with open(
    "assets/styles.css",
    "r",
    encoding="utf-8"
) as css_file:
    css = css_file.read()


st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown(
        """
<div class="brand">

<div class="brand-icon">
◆
</div>

<div>

<div class="brand-name">
SupportIQ
</div>

<div class="brand-subtitle">
AI Support Intelligence
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-title">NAVIGATION</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "AI Assistant",
            "Knowledge Base",
            "Architecture"
        ],
        label_visibility="collapsed"
    )


# ==================================================
# MAIN HEADER
# ==================================================

st.markdown(
    """
<div class="main-header">

<div>

<h1>
SupportIQ
</h1>

<p>
AI-Powered Customer Support Intelligence Platform
</p>

</div>

<div class="status-badge">

<span class="status-dot"></span>

AI System Online

</div>

</div>
""",
    unsafe_allow_html=True
)


# ==================================================
# OVERVIEW PAGE
# ==================================================

if page == "Overview":

    # ==============================================
    # OVERVIEW HEADING
    # ==============================================

    st.markdown(
        """
<div class="section-heading">

<div>

<h2>
Overview
</h2>

<p>
Monitor your AI-powered customer support intelligence platform
</p>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    # ==============================================
    # KPI CARDS
    # ==============================================

    metric_html = """
<div class="metric-grid">


<div class="metric-card">

<div class="metric-top">

<div class="metric-icon blue">
▣
</div>

<div class="metric-status">
DATA
</div>

</div>

<div class="metric-label">
Support Tickets
</div>

<div class="metric-value">
1.2M+
</div>

<div class="metric-detail">
Historical support records
</div>

</div>


<div class="metric-card">

<div class="metric-top">

<div class="metric-icon purple">
◆
</div>

<div class="metric-status">
MODEL
</div>

</div>

<div class="metric-label">
Embedding Model
</div>

<div class="metric-value model-value">
MiniLM
</div>

<div class="metric-detail">
384-dimensional vectors
</div>

</div>


<div class="metric-card">

<div class="metric-top">

<div class="metric-icon cyan">
◎
</div>

<div class="metric-status">
RAG
</div>

</div>

<div class="metric-label">
Vector Retrieval
</div>

<div class="metric-value">
Top 3
</div>

<div class="metric-detail">
Similar historical cases
</div>

</div>


<div class="metric-card">

<div class="metric-top">

<div class="metric-icon green">
✦
</div>

<div class="live-label">

<span class="small-live-dot"></span>

ACTIVE

</div>

</div>

<div class="metric-label">
Local LLM
</div>

<div class="metric-value model-value">
Llama 3.2
</div>

<div class="metric-detail">
Ollama inference engine
</div>

</div>


</div>
"""

    st.markdown(
        metric_html,
        unsafe_allow_html=True
    )


    # ==============================================
    # SPACE BETWEEN SECTIONS
    # ==============================================

    st.markdown(
        '<div class="dashboard-spacer"></div>',
        unsafe_allow_html=True
    )


      # ----------------------------------------------
    # SECOND DASHBOARD ROW
    # ----------------------------------------------
    
    left_column, right_column = st.columns(
        [1.65, 1],
        gap="medium"
    )
    
    
    # ==============================================
    # LEFT - AI SUPPORT ASSISTANT
    # ==============================================
    
    with left_column:
    
        st.markdown(
            """
    <div class="panel-heading">
    
    <div class="panel-icon assistant-icon">
    ✦
    </div>
    
    <div>
    
    <div class="panel-title">
    AI Support Assistant
    </div>
    
    <div class="panel-subtitle">
    Ask SupportIQ about a customer support issue
    </div>
    
    </div>
    
    </div>
    """,
            unsafe_allow_html=True
        )
    
    
    
    # ==============================================
    # RIGHT - HOW SUPPORTIQ WORKS
    # ==============================================
    
    with right_column:
    
        workflow_html = """
    <div class="workflow-card">
    
    <div class="workflow-header">
    
    <div>
    
    <div class="workflow-title">
    How SupportIQ Works
    </div>
    
    <div class="workflow-subtitle">
    RAG-powered support intelligence
    </div>
    
    </div>
    
    <div class="workflow-live">
    <span class="small-live-dot"></span>
    LIVE
    </div>
    
    </div>
    
    <div class="workflow">
    
    <div class="workflow-step">
    <div class="workflow-icon query-icon">◫</div>
    <div class="workflow-name">Query</div>
    <div class="workflow-description">User issue</div>
    </div>
    
    <div class="workflow-arrow">→</div>
    
    <div class="workflow-step">
    <div class="workflow-icon retrieve-icon">◆</div>
    <div class="workflow-name">Retrieve</div>
    <div class="workflow-description">Vector search</div>
    </div>
    
    <div class="workflow-arrow">→</div>
    
    <div class="workflow-step">
    <div class="workflow-icon reason-icon">✦</div>
    <div class="workflow-name">Reason</div>
    <div class="workflow-description">RAG context</div>
    </div>
    
    <div class="workflow-arrow">→</div>
    
    <div class="workflow-step">
    <div class="workflow-icon answer-icon">✓</div>
    <div class="workflow-name">Answer</div>
    <div class="workflow-description">AI response</div>
    </div>
    
    </div>
    
    <div class="pipeline-status">
    <span class="pipeline-dot"></span>
    RAG Pipeline Operational
    </div>
    
    </div>
    """
    
        st.markdown(
            workflow_html,
            unsafe_allow_html=True
        )
    
    
     # ==============================================
    # CLEAR PREVIOUS QUESTION AFTER SUBMISSION
    # ==============================================
    
    if st.session_state["clear_overview_input"]:
    
        st.session_state["support_question"] = ""
    
        st.session_state["clear_overview_input"] = False
    
    
    support_question = st.text_area(
        "Describe your support issue",
        placeholder="Example: My salary statement is not showing...",
        height=130,
        key="support_question"
    )
    
    
    analyze_button = st.button(
        "✦  Analyze Issue",
        type="primary",
        use_container_width=True
    )
    
    
    
    
        # ==============================================
    # ANALYZE SUPPORT ISSUE
    # ==============================================
    
    if analyze_button:
    
        if support_question.strip() == "":
    
            st.warning(
                "Please describe a support issue before analyzing."
            )
    
        else:
    
            with st.spinner(
                "SupportIQ is searching historical cases "
                "and generating a response..."
            ):
    
                try:
    
                    # ------------------------------------------
                    # START TIMER
                    # ------------------------------------------
    
                    start_time = time.time()
    
    
                    # ------------------------------------------
                    # GENERATE ANSWER + RETRIEVED CASES
                    # ------------------------------------------
    
                    answer = generate_support_answer(
                        support_question
                    )
    
    
                    # ------------------------------------------
                    # STOP TIMER
                    # ------------------------------------------
    
                    end_time = time.time()
    
                    response_time = end_time - start_time
    
    
                    # ------------------------------------------
                    # STORE USER MESSAGE
                    # ------------------------------------------
    
                    st.session_state["chat_messages"].append(
                        {
                            "role": "user",
                            "content": support_question
                        }
                    )
    
    
                    # ------------------------------------------
                    # STORE ASSISTANT MESSAGE
                    # ------------------------------------------
    
                    st.session_state["chat_messages"].append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "response_time": response_time
                        }
                    )
    
                    # Clear the input on the next rerun
                    st.session_state["clear_overview_input"] = True
    
                    st.rerun()
    
     
    
    
                except Exception as error:
    
                    st.error(
                        f"Unable to generate response: {error}"
                    )
    
    
       # ==============================================
    # DISPLAY CONVERSATION HISTORY
    # ==============================================
    
    if len(st.session_state["chat_messages"]) > 0:
    
        st.markdown(
            """
    <div class="response-heading">
    
    <div class="response-icon">✦</div>
    
    <div>
    
    <div class="response-title"> SupportIQ Conversation</div>
    
    <div class="response-subtitle">
    AI recommendations grounded in historical support cases
    </div>
    
    </div>
    
    <div class="response-badge">
        AI ASSISTANT
    </div>
    
    </div>
    """,
            unsafe_allow_html=True
        )
    
    
        # ==============================================
        # LOOP THROUGH ALL CHAT MESSAGES
        # ==============================================
    
        for message in st.session_state["chat_messages"]:
    
            # ------------------------------------------
            # USER MESSAGE
            # ------------------------------------------
            if message["role"] == "user":
                with st.chat_message("user"):

                    st.write(
                        message["content"]
                    )
    
            # ------------------------------------------
            # ASSISTANT MESSAGE
            # ------------------------------------------
            elif message["role"] == "assistant":
            
    
                with st.chat_message("assistant"):
    
                    st.markdown(
                        message["content"]
                    )
    
    
                    # ----------------------------------
                    # RESPONSE TIME
                    # ----------------------------------
    
                    if "response_time" in message:
    
                        st.caption(
                            f"⚡ Response generated in "
                            f"{message['response_time']:.2f} seconds"
                        )
# ==================================================
# AI ASSISTANT PAGE
# ==================================================

elif page == "AI Assistant":

    # ==============================================
    # PAGE HEADER + NEW CHAT BUTTON
    # ==============================================

    title_column, new_chat_column = st.columns(
        [5, 1]
    )

    with title_column:

        st.markdown(
            """
            <div class="section-heading">
                <div>
                    <h2>AI Support Assistant</h2>
                    <p>
                        Ask SupportIQ about a customer support issue.
                        Responses are generated using similar historical cases.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with new_chat_column:

        new_chat = st.button(
            "＋ New Chat",
            key="assistant_new_chat",
            use_container_width=True
        )


    # ==============================================
    # NEW CHAT
    # ==============================================

    if new_chat:

        st.session_state["assistant_chat_messages"] = []

        st.session_state["assistant_question"] = ""

        st.session_state["clear_assistant_input"] = False

        st.rerun()


    # ==============================================
    # CLEAR INPUT AFTER PREVIOUS SUBMISSION
    # ==============================================

    if st.session_state["clear_assistant_input"]:

        st.session_state["assistant_question"] = ""

        st.session_state["clear_assistant_input"] = False


    # ==============================================
    # QUESTION INPUT
    # ==============================================

    assistant_question = st.text_area(
        "Describe the customer support issue",
        placeholder=(
            "Example: Employee is unable to view "
            "their salary statement..."
        ),
        height=130,
        key="assistant_question"
    )


    assistant_button = st.button(
        "✦ Analyze Support Issue",
        type="primary",
        use_container_width=True,
        key="assistant_analyze_button"
    )


    # ==============================================
    # GENERATE ANSWER
    # ==============================================

    if assistant_button:

        if assistant_question.strip() == "":

            st.warning(
                "Please describe a support issue before analyzing."
            )

        else:

            with st.spinner(
                "SupportIQ is retrieving similar cases "
                "and generating a response..."
            ):

                try:

                    # ------------------------------------------
                    # START TIMER
                    # ------------------------------------------

                    start_time = time.time()


                    # ------------------------------------------
                    # GENERATE AI ANSWER
                    # ------------------------------------------

                    answer = generate_support_answer(
                        assistant_question
                    )


                    # ------------------------------------------
                    # STOP TIMER
                    # ------------------------------------------

                    end_time = time.time()

                    response_time = (
                        end_time - start_time
                    )


                    # ------------------------------------------
                    # RETRIEVE HISTORICAL CASES
                    # ------------------------------------------

                    similar_cases = search_similar_tickets(
                        assistant_question,
                        top_k=3
                    )


                    # ------------------------------------------
                    # CREATE CONVERSATION RECORD
                    # ------------------------------------------

                    conversation = {
                        "question": assistant_question,
                        "answer": answer,
                        "response_time": response_time,
                        "similar_cases": similar_cases
                    }


                    # ------------------------------------------
                    # ADD TO CHAT HISTORY
                    # ------------------------------------------

                    st.session_state[
                        "assistant_chat_messages"
                    ].append(
                        conversation
                    )


                    # ------------------------------------------
                    # CLEAR QUESTION ON NEXT RERUN
                    # ------------------------------------------

                    st.session_state[
                        "clear_assistant_input"
                    ] = True


                    st.rerun()


                except Exception as error:

                    st.error(
                        f"Unable to generate response: {error}"
                    )


    # ==============================================
    # DISPLAY CONVERSATION HISTORY
    # ==============================================

    if len(
        st.session_state["assistant_chat_messages"]
    ) > 0:

        st.markdown("---")

        st.markdown(
            """
<div class="response-heading">

<div class="response-icon">✦</div>

<div>
<div class="response-title">SupportIQ Conversation</div>
<div class="response-subtitle">AI recommendations grounded in historical support cases
</div>
</div>

<div class="response-badge">AI ASSISTANT</div>
</div>
""",
            unsafe_allow_html=True
        )


        # ==========================================
        # DISPLAY EVERY QUESTION + ANSWER
        # ==========================================

        for conversation in st.session_state[
            "assistant_chat_messages"
        ]:

            # --------------------------------------
            # USER QUESTION
            # --------------------------------------

            with st.chat_message("user"):
                st.write(conversation["question"])

            # --------------------------------------
            # AI ANSWER
            # --------------------------------------

            st.markdown(
                '<div class="support-ai-message">',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="support-ai-icon">
                    ✦
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                conversation["answer"]
            )


            # --------------------------------------
            # RESPONSE TIME
            # --------------------------------------

            st.caption(
                f"⚡ Response generated in "
                f"{conversation['response_time']:.2f} seconds"
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


            # --------------------------------------
            # RETRIEVED HISTORICAL CASES
            # --------------------------------------

            with st.expander(
                "View retrieved historical cases"
            ):

                similar_cases = conversation[
                    "similar_cases"
                ]

                case_number = 1

                for row_index, row in similar_cases.iterrows():

                    similarity = row[
                        "similarity_score"
                    ]

                    st.markdown(
                        f"### Case {case_number}"
                    )

                    st.write(
                        "**Similarity:** "
                        f"{similarity:.2f}"
                    )

                    st.write(
                        "**Category:**",
                        row["category"]
                    )

                    st.write(
                        "**Sub Category:**",
                        row["sub_category"]
                    )

                    st.write(
                        "**Product:**",
                        row["product"]
                    )

                    st.write(
                        "**Priority:**",
                        row["priority"]
                    )

                    st.write(
                        "**Issue:**",
                        row["issue_description"]
                    )

                    st.write(
                        "**Resolution:**",
                        row["resolution"]
                    )

                    case_number = (
                        case_number + 1
                    )

                    st.markdown("---")



    # ==============================================
    # HANDLE NEW CHAT
    # ==============================================

    if new_chat:

        # Clear chat conversation
        st.session_state["chat_messages"] = []

        # Clear previous AI answer
        if "assistant_answer" in st.session_state:
            del st.session_state["assistant_answer"]

        # Clear retrieved cases
        if "similar_cases" in st.session_state:
            del st.session_state["similar_cases"]

        # Clear previous response time
        if "assistant_response_time" in st.session_state:
            del st.session_state["assistant_response_time"]

        # Refresh the page
        st.rerun()

  

    # ==============================================
    # GENERATE RESPONSE
    # ==============================================

    if assistant_button:

        if assistant_question.strip() == "":

            st.warning(
                "Please describe a support issue before analyzing."
            )

        else:

            with st.spinner(
                "Retrieving historical cases and generating recommendation..."
            ):

                try:

                    # ------------------------------------------
                    # START TIMER
                    # ------------------------------------------

                    start_time = time.time()


                    # ------------------------------------------
                    # GENERATE RAG + LLM ANSWER
                    # ------------------------------------------

                    answer = generate_support_answer(
                        assistant_question
                    )


                    # ------------------------------------------
                    # RETRIEVE TOP 3 HISTORICAL CASES
                    # ------------------------------------------

                    similar_cases = search_similar_tickets(
                        assistant_question,
                        top_k=3
                    )


                    # ------------------------------------------
                    # STOP TIMER
                    # ------------------------------------------

                    end_time = time.time()

                    response_time = end_time - start_time


                    # ------------------------------------------
                    # STORE ANSWER
                    # ------------------------------------------

                    st.session_state[
                        "assistant_answer"
                    ] = answer


                    # ------------------------------------------
                    # STORE HISTORICAL CASES
                    # ------------------------------------------

                    st.session_state[
                        "similar_cases"
                    ] = similar_cases


                    # ------------------------------------------
                    # STORE RESPONSE TIME
                    # ------------------------------------------

                    st.session_state[
                        "assistant_response_time"
                    ] = response_time


                except Exception as error:

                    st.error(
                        f"Unable to generate response: {error}"
                    )


    # ==============================================
    # DISPLAY AI RESPONSE
    # ==============================================

    if "assistant_answer" in st.session_state:

        st.markdown(
            """
<div class="response-heading">

<div class="response-icon">
✦
</div>

<div>

<div class="response-title">
SupportIQ Recommendation
</div>

<div class="response-subtitle">
Generated using RAG and historical support cases
</div>

</div>

<div class="response-badge">
AI GENERATED
</div>

</div>
""",
            unsafe_allow_html=True
        )


        # ------------------------------------------
        # DISPLAY ANSWER
        # ------------------------------------------

        st.markdown(
            st.session_state[
                "assistant_answer"
            ]
        )


        # ------------------------------------------
        # DISPLAY RESPONSE TIME
        # ------------------------------------------

        if "assistant_response_time" in st.session_state:

            st.caption(
                f"⚡ Response generated in "
                f"{st.session_state['assistant_response_time']:.2f} seconds"
            )


    # ==============================================
    # DISPLAY RETRIEVED HISTORICAL CASES
    # ==============================================

    if "similar_cases" in st.session_state:

        st.markdown("---")

        st.markdown(
            "### Retrieved Historical Cases"
        )

        st.caption(
            "Top 3 historical support cases retrieved "
            "using semantic similarity."
        )


        similar_cases = st.session_state[
            "similar_cases"
        ]


        case_number = 1


        for index, case in similar_cases.iterrows():

            similarity_score = case[
                "similarity_score"
            ]


            with st.expander(
                f"Case {case_number} — "
                f"Similarity: {similarity_score:.2f}"
            ):

                # ----------------------------------
                # CATEGORY
                # ----------------------------------

                if "category" in similar_cases.columns:

                    st.markdown(
                        f"**Category:** "
                        f"{case['category']}"
                    )


                # ----------------------------------
                # SUB CATEGORY
                # ----------------------------------

                if "sub_category" in similar_cases.columns:

                    st.markdown(
                        f"**Sub Category:** "
                        f"{case['sub_category']}"
                    )


                # ----------------------------------
                # PRODUCT
                # ----------------------------------

                if "product" in similar_cases.columns:

                    st.markdown(
                        f"**Product:** "
                        f"{case['product']}"
                    )


                # ----------------------------------
                # PRIORITY
                # ----------------------------------

                if "priority" in similar_cases.columns:

                    st.markdown(
                        f"**Priority:** "
                        f"{case['priority']}"
                    )


                # ----------------------------------
                # ISSUE
                # ----------------------------------

                if "issue_description" in similar_cases.columns:

                    st.markdown(
                        f"**Issue:** "
                        f"{case['issue_description']}"
                    )


                # ----------------------------------
                # RESOLUTION
                # ----------------------------------

                if "resolution" in similar_cases.columns:

                    st.markdown(
                        f"**Resolution:** "
                        f"{case['resolution']}"
                    )


            case_number = case_number + 1


# ==================================================
# KNOWLEDGE BASE PAGE
# ==================================================

elif page == "Knowledge Base":

    # ==============================================
    # PAGE HEADING
    # ==============================================

    st.markdown(
        """
<div class="section-heading">

<div>

<h2>
Knowledge Base
</h2>

<p>
Explore the historical support cases used by
SupportIQ's RAG pipeline.
</p>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    # ==============================================
    # KNOWLEDGE BASE METRICS
    # ==============================================

    total_records = len(rag_df)

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            label="Knowledge Records",
            value=f"{total_records:,}"
        )


    with col2:

        st.metric(
            label="Embedding Dimension",
            value="384"
        )


    with col3:

        st.metric(
            label="Vector Retrieval",
            value="Top 3"
        )


    st.markdown("---")

    # ==============================================
    # SEMANTIC VECTOR SEARCH
    # ==============================================

    st.markdown(
        "### 🔎 Semantic Vector Search"
    )

    st.caption(
        "Search the knowledge base using natural language. "
        "SupportIQ converts the query into an embedding and "
        "retrieves the most similar historical support cases."
    )


    semantic_question = st.text_input(
        "Describe a support issue",
        placeholder=(
            "Example: Employee cannot view salary statement"
        ),
        key="knowledge_semantic_question"
    )


    semantic_search_button = st.button(
        "✦ Find Similar Cases",
        key="knowledge_semantic_search",
        use_container_width=True
    )


    # ==============================================
    # RUN VECTOR SEARCH
    # ==============================================

    if semantic_search_button:

        if semantic_question.strip() == "":

            st.warning(
                "Please enter a support issue."
            )

        else:

            with st.spinner(
                "Searching historical support cases..."
            ):

                similar_cases = search_similar_tickets(
                    semantic_question,
                    top_k=3
                )


            # ==========================================
            # DISPLAY SEMANTIC SEARCH RESULTS
            # ==========================================

            if (
                similar_cases is None
                or len(similar_cases) == 0
            ):

                st.info(
                    "No sufficiently relevant historical "
                    "support cases were found."
                )

            else:

                st.success(
                    f"Found {len(similar_cases)} similar "
                    "historical cases."
                )


                case_number = 1

                for index, case in similar_cases.iterrows():

                    similarity_score = case.get(
                        "similarity_score",
                        0
                    )


                    with st.expander(
                        f"Case {case_number} — "
                        f"Similarity: {similarity_score:.2f}"
                    ):

                        # ------------------------------
                        # CATEGORY
                        # ------------------------------

                        st.markdown(
                            f"**Category:** "
                            f"{case.get('category', 'N/A')}"
                        )


                        # ------------------------------
                        # SUB CATEGORY
                        # ------------------------------

                        st.markdown(
                            f"**Sub Category:** "
                            f"{case.get('sub_category', 'N/A')}"
                        )


                        # ------------------------------
                        # PRODUCT
                        # ------------------------------

                        st.markdown(
                            f"**Product:** "
                            f"{case.get('product', 'N/A')}"
                        )


                        # ------------------------------
                        # PRIORITY
                        # ------------------------------

                        st.markdown(
                            f"**Priority:** "
                            f"{case.get('priority', 'N/A')}"
                        )


                        # ------------------------------
                        # ISSUE
                        # ------------------------------

                        st.markdown(
                            "#### Issue"
                        )

                        st.write(
                            case.get(
                                "issue_description",
                                "N/A"
                            )
                        )


                        # ------------------------------
                        # RESOLUTION
                        # ------------------------------

                        st.markdown(
                            "#### Resolution"
                        )

                        st.write(
                            case.get(
                                "resolution",
                                "N/A"
                            )
                        )


                    case_number = case_number + 1


    st.markdown("---")

    # ==============================================
    # SEARCH AND FILTER
    # ==============================================

    st.markdown(
        "### Explore Historical Support Cases"
    )


    search_text = st.text_input(
        "Search Knowledge Base",
        placeholder=(
            "Search by issue, resolution, product..."
        )
    )


    # ----------------------------------------------
    # CATEGORY FILTER
    # ----------------------------------------------

    category_options = ["All"]

    if "category" in rag_df.columns:

        categories = (
            rag_df["category"]
            .dropna()
            .unique()
            .tolist()
        )

        categories.sort()

        category_options.extend(
            categories
        )


    selected_category = st.selectbox(
        "Filter by Category",
        category_options
    )


    # ==============================================
    # CREATE DISPLAY DATA
    # ==============================================

    display_df = rag_df.copy()


    # ----------------------------------------------
    # APPLY CATEGORY FILTER
    # ----------------------------------------------

    if (
        selected_category != "All"
        and "category" in display_df.columns
    ):

        display_df = display_df[
            display_df["category"]
            == selected_category
        ]


    # ----------------------------------------------
    # APPLY SEARCH
    # ----------------------------------------------

    if search_text.strip() != "":

        search_text_lower = (
            search_text
            .strip()
            .lower()
        )


        search_mask = False


        if "issue_description" in display_df.columns:

            search_mask = (
                display_df[
                    "issue_description"
                ]
                .fillna("")
                .str.lower()
                .str.contains(
                    search_text_lower,
                    regex=False
                )
            )


        if "resolution" in display_df.columns:

            resolution_mask = (
                display_df[
                    "resolution"
                ]
                .fillna("")
                .str.lower()
                .str.contains(
                    search_text_lower,
                    regex=False
                )
            )

            search_mask = (
                search_mask
                | resolution_mask
            )


        if "product" in display_df.columns:

            product_mask = (
                display_df[
                    "product"
                ]
                .fillna("")
                .str.lower()
                .str.contains(
                    search_text_lower,
                    regex=False
                )
            )

            search_mask = (
                search_mask
                | product_mask
            )


        display_df = display_df[
            search_mask
        ]


    # ==============================================
    # SELECT COLUMNS FOR DISPLAY
    # ==============================================

    display_columns = []


    if "category" in display_df.columns:

        display_columns.append(
            "category"
        )


    if "sub_category" in display_df.columns:

        display_columns.append(
            "sub_category"
        )


    if "product" in display_df.columns:

        display_columns.append(
            "product"
        )


    if "priority" in display_df.columns:

        display_columns.append(
            "priority"
        )


    if "issue_description" in display_df.columns:

        display_columns.append(
            "issue_description"
        )


    if "resolution" in display_df.columns:

        display_columns.append(
            "resolution"
        )


    # ==============================================
    # DISPLAY RESULTS
    # ==============================================

    st.markdown(
        f"**Matching Cases: {len(display_df):,}**"
    )


    if len(display_df) == 0:

        st.info(
            "No historical support cases match "
            "the selected search and filters."
        )

    else:

        st.dataframe(
            display_df[
                display_columns
            ].head(100),
            use_container_width=True,
            hide_index=True
        )


        if len(display_df) > 100:

            st.caption(
                "Showing the first 100 matching records."
            )

# ==================================================
# ARCHITECTURE PAGE
# ==================================================

elif page == "Architecture":

    # ==============================================
    # PAGE HEADING
    # ==============================================

    st.markdown(
        """
<div class="section-heading">

<div>

<h2>
System Architecture
</h2>

<p>
End-to-end architecture of the SupportIQ
data engineering, machine learning and GenAI platform.
</p>

</div>

</div>
""",
        unsafe_allow_html=True
    )

    # ==============================================
    # ARCHITECTURE OVERVIEW
    # ==============================================

    st.markdown(
        """
<div class="architecture-title">
SupportIQ End-to-End Pipeline
</div>

<div class="architecture-subtitle">
From raw customer support data to AI-powered recommendations
</div>
""",
        unsafe_allow_html=True
    )


    # ==============================================
    # DATA ENGINEERING LAYER
    # ==============================================

    st.markdown(
        """
<div class="architecture-section">

<div class="architecture-section-title">
01 &nbsp; DATA ENGINEERING
</div>

<div class="architecture-flow">

<div class="architecture-node">
<div class="architecture-node-icon blue-node">▣</div>
<div class="architecture-node-title">Raw Data</div>
<div class="architecture-node-text">1.2M+ Support Tickets</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon cyan-node">⚙</div>
<div class="architecture-node-title">PySpark</div>
<div class="architecture-node-text">Cleaning & Transformation</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon bronze-node">◆</div>
<div class="architecture-node-title">Bronze</div>
<div class="architecture-node-text">Raw Delta Layer</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon silver-node">◆</div>
<div class="architecture-node-title">Silver</div>
<div class="architecture-node-text">Clean Data</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon gold-node">◆</div>
<div class="architecture-node-title">Gold</div>
<div class="architecture-node-text">Analytics Ready</div>
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    # ==============================================
    # ANALYTICS + ML LAYER
    # ==============================================

    st.markdown(
        """
<div class="architecture-section">

<div class="architecture-section-title">
02 &nbsp; ANALYTICS & MACHINE LEARNING
</div>

<div class="architecture-flow">

<div class="architecture-node">
<div class="architecture-node-icon blue-node">▤</div>
<div class="architecture-node-title">Gold Data</div>
<div class="architecture-node-text">Business Analytics</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon purple-node">◈</div>
<div class="architecture-node-title">Power BI</div>
<div class="architecture-node-text">Support Dashboard</div>
</div>

<div class="architecture-arrow">+</div>

<div class="architecture-node">
<div class="architecture-node-icon cyan-node">◎</div>
<div class="architecture-node-title">ML Pipeline</div>
<div class="architecture-node-text">SLA Prediction</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon green-node">✓</div>
<div class="architecture-node-title">Predictions</div>
<div class="architecture-node-text">Delta Output</div>
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    # ==============================================
    # GENAI / RAG LAYER
    # ==============================================

    st.markdown(
        """
<div class="architecture-section">

<div class="architecture-section-title">
03 &nbsp; GENAI & RAG
</div>

<div class="architecture-flow">

<div class="architecture-node">
<div class="architecture-node-icon blue-node">▣</div>
<div class="architecture-node-title">Knowledge Base</div>
<div class="architecture-node-text">Historical Cases</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon purple-node">◆</div>
<div class="architecture-node-title">MiniLM</div>
<div class="architecture-node-text">384-D Embeddings</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon cyan-node">◎</div>
<div class="architecture-node-title">Vector Search</div>
<div class="architecture-node-text">Cosine Similarity</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon purple-node">✦</div>
<div class="architecture-node-title">RAG</div>
<div class="architecture-node-text">Context Grounding</div>
</div>

<div class="architecture-arrow">→</div>

<div class="architecture-node">
<div class="architecture-node-icon green-node">✦</div>
<div class="architecture-node-title">Llama 3.2:1B</div>
<div class="architecture-node-text">Ollama Local LLM</div>
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    # ==============================================
    # FINAL APPLICATION
    # ==============================================

    st.markdown(
        """
<div class="architecture-final">

<div class="architecture-final-icon">
✦
</div>

<div>

<div class="architecture-final-title">
SupportIQ AI Support Assistant
</div>

<div class="architecture-final-text">
Streamlit application integrating semantic retrieval,
RAG and Llama 3.2 to generate support recommendations
grounded in historical customer support cases
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )