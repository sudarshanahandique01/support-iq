# 🎧 SupportIQ — AI-Powered Customer Support Analytics & Resolution Platform

👉 [Launch SupportIQ] https://support-iq.streamlit.app/

SupportIQ is an end-to-end **Data Engineering, Machine Learning, Business Intelligence, and Generative AI** project designed to analyze customer support operations and assist support teams in resolving issues using historical support cases.

The project processes **1.2M+ synthetic support tickets** through a PySpark-based data pipeline, transforms the data using a **Bronze → Silver → Gold** architecture, provides operational insights through **Power BI**, predicts resolution SLA outcomes using Machine Learning, and uses **Retrieval-Augmented Generation (RAG)** to recommend resolutions for support issues.

The application includes an interactive **Streamlit AI Support Assistant** that retrieves semantically similar historical support cases and generates contextual resolution recommendations.

---

## 🚀 Key Features

- 📊 Processes **1.2M+ customer support tickets**
- ⚡ Large-scale data processing using **PySpark**
- 🏗️ **Bronze → Silver → Gold** data architecture
- 🧹 Data profiling, cleaning, validation, and transformation
- 🔍 Spark SQL-based support analytics
- 📈 Interactive **Power BI dashboard**
- 🤖 Machine Learning for **Resolution SLA Prediction**
- 🧠 **Sentence Transformers (MiniLM)** for semantic embeddings
- 🔎 Hybrid retrieval using **semantic similarity + keyword matching**
- 📚 RAG-based historical support case retrieval
- 💬 Local AI assistant using **Llama 3.2 via Ollama**
- ☁️ Lightweight retrieval-based fallback for cloud deployment
- 🖥️ Interactive multi-page **Streamlit application**
- 🌐 Public deployment using **Streamlit Community Cloud**

---

## 🏗️ Project Architecture

SupportIQ follows an end-to-end architecture that combines **Data Engineering, Business Intelligence, Machine Learning, and Generative AI**.

```text
                    ┌─────────────────────────┐
                    │  1.2M+ Support Tickets │
                    │     Synthetic Data      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │         PySpark         │
                    │ Profiling & Cleaning    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Medallion Pipeline    │
                    │ Bronze → Silver → Gold  │
                    └────────────┬────────────┘
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
                ▼                ▼                ▼
        ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
        │   Power BI   │ │      ML      │ │    GenAI     │
        │  Analytics   │ │ SLA Prediction│ │ Knowledge Base│
        └──────────────┘ └──────────────┘ └───────┬──────┘
                                                   │
                                                   ▼
                                         ┌──────────────────┐
                                         │ MiniLM Embeddings │
                                         │    384-D Vector   │
                                         └────────┬─────────┘
                                                  │
                                                  ▼
                                         ┌──────────────────┐
                                         │ Hybrid Retrieval │
                                         │ Semantic+Keyword │
                                         └────────┬─────────┘
                                                  │
                                                  ▼
                                         ┌──────────────────┐
                                         │       RAG        │
                                         └────────┬─────────┘
                                                  │
                                    ┌─────────────┴─────────────┐
                                    │                           │
                                    ▼                           ▼
                            ┌───────────────┐           ┌───────────────┐
                            │ Local Mode    │           │ Cloud Mode    │
                            │ Llama 3.2     │           │ Retrieval     │
                            │ + Ollama      │           │ Fallback      │
                            └───────┬───────┘           └───────┬───────┘
                                    │                           │
                                    └─────────────┬─────────────┘
                                                  ▼
                                         ┌──────────────────┐
                                         │ Streamlit App    │
                                         │ SupportIQ        │
                                         └──────────────────┘
```



## 🛠️ Technology Stack

| Area | Technologies |
|---|---|
| **Programming** | Python |
| **Data Engineering** | PySpark, Spark SQL |
| **Data Architecture** | Bronze → Silver → Gold Medallion Architecture |
| **Data Storage** | Delta Lake, Parquet |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn, Logistic Regression, Decision Tree, Random Forest |
| **Data Visualization** | Power BI |
| **Embeddings** | Sentence Transformers (`all-MiniLM-L6-v2`) |
| **Vector Retrieval** | Cosine Similarity, Keyword Matching |
| **GenAI / RAG** | Retrieval-Augmented Generation (RAG) |
| **Local LLM** | Llama 3.2:1B via Ollama |
| **Application** | Streamlit |
| **Cloud Deployment** | Streamlit Community Cloud |
| **Development** | VS Code, Jupyter Notebook, Databricks |
| **Version Control** | Git, GitHub |

