# Azure Databricks Retail Lakehouse

End-to-end lakehouse project built on **Azure Databricks**, demonstrating:
- Raw data ingestion (Bronze)
- Transformations & cleaning (Silver)
- Aggregations & business metrics (Gold)
- Machine Learning (forecasting & pricing)
- Visualization with Databricks SQL

## 🏗️ Project Structure

azure-databricks-retail-lakehouse/
├─ src/                        # All your Databricks jobs/notebooks
│   ├─ ingestion/              # Bronze: raw ingestion scripts
│   ├─ transformations/        # Silver: cleaning + joins
│   ├─ gold/                   # Gold: aggregates, business-ready tables
│   └─ ml/                     # Machine learning (forecasting/pricing)
├─ infra/                      # Infrastructure & config
│   ├─ unity_catalog_setup.sql # Catalog & schema creation
│   └─ storage_config.json     # Storage mount/config details
├─ jobs/                       # Workflow/job JSON definitions
│   └─ workflows.json
├─ dbsql/                      # SQL queries & dashboard notes
│   └─ dashboards.md
├─ tests/                      # Unit tests for PySpark transforms
│   └─ test_transforms.py
├─ data/                       # Only small local test CSVs (not prod data)
├─ README.md                   # Project overview

## 🚀 Tech Stack
- Azure Databricks
- Azure Data Lake Gen2
- Unity Catalog
- PySpark / Delta Lake
- MLflow
- Databricks SQL

## 📊 Dataset
[Kaggle: Store Item Demand Forecasting Challenge](https://www.kaggle.com/competitions/demand-forecasting-kernels-only/data)

## 🔗 Links
- [Project GitHub Repo](#)
- [LinkedIn Project Post](#)

├─ requirements.txt            # Python deps (mlflow, pandas, etc.)
└─ .github/workflows/ci.yml    # CI/CD pipeline (lint/tests/deploy)
