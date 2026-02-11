from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, sum
spark=SparkSession.builder.appName("BankingTransactionAnalytics").getOrCreate()
df = spark.read.csv("data/transactions.csv", header=True, inferSchema=True)
df = df.dropna(subset=["transaction_id","transaction_time","transaction_amount"])
df = df.withColumn("transaction_amount", col("transaction_amount").cast("double"))
daily_df = df.withColumn("date", to_date("transaction_time")) \
    .groupBy("customer_id", "date") \
    .agg(sum("transaction_amount").alias("daily_total"))
fraud_df = df.filter(col("transaction_amount") > 10000) 
daily_df.write.mode("overwrite").parquet("output/daily_transaction")
fraud_df.write.mode("overwrite").parquet("output/high_value_transactions")
print("Pipeline completed successfully!")

