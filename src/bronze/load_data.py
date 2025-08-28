from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit
import json

def run_ingestion(storage_account, container_name, account_key):
    # Configure Spark to access ADLS Gen2 via ABFSS
    spark = SparkSession.builder.getOrCreate()
    spark.conf.set(f"fs.azure.account.key.{storage_account}.dfs.core.windows.net", account_key)

    # ---------------------------
    # 3. Load raw CSVs from ABFSS path
    # ---------------------------
    train_path = f"abfss://{container_name}@{storage_account}.dfs.core.windows.net/sales/train.csv"
    test_path  = f"abfss://{container_name}@{storage_account}.dfs.core.windows.net/sales/test.csv"

    # Read train CSV
    df_train = spark.read.csv(train_path, header=True, inferSchema=True) \
        .withColumn("ingested_at", current_timestamp()) \
        .withColumn("source_file", lit("train.csv")) \
        .withColumn("batch_id", lit("batch_001"))

    # Read test CSV
    df_test = spark.read.csv(test_path, header=True, inferSchema=True) \
        .withColumn("ingested_at", current_timestamp()) \
        .withColumn("source_file", lit("test.csv")) \
        .withColumn("batch_id", lit("batch_001"))

    # ---------------------------
    # 4. Write to Bronze Delta Tables in Unity Catalog
    # ---------------------------
    df_train.write.format("delta").mode("overwrite").saveAsTable("retail_lakehouse.bronze.sales_train")
    df_test.write.format("delta").mode("overwrite").saveAsTable("retail_lakehouse.bronze.sales_test")

    # ---------------------------
    # 5. Verify tables
    # ---------------------------
    # print("Train table preview:")
    # display(spark.sql("SELECT * FROM retail_lakehouse.bronze.sales_train LIMIT 5"))

    # print("Test table preview:")
    # display(spark.sql("SELECT * FROM retail_lakehouse.bronze.sales_test LIMIT 5"))
