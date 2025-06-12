from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()

data = spark.read.csv(
    './resources/data/brooklyn_sales_map.csv', inferSchema=True, header=True)
data.show(5)
