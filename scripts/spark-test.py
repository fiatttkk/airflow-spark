from pyspark.sql import SparkSession

file_path = '/opt/airflow/data/movie_profit.csv'

# Create Spark Session
spark = SparkSession.builder \
    .appName("Test_001") \
    .getOrCreate()
    
df = spark.read.format('csv').option('header', True).load(file_path)
df.show()

spark.stop()