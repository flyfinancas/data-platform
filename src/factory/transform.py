from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, ArrayType, TimestampType
spark = SparkSession.builder.appName("Fly").getOrCreate()

class Transformer:
    def __init__(self, df, schema):
        self.df = df
        self.schema = schema

    def df_reader(self, df, schema):
        df = spark.createDataFrame(df, schema=schema)

if __name__ == "__main__":
    pass