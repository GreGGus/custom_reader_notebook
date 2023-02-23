# Databricks notebook source
def read_delta_table(name):
    return spark.read.table(name)

# COMMAND ----------

import datetime

def generate_date():
    x = datetime.datetime(2020, 5, 17)
    return x


# COMMAND ----------