---

### 🔧 Core Technologies

**PySpark** is used to process, clean, transform, and analyze the large synthetic support-ticket dataset.

**Delta Lake** is used to organize processed data through Bronze, Silver, and Gold layers.

**Power BI** provides an interactive dashboard for monitoring customer-support KPIs and operational trends.

**Scikit-learn** is used to build and evaluate machine-learning models for Resolution SLA Prediction.

**Sentence Transformers** converts historical support cases into 384-dimensional semantic embeddings using `all-MiniLM-L6-v2`.

**Hybrid Retrieval** combines semantic cosine similarity with keyword matching to retrieve relevant historical support cases.

**RAG (Retrieval-Augmented Generation)** uses retrieved historical cases as context for support-resolution recommendations.

**Llama 3.2:1B + Ollama** provides local LLM-based response generation. The cloud deployment uses a retrieval-based fallback when Ollama is unavailable.

**Streamlit** provides the interactive SupportIQ web application and AI Support Assistant.

---


## 📂 Dataset

SupportIQ uses a large **synthetic customer-support dataset containing 1.2M+ ticket records**. The dataset was generated specifically for this project to simulate realistic enterprise support operations while also including intentional data-quality issues for ETL and data-cleaning practice.

### Dataset Features

Each support ticket contains information such as:

- Ticket and customer identifiers
- Assigned support agent
- Created and closed dates
- Priority and status
- Category and sub-category
- Product
- Support channel
- Issue description
- Resolution
- Customer region
- First-response time
- Resolution time
- Customer satisfaction score
- Escalation status

The support domains include:

`Core HR` • `Benefits` • `Payroll` • `Time Management` • `Recruitment` • `Performance`

### Intentional Data Quality Issues

The raw dataset contains intentionally introduced issues such as:

- Missing values
- Duplicate records
- Inconsistent text formatting
- Invalid priority values
- Invalid customer satisfaction values
- Invalid date relationships
- Resolution-time outliers

These issues allow the project to demonstrate a realistic **identify → inspect → clean → validate** ETL workflow.

---

## ⚙️ Data Engineering Pipeline

The raw support-ticket data is processed using **PySpark** and organized using a Medallion Architecture.

```text
Raw CSV
   │
   ▼
┌─────────────────────┐
│       BRONZE        │
│ Raw ingested data   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       SILVER        │
│ Cleaned & validated │
│ support ticket data │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│        GOLD         │
│ Analytics-ready     │
│ aggregated data     │
└──────────┬──────────┘
           │
           ├──────────────► Power BI
           │
           ├──────────────► Machine Learning
           │
           └──────────────► GenAI / RAG
```

### 🥉 Bronze Layer

The Bronze layer stores the ingested support-ticket data while preserving the raw structure for downstream processing.

### 🥈 Silver Layer

The Silver layer contains cleaned and validated support-ticket data. Processing includes handling missing values and duplicates, standardizing values, validating fields, and preparing reliable records for downstream analytics.

### 🥇 Gold Layer

The Gold layer contains analytics-ready datasets and aggregations used for reporting and business intelligence.

Spark SQL and PySpark transformations are used to create support metrics and analytical datasets consumed by the **Power BI dashboard** and downstream components.

---

## 📊 Power BI Dashboard

SupportIQ includes an interactive **Power BI dashboard** built on the processed Gold-layer support data.

The dashboard provides a consolidated view of customer-support operations and allows users to analyze ticket volume, resolution performance, customer satisfaction, escalation trends, and other operational metrics.

### Dashboard Filters

Interactive slicers allow the dashboard to be filtered by:

- Category
- Priority
- Channel
- Month

### Key Performance Indicators

The dashboard includes KPIs such as:

- **Total Tickets**
- **Open Tickets**
- **Resolved Tickets**
- **Escalated Tickets**
- **Average Resolution Time**
- **Average Customer Satisfaction (CSAT)**

### Dashboard Visualizations

The analytical views include:

- Monthly Ticket Volume
- Tickets by Category
- Tickets by Priority
- Ticket Status Distribution
- Channel-wise Ticket Distribution
- Customer Satisfaction Analysis
- Resolution Performance
- Escalation Analysis

### SLA Analysis

For project analysis, the following thresholds are used:

- **Resolution SLA:** ≤ 72 hours
- **First Response SLA:** ≤ 60 minutes

