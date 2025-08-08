# 🏥 Big Data Analytics & Visualization for Healthcare Insights 

---

## 📌 Overview
This project uses **PySpark**, **matplotlib**, and **Hadoop MapReduce** to process, analyze, and visualize large-scale healthcare data from Consulting Labs.  
The goal is to uncover patterns in test requests, identify seasonal trends, and provide actionable insights for better resource allocation, staffing, and patient care.

---

## 📊 Key Features
- **Data Merging & Cleaning**: Integrated and preprocessed 11 Excel files (~300k rows, expanded to ~800k rows).
- **Statistical & Graphical Analysis**:
  - Top 10 most requested tests with demand classification (High/Medium/Low).
  - Monthly and seasonal trends in test requests.
  - Predictive modeling using Decision Tree Regression.
- **Big Data Tools**:
  - **PySpark** for scalable data processing.
  - **Hadoop MapReduce** for distributed word count on requested test names.
- **Visualization**:
  - Bar charts, line charts, and seasonal breakdowns for easy interpretation.

---

## 🔍 Insights
- **CBC** (Complete Blood Count) is the most requested test, followed by Urine Analysis.
- Peak demand occurs in **summer** and **fall**; spring has the lowest demand.
- Predictive modeling can help anticipate busy months, improving staffing and supply management.

---
