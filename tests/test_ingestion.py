import pytest

def test_bronze_train_exists(spark):
    df = spark.table("retail_lakehouse.bronze.sales_raw_train")
    assert df.count() > 0, "Train bronze table is empty!"

def test_bronze_test_exists(spark):
    df = spark.table("retail_lakehouse.bronze.sales_raw_test")
    assert df.count() > 0, "Test bronze table is empty!"