These thresholds are analytical assumptions used for this synthetic project and are **not intended to represent the SLA policy of any specific organization**.

The dashboard helps support teams identify operational trends, high-volume support areas, resolution bottlenecks, and service-performance patterns.

---

### 📷 Dashboard Preview

> Add a screenshot of the completed Power BI dashboard here.

## 🤖 Machine Learning — Resolution SLA Prediction

SupportIQ includes a Machine Learning component that predicts whether a support ticket is likely to meet the defined **72-hour resolution SLA**.

### Target Variable

The target variable was created using `resolution_hours`:

- **1 — SLA Met:** Resolution time ≤ 72 hours
- **0 — SLA Not Met:** Resolution time > 72 hours

Tickets without a resolution time were excluded from model training.

To prevent **data leakage**, `resolution_hours` itself was not used as an input feature.

### Model Features

The following ticket attributes were used:

- Priority
- Category
- Sub-category
- Product
- Channel
- Customer Region

### Models Evaluated

Three classification algorithms were evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.6435 | 0.4141 | 0.6435 | 0.5039 | 0.4996 |
| Decision Tree | 0.6435 | 0.4141 | 0.6435 | 0.5039 | 0.5000 |
| Random Forest | 0.6435 | 0.4141 | 0.6435 | 0.5039 | 0.5000 |

### Model Interpretation

The models achieved approximately **64% accuracy**, but the ROC-AUC remained close to **0.50**.

This indicates that the available synthetic features contain limited predictive signal for distinguishing between tickets that meet or miss the SLA. The accuracy is therefore influenced largely by the underlying class distribution rather than strong predictive separation.

Instead of presenting the accuracy alone, the project evaluates multiple metrics including **Precision, Recall, F1 Score, and ROC-AUC** to provide a more complete assessment of model performance.

Logistic Regression was retained as the baseline model for the downstream workflow.

### Key Learning

This result demonstrates an important Machine Learning principle:

> A high accuracy value does not necessarily mean that a classification model has strong predictive capability.

Model performance depends heavily on the quality of the available features and the relationship between those features and the target variable.

---

## 🧠 GenAI & Retrieval-Augmented Generation (RAG)

SupportIQ includes a **Retrieval-Augmented Generation (RAG)** pipeline that uses historical support cases to provide context-aware resolution recommendations.

Rather than relying only on an LLM's general knowledge, the system first retrieves relevant historical support cases and uses those cases as grounding context for the response.

### 📚 Knowledge Base

Cleaned support tickets from the Silver layer are transformed into a structured knowledge base containing:

- Category
- Sub-category
- Product
- Priority
- Issue description
- Historical resolution

Records without a valid historical resolution are excluded from the knowledge base.

After removing duplicate knowledge entries, the final knowledge base contains approximately **360 unique support-case combinations**.

Example:

```text
Category: Payroll
Sub Category: Overtime
Product: HCM
Priority: High
Issue: Overtime hours are not reflected in payroll
Resolution: Approved overtime information and payroll processing were reviewed and corrected
```

### 🔢 Semantic Embeddings

Support cases are converted into numerical vector representations using:

`sentence-transformers/all-MiniLM-L6-v2`

Each support case is represented by a **384-dimensional embedding vector**.

```text
Historical Support Case
          ↓
     MiniLM Model
          ↓
384-Dimensional Embedding
```

The embeddings allow SupportIQ to compare the semantic meaning of a user's question with historical support issues.

### 🔎 Hybrid Retrieval

SupportIQ combines two retrieval techniques:

**Semantic Similarity — 75%**

Cosine similarity compares the user's query embedding with the stored support-case embeddings.

**Keyword Matching — 25%**

Keyword overlap provides additional weight when important terms in the user's question match terms in historical issues.

The final retrieval score is calculated as:

```text
Final Score =
(Semantic Similarity × 0.75)
+
(Keyword Score × 0.25)
```

The highest-ranking support cases are then selected as context for the response.

### 🛡️ Relevance Filtering

A relevance threshold prevents unrelated questions from being forced into an incorrect support category.

For example:

```text
Question:
How do I cook chicken biryani?

Result:
I could not find sufficiently relevant historical
support cases for this question.
Further investigation may be required.
```

This helps reduce irrelevant or unsupported responses.

### 💬 RAG Response Pipeline

