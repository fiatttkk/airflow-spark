from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark Hello World").getOrCreate()

print("Hello, world!")