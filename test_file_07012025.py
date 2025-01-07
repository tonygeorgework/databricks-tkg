# Databricks notebook source


# COMMAND ----------

#exploring open source datasets on dbfs
dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

#Checking power-plant open source dataset
dbutils.fs.ls('/databricks-datasets/power-plant/data/')

# COMMAND ----------

#Creating spark dataframe from open source dataset
df1=spark.read.csv('dbfs:/databricks-datasets/power-plant/data/Sheet1.tsv')

# COMMAND ----------

df1.limit(5).show()
