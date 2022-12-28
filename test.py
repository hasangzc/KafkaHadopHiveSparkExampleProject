from pyspark.sql import SparkSession
import pandas as pd

# Create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Read a Parquet file from HDFS into a DataFrame
df = spark.read.parquet("/user/hive/warehouse/trends/part-00000-bbac1cd5-7d95-4a2b-a7f2-54a5ce2db70e-c000.snappy.parquet")

df.printSchema()
# Print the contents of the DataFrame
df.select("value").show()

pandas_df = df.select("value").toPandas()
pandas_df.to_csv("/home/hasan/output.csv", index=False)
print(pandas_df)