```text
User Question
      │
      ▼
MiniLM Query Embedding
      │
      ▼
Semantic Similarity
      +
Keyword Matching
      │
      ▼
Hybrid Retrieval
      │
      ▼
Top Relevant Historical Cases
      │
      ▼
Relevance Check
      │
      ▼
RAG Context
      │
      ├──────────── Local ────────────► Llama 3.2 via Ollama
      │
      └──────────── Cloud ────────────► Retrieval-Based Fallback
                                             │
                                             ▼
                                   Support Recommendation
```

### 🖥️ Local AI Mode

When SupportIQ is executed locally, the retrieved historical cases are provided as context to **Llama 3.2:1B running through Ollama**.

The assistant structures the response into:

1. **Likely Issue**
2. **Recommended Resolution**
3. **Recommended Next Steps**
4. **Escalation Recommendation**

### ☁️ Cloud Deployment Mode

The public Streamlit deployment does not depend on a locally running Ollama server.

When Ollama is unavailable, SupportIQ uses the retrieved historical case information to construct a lightweight structured response.

This keeps the public application functional without requiring a paid external LLM API.

### Example Retrieval

```text
User Question:
Employee cannot submit a leave request

Retrieved Case:
Category: Time Management
Sub-category: Leave
Issue: Employee leave request is not showing

Historical Resolution:
Employee leave information and request configuration
were reviewed and corrected.
```

Even though the user's wording differs from the stored issue, semantic retrieval identifies the relevant **Time Management → Leave** support case.

---

## 🖥️ Streamlit Application

SupportIQ provides an interactive **Streamlit web application** that brings the analytics and AI components together in a single interface.

The application is organized into four main sections:

### 🏠 Overview

The Overview page provides a high-level summary of the SupportIQ platform and its core components.

It highlights:

- **1.2M+ Support Tickets**
- **MiniLM Embedding Model**
- **384-Dimensional Embeddings**
- **Top-3 Vector Retrieval**
- **Llama 3.2 Local LLM**
- **Ollama Inference Engine**

---

### 💬 AI Assistant

The AI Assistant allows users to enter a support-related question in natural language.

Example:

```text
Overtime hours are not reflected in payroll
```

SupportIQ then:

```text
User Question
      ↓
Generate Query Embedding
      ↓
Search Historical Support Cases
      ↓
Hybrid Similarity Ranking
      ↓
Select Relevant Cases
      ↓
Relevance Validation
      ↓
Generate Structured Recommendation
```

A typical response contains:

- **Likely Issue**
- **Recommended Resolution**
- **Recommended Next Steps**
- **Escalation Recommendation**

The application also maintains conversation history during the active Streamlit session.

---

### 📚 Knowledge Base

The Knowledge Base page allows users to search the historical support knowledge directly.

Semantic search makes it possible to retrieve relevant cases even when the search wording is different from the stored issue description.

For example:

```text
Search:
Employee cannot submit a leave request

Relevant historical case:
Time Management → Leave
```

This provides visibility into the historical information used by the RAG pipeline.

---

### 🏗️ Architecture

The Architecture page provides a visual explanation of the SupportIQ workflow, including:

- Data generation
- PySpark processing
- Bronze, Silver, and Gold layers
- Power BI analytics
- Machine Learning
- Knowledge Base
- Embeddings
- Vector retrieval
- RAG
- Local LLM
- Streamlit application

---

### 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

SupportIQ supports two execution modes:

| Mode | Response Engine |
|---|---|
| **Local** | RAG + Llama 3.2:1B through Ollama |
| **Cloud** | RAG + Retrieval-Based Structured Fallback |

The cloud fallback allows the public application to remain functional without requiring a paid external LLM API or a locally running Ollama server.

---


## 🧪 RAG Testing & Results

The SupportIQ retrieval pipeline was tested using support questions from different functional areas as well as an unrelated query.

### Test 1 — Core HR

**Query:**

```text
Employee profile contains incorrect information
```

**Retrieved Classification:**

```text
Core HR → Employee Profile
```

**Historical Resolution:**

```text
Employee profile data and access configuration were reviewed and corrected.
```

**Result:** ✅ Correct retrieval and resolution

---

### Test 2 — Payroll

**Query:**

```text
Overtime hours are not reflected in payroll
```

**Retrieved Classification:**

```text
Payroll → Overtime
```

**Historical Resolution:**

```text
Approved overtime information and payroll processing were reviewed and corrected.
```

**Result:** ✅ Correct retrieval and resolution

---

### Test 3 — Benefits

**Query:**

```text
Employee is unable to enroll in benefits
```

**Retrieved Classification:**

