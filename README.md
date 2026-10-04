# SupportIQ — AI-Powered Customer Support Analytics & Resolution Platform

SupportIQ is an end-to-end **Data Engineering, Machine Learning, and Generative AI platform** designed to analyze customer support operations and assist support teams with AI-powered resolution recommendations.

The project processes more than **1.2 million synthetic customer support tickets** using PySpark and a Bronze–Silver–Gold data architecture. The processed data is used for business analytics, SLA prediction, and a Retrieval-Augmented Generation (RAG) system that retrieves similar historical support cases and generates contextual support recommendations.

## Key Capabilities

- Large-scale data processing using **PySpark**
- Bronze–Silver–Gold data architecture with **Delta Lake**
- Data profiling, cleaning, transformation, Spark SQL, joins, and window functions
- Interactive customer support analytics using **Power BI**
- Machine Learning pipeline for **Resolution SLA Prediction**
- Historical support knowledge base for GenAI
- Semantic embeddings using **MiniLM**
- Vector similarity search using **Cosine Similarity**
- Retrieval-Augmented Generation (**RAG**)
- Local LLM inference using **Llama 3.2 through Ollama**
- Interactive AI Support Assistant built with **Streamlit**

## High-Level Architecture

```text
1.2M+ Synthetic Support Tickets
              │
              ▼
           PySpark
              │
              ▼
     Data Profiling & Cleaning
              │
              ▼
      Data Transformation
              │
              ▼
     Bronze → Silver → Gold
              │
        ┌─────┴─────┐
        ▼           ▼
     Power BI    Machine Learning
                    │
                    ▼
              SLA Predictions

Historical Resolved Tickets
              │
              ▼
       Knowledge Base
              │
              ▼
       MiniLM Embeddings
              │
              ▼
        Vector Search
      (Cosine Similarity)
              │
              ▼
             RAG
              │
              ▼
      Llama 3.2 + Ollama
              │
              ▼
   SupportIQ AI Assistant
         (Streamlit)
