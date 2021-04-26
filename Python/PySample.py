
from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession,SQLContext
from pyspark.sql import  functions as F
from pyspark.sql.types import *


spark = SparkSession.builder.appName('PySample').master("local").getOrCreate()
# SQLContext=SQLContext(spark)

# sc= SparkContext(master="local",appName="PySample")

df= spark.read.csv("data.csv")

df.show(5)

