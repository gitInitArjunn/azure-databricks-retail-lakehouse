from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, current_timestamp

spark = SparkSession.builder.getOrCreate()

# ---------------------------
# 1. Load Bronze
# ---------------------------
df_train = spark.table("retail_lakehouse.bronze.sales_train")
df_test  = spark.table("retail_lakehouse.bronze.sales_test")

# ---------------------------
# 2. Clean Train
# ---------------------------
df_train_clean = (
    df_train
    .withColumn("date", to_date(col("date"), "dd-MM-yyyy"))
    .withColumn("store", col("store").cast("int"))
    .withColumn("item", col("item").cast("int"))
    .withColumn("sales", col("sales").cast("int"))
    .withColumn("cleaned_at", current_timestamp())
)

# ---------------------------
# 3. Clean Test
# ---------------------------
df_test_clean = (
    df_test
    .withColumn("date", to_date(col("date"), "dd-MM-yyyy"))
    .withColumn("store", col("store").cast("int"))
    .withColumn("item", col("item").cast("int"))
    .withColumn("id", col("id").cast("int"))
    .withColumn("cleaned_at", current_timestamp())
)

# ---------------------------
# 4. Write to Silver
# ---------------------------
(
    df_train_clean.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("retail_lakehouse.silver.sales_train_clean")
)

(
    df_test_clean.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("retail_lakehouse.silver.sales_test_clean")
)

print("✅ Train & Test cleaned and written to Silver")
