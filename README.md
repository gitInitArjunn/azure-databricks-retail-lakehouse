# Azure Databricks Retail Lakehouse

End-to-end lakehouse project built on **Azure Databricks**, demonstrating:
- Raw data ingestion (Bronze)
- Transformations & cleaning (Silver)
- Aggregations & business metrics (Gold)
- Machine Learning (forecasting & pricing)
- Visualization with Databricks SQL

## 🏗️ Project Structure

azure-databricks-retail-lakehouse/  
├─ src/  
│  ├─ ingestion/  
│  ├─ transformations/  
│  ├─ gold/  
│  └─ ml/  
├─ infra/  
│  ├─ unity_catalog_setup.sql  
│  └─ storage_config.json  
├─ jobs/  
│  └─ workflows.json  
├─ dbsql/  
│  └─ dashboards.md  
├─ tests/  
│  └─ test_transforms.py  
├─ data/  
└─ README.md

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