```text
Benefits → Benefit Enrollment
```

**Historical Resolution:**

```text
Employee benefit eligibility and enrollment configuration were reviewed and corrected.
```

**Result:** ✅ Correct retrieval and resolution

---

### Test 4 — Semantic Retrieval

The following query intentionally uses wording that is different from the stored historical issue.

**Query:**

```text
Employee cannot submit a leave request
```

SupportIQ retrieved:

```text
Time Management → Leave
```

with the similar historical issue:

```text
Employee leave request is not showing
```

and the resolution:

```text
Employee leave information and request configuration were reviewed and corrected.
```

**Result:** ✅ Semantic retrieval successfully identified the relevant support case despite different wording.

---

### Test 5 — Out-of-Domain Query

**Query:**

```text
How do I cook chicken biryani?
```

**SupportIQ Response:**

```text
I could not find sufficiently relevant historical support cases for this question.
Further investigation may be required.
```

**Result:** ✅ The relevance threshold prevented an unrelated question from being mapped to an incorrect support case.

---

### Cloud Deployment Test

The deployed Streamlit application was also tested with:

```text
Overtime hours are not reflected in payroll
```

The application successfully retrieved:

```text
Payroll → Overtime
```

and returned the correct historical resolution using the cloud retrieval-based fallback.

Observed response time during this test:

```text
0.16 seconds
```

> Response time can vary depending on deployment state, network conditions, and application startup.

### Test Summary

| Test | Expected | Result |
|---|---|---|
| Core HR retrieval | Employee Profile | ✅ Passed |
| Payroll retrieval | Overtime | ✅ Passed |
| Benefits retrieval | Benefit Enrollment | ✅ Passed |
| Semantic query | Time Management → Leave | ✅ Passed |
| Unrelated query rejection | No support answer | ✅ Passed |
| Cloud fallback | Correct structured response | ✅ Passed |

These tests demonstrate that the retrieval pipeline can identify relevant historical support cases, handle semantically similar wording, and reject queries that fall outside the available support knowledge base.

---

## ⚠️ Limitations

SupportIQ is a portfolio and learning project built using synthetic support-ticket data. The following limitations should be considered when interpreting the results.

### Synthetic Dataset

The 1.2M+ support tickets are synthetically generated rather than collected from a real production support environment.

Although the dataset simulates enterprise support scenarios and intentional data-quality problems, it cannot fully reproduce the complexity and variability of real customer-support data.

### Machine Learning Performance

The Resolution SLA Prediction models achieved approximately **64% accuracy**, while ROC-AUC remained close to **0.50**.

This indicates limited predictive signal between the available synthetic features and the SLA target. The ML component therefore demonstrates the end-to-end modeling workflow rather than a production-ready predictive system.

### Knowledge Base Size

After removing duplicate knowledge entries, the RAG knowledge base contains approximately **360 unique support-case combinations**.

This is sufficient to demonstrate semantic retrieval and RAG concepts, but a production system would require a much larger and continuously updated knowledge base.

### Local LLM Dependency

LLM-based response generation uses **Llama 3.2:1B through Ollama**, which requires Ollama to be installed and running locally.

The public Streamlit deployment therefore uses a retrieval-based structured fallback instead of local LLM generation.

### Vector Search

The current implementation performs cosine similarity against the stored embedding matrix directly.

This works well for the current knowledge-base size, but a production-scale implementation with millions of embeddings would benefit from a dedicated vector-search system.

---

## 🔮 Future Improvements

Potential future enhancements include:

- Integrating real or more behaviorally realistic support-ticket data
- Engineering stronger features for SLA prediction
- Expanding the historical support knowledge base
- Adding automated knowledge-base updates from newly resolved tickets
- Using a dedicated vector database for large-scale retrieval
- Adding metadata filtering before semantic search
- Improving retrieval evaluation with metrics such as Precision@K and Recall@K
- Integrating a production-hosted LLM for cloud-based generation
- Adding user authentication and role-based access
- Adding feedback collection for AI recommendations
- Monitoring retrieval quality and model performance over time
- Building automated data and model pipelines for production deployment

---

## 🎯 Project Objective

The primary objective of SupportIQ is to demonstrate how multiple data and AI technologies can be integrated into a single end-to-end solution:

**Data Engineering → Analytics → Machine Learning → Semantic Search → RAG → Generative AI → Application Deployment**

The project focuses not only on model building, but also on data quality, scalable processing, evaluation, retrieval reliability, application development, and deployment.