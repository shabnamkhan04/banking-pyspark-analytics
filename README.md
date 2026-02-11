# Banking PySpark Analytics Project

## Overview

This project demonstrates a **real-world banking data analytics pipeline** built using **PySpark**. It simulates transaction processing, fraud detection, and analytics similar to what data engineers build in financial institutions.

The goal of this project is to showcase **production-level data engineering skills** including:

* Data ingestion
* Transformations with Spark
* Window-based fraud detection
* Partitioned Parquet data lake storage
* Delta Lake upserts
* Layered Bronze–Silver–Gold architecture

---

## Tech Stack

* **Python 3**
* **PySpark**
* **Delta Lake**
* **Parquet Data Lake**
* **Git & GitHub**

---

## Project Structure

```
banking-pyspark-project/
│
├── data/
│   └── transactions.csv
│
├── scripts/
│   └── banking_pipeline.py
│
├── output/
│   ├── daily_transaction/
│   └── high_value_transactions/
│
└── README.md
```

---

## Key Features

### 1. Transaction Processing

* Reads raw banking transactions
* Cleans and transforms data using Spark DataFrames

### 2. Fraud Detection using Window Functions

* Detects **multiple rapid transactions per account**
* Demonstrates real banking fraud‑monitoring logic

### 3. Partitioned Parquet Write

* Stores processed data partitioned by **date**
* Mimics scalable **data lake storage** used in enterprises

### 4. Delta Lake Support

* Enables **ACID transactions** and **upserts**
* Critical for **changing transaction status** in banking systems

### 5. Bronze → Silver → Gold Architecture

* **Bronze:** Raw ingested data
* **Silver:** Cleaned and validated transactions
* **Gold:** Aggregated analytics for reporting

---

## How to Run the Project

### 1. Install dependencies

```bash
pip install pyspark delta-spark
```

### 2. Run pipeline

```bash
python scripts/banking_pipeline.py
```

### 3. Output

* Partitioned **Parquet files** in `output/`
* Fraud‑filtered **high‑value transactions**

---

## Architecture Diagram

```
CSV Transactions
      ↓
   PySpark ETL
      ↓
 Fraud Detection (Window)
      ↓
 Silver Clean Data
      ↓
 Partitioned Parquet / Delta
      ↓
   Gold Analytics Layer
```

---

## Real‑World Relevance

This project reflects tasks performed by **Data Engineers in banking and fintech**:

* Handling high‑volume transaction streams
* Implementing fraud detection logic
* Managing scalable data lakes
* Supporting analytics and dashboards

---

## Author

**Shabnam Khan**
Aspiring Data Engineer | PySpark | SQL | Azure | Data Analytics

GitHub: [https://github.com/shabnamkhan04](https://github.com/shabnamkhan04)

---

## License

This project is for **learning and portfolio purposes**.
