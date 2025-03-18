# Task 1: Local Chatbot with LLM Inference Using Ollama

## Overview
This project implements a local chatbot system using LLM inference on a personal laptop (CPU). It integrates Ollama LLM (Llama 3) for chatbot responses and provides a feature to find similar parts based on a description. To search similar parts please use **"similar parts"** key word in prompt and add partial or full desctription of the part. The system is designed to be used entirely locally, without relying on cloud-based services.

## Features
- Uses **Ollama LLM (Llama 3)** for chatbot responses.
- Retrieves similar parts from a CSV dataset.
- Supports real-time conversation.

## Setup Instructions

### Prerequisites
- **Python 3.12** installed  
- Install required dependencies:
  ```sh
  pip install pandas langchain_ollama

# Task 2: Binary Classification using random forest classifier

## Overview
This task implements a **Random Forest Classifier** to predict a binary classification label (`Type`: **y = 1, n = 0**). The dataset is created by merging two tables (`table_1.csv` and `table_2.csv`) based on a common ID column.  

## Dataset Overview

- Two tables (`table_1.csv`, `table_2.csv`) containing various features.
- Merged on the `ID` column to form a unified dataset.
- Categorical columns were label-encoded, converting string values into numerical form.
- **Missing values were handled**:
  - **Numerical columns:** Filled with the **mean** of the column.
  - **Categorical columns:** Filled with the **most frequent value (mode)**.
- **Binary target column (`Type`)**:
  - `'y'` was encoded as `1`
  - `'n'` was encoded as `0`
- **Final dataset was split** into:
  - **80% training data**
  - **20% test data**

## Model and Methodology

### 1. Data Preprocessing
- **Missing values handled** using **mean/mode imputation**.
- **Label encoding applied** to categorical features.
- **Removed any rows with NaN in the `Type` column**.

### 2. Model Training
- **Random Forest Classifier** with:
  - `n_estimators=100` (100 decision trees)
  - `random_state=42` (for reproducibility)
- **Training set:** 80% of the data.

### 3. Evaluation Metrics
The model was evaluated on the **test set (20%)** using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **Classification Report**
- **Confusion Matrix**

---

## Results

| Metric       | Score |
|--------------|--------|
| **Accuracy**  | 99.22% |
| **Precision** | 99.16% |
| **Recall**    | 100%   |
| **F1-Score**  | 99.58% |


# Task 3: Finding Similar Fictitious Parts Based on Description

## Overview
This project aims to identify 5 alternative parts for each fictitious part in the dataset based on description similarity. The dataset, `Parts.csv`, contains 998 rows and 32 columns, including *electrical technical details with part descriptions and ID. The approach focuses on text-based similarity matching to recommend the most relevant alternative parts.

### Key Observations
   - 663 non-null values out of 998 rows.  
   - 335 missing descriptions (~33%) were filled using structured text generation.  
   - Many descriptions were generated from technical attributes (e.g., movement type, voltage, temperature).  
   - Some parts had similar wording, which helped in similarity matching.  
   - columns contained electrical technical details.  

### Challenges and Solutions

- **Missing Descriptions** : Generated structured descriptions using key features (e.g., voltage, movement type).
- **Noisy Data** : Removed special characters and applied lowercasing for uniformity.
- **Finding Similar Parts Efficiently** : Used TF-IDF vectorization and cosine similarity for accurate matches.

## Solution Approach

### Step 1: Preprocessing
- Converted all text to lowercase for consistency.  
- Removed unnecessary characters (`| , / ()`) from all columns.  
- Generated missing descriptions using a structured, rule-based function.  
- used "unknown part" where neither description nor technical details are given`.  

### Step 2: TF-IDF Vectorization
- TF-IDF (Term Frequency-Inverse Document Frequency) was used to convert descriptions into numerical representations.  
- This ensured that important words had higher relevance, while common words had lower weight.  

### Step 3: Similarity Calculation
- Cosine similarity was applied to measure the textual similarity between descriptions.  
- For each part, the five most similar parts were identified (excluding itself).  

### Step 4: Storing Results
- The top 5 similar parts ID for each part were added as a new column: `"SIMILAR_PARTS"`.  If One also want description of similar parts with its ID one can change script accordingly.
- The updated dataset was saved as `Parts_with_similarities.csv`.  
