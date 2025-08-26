import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    # First try to grab active session (Databricks)
    spark = SparkSession.getActiveSession()
    if spark:
        return spark
    # Else fallback to local for dev
    return (
        SparkSession.builder
        .appName("retail-lakehouse-tests")
        .master("local[*]")
        .getOrCreate()
    )
