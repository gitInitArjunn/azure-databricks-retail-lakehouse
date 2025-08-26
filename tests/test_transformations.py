import pytest

def test_train_columns(spark):
    df = spark.table("retail_lakehouse.silver.sales_train_clean")
    expected_cols = {"date", "store", "item", "sales", "cleaned_at"}
    assert expected_cols.issubset(set(df.columns)), f"Train table missing columns: {expected_cols - set(df.columns)}"

def test_test_columns(spark):
    df = spark.table("retail_lakehouse.silver.sales_test_clean")
    expected_cols = {"id", "date", "store", "item", "cleaned_at"}
    assert expected_cols.issubset(set(df.columns)), f"Test table missing columns: {expected_cols - set(df.columns)}"

def test_no_null_sales_in_train(spark):
    df = spark.table("retail_lakehouse.silver.sales_train_clean")
    assert df.filter(df.sales.isNull()).count() == 0, "Train data has null sales!"
