from pyspark.sql import SparkSession, functions as F, Window


def run_process():
    # -----------------------------
    # Initialize Spark
    # -----------------------------
    spark = SparkSession.builder \
        .appName("Silver_to_Gold_Processing") \
        .getOrCreate()

    # -----------------------------
    # Load Silver Data
    # -----------------------------
    train_silver = spark.table("retail_lakehouse.silver.sales_train_clean")
    test_silver = spark.table("retail_lakehouse.silver.sales_test_clean")

    # -----------------------------
    # Feature Engineering for Train
    # -----------------------------
    train = train_silver \
        .withColumn("year", F.year("date")) \
        .withColumn("month", F.month("date")) \
        .withColumn("dayofweek", F.dayofweek("date")) \
        .withColumn("is_weekend", F.when(F.dayofweek("date").isin([1, 7]), 1).otherwise(0))

    # -----------------------------
    # Lag & Rolling Features
    # -----------------------------
    window_store_item = Window.partitionBy("store", "item").orderBy("date")

    # Lag features
    train = train \
        .withColumn("sales_lag_1", F.lag("sales", 1).over(window_store_item)) \
        .withColumn("sales_lag_7", F.lag("sales", 7).over(window_store_item))

    # Rolling averages
    train = train \
        .withColumn("sales_roll7_avg", F.avg("sales").over(window_store_item.rowsBetween(-6, 0))) \
        .withColumn("sales_roll30_avg", F.avg("sales").over(window_store_item.rowsBetween(-29, 0)))

    # -----------------------------
    # Gold Layer: Train
    # -----------------------------
    train_gold_cols = [
        "date", "store", "item", "sales", "year", "month", "dayofweek", "is_weekend",
        "sales_lag_1", "sales_lag_7", "sales_roll7_avg", "sales_roll30_avg",
        "ingested_at", "source_file", "batch_id", "cleaned_at"
    ]

    train_gold = train.select(*train_gold_cols)

    # Write to Gold
    train_gold.write.mode("overwrite").format("delta").saveAsTable("retail_lakehouse.gold.sales_train")

    # -----------------------------
    # Gold Layer: Test (Copy as-is)
    # -----------------------------
    test_gold_cols = [
        "id", "date", "store", "item",
        "ingested_at", "source_file", "batch_id", "cleaned_at"
    ]
    test_gold = test_silver.select(*test_gold_cols)
    test_gold.write.mode("overwrite").format("delta").saveAsTable("retail_lakehouse.gold.sales_test")

    print("✅ Silver → Gold processing completed successfully")



