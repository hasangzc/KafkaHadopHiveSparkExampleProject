from pyspark import SparkContext                                                                                        
from pyspark.sql import SparkSession                                                                                    
from pyspark.streaming import StreamingContext                                                                          
from pyspark.sql.functions import  regexp_extract, cast
import json
import pandas as pd
from pyspark.sql.functions import regexp_replace


def write_to_hive(df, epoch_id):
    df.write.mode("overwrite").format("parquet").saveAsTable("trends")


spark_context = SparkContext(appName="TrendsProject")    
ssc = StreamingContext(spark_context, 5)   

# Create a SparkSession and set the Hive metastore URL
ss = SparkSession.builder.appName("TrendsProject").config("spark.sql.warehouse.dir",
 "/user/hive/warehouse").config("hive.metastore.uris", "thrift://localhost:9083").enableHiveSupport().getOrCreate()                                                                                                                                                       
                                                 
ss.sparkContext.setLogLevel('WARN')                                                                                     

# consumer = KafkaConsumer("trends", bootstrap_servers=["kafka-server:9092"], value_deserializer=json.loads)
# dstream = KafkaUtils.createDirectStream(ssc, ["trends"], {"metadata.broker.list": "kafka-server:9092"}, valueDecoder=json.loads)

dstream = ss.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "trends").load()


dstream = dstream.withColumn("value", dstream["value"].cast("string"))

dstream  = dstream.withColumn("value", regexp_replace(dstream["value"], "\n|\r", ""))

# Convert the DStream to a DataFrame and select the desired fields
df = dstream.selectExpr("get_json_object(value, '$.index') as index", "get_json_object(value, '$.title') as title",
                         "get_json_object(value, '$.subtitle') as subtitle", "get_json_object(value, '$.source') as source",
                        "get_json_object(value, '$.time_published') as time_published", "get_json_object(value, '$.searches') as searches")


# Add a new column with the numeric value of the "searches" field
# df = df.withColumn("searches_numeric", cast(regexp_extract("searches", "(\d+)", 1), "long"))

# Drop the original "searches" column
# df = df.drop("searches")

# Write the data to Hive
query = (
    dstream
    .writeStream
    .foreachBatch(write_to_hive)
    .format("parquet")
    .outputMode("append")
    .option("path", "/user/hive/warehouse/trends")
    .option("checkpointLocation", "/tmp/checkpoints")
    .start()
)

query.awaitTermination()
                                                                                                     








                                                                                                                

