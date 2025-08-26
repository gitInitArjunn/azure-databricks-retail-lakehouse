# process.py

from pyspark.sql import SparkSession, functions as F

# -----------------------------
# Initialize Spark session
# -----------------------------
spark = SparkSession.builder \
    .appName("Gold Layer Validation") \
    .getOrCreate()


# -----------------------------
# Null Check (all columns)
# -----------------------------
def null_report(df, df_name):
    print(f"\n🔎 Null Check for {df_name}:")
    null_counts = df.select([
        F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in df.columns
    ])
    null_counts.show(truncate=False)


# -----------------------------
# Duplicate Check
# -----------------------------
def duplicate_report(df, df_name, subset_cols):
    print(f"\n🔎 Duplicate Check for {df_name}:")
    dup_count = df.groupBy(subset_cols).count().filter(F.col("count") > 1).count()
    if dup_count > 0:
        print(f"⚠️ Found {dup_count} duplicate rows based on {subset_cols}")
    else:
        print("✅ No duplicates found")


# -----------------------------
# Sales Sanity Check (Train only)
# -----------------------------
def sales_sanity(df):
    print("\n🔎 Sales Sanity Check:")
    df.select(
        F.min("sales").alias("min_sales"),
        F.max("sales").alias("max_sales"),
        F.mean("sales").alias("avg_sales")
    ).show()
    invalid_sales = df.filter(F.col("sales") < 0).count()
    if invalid_sales > 0:
        print(f"⚠️ Found {invalid_sales} rows with negative sales")
    else:
        print("✅ No negative sales values")


# -----------------------------
# Run Validation
# -----------------------------
def run_validation(train_gold, test_gold):
    # Null check
    null_report(train_gold, "Train Gold")
    null_report(test_gold, "Test Gold")

    # Duplicate check
    duplicate_report(train_gold, "Train Gold", ["date", "store", "item"])
    duplicate_report(test_gold, "Test Gold", ["id"])

    # Sales sanity (only train has sales)
    sales_sanity(train_gold)


# -----------------------------
# Main execution
# -----------------------------
if __name__ == "__main__":
    # Load Gold tables
    train_gold = spark.table("retail_lakehouse.gold.sales_train")
    test_gold = spark.table("retail_lakehouse.gold.sales_test")

    # Run all validations
    run_validation(train_gold, test_gold)
