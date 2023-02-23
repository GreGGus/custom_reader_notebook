# Databricks notebook source
# MAGIC %run ../custom_reader_notebook/delta/delta_add_date

# COMMAND ----------

from runtime.nutterfixture import NutterFixture, tag
class DateTestFixture(NutterFixture):
   def assertion_date(self):
      date = generate_date() # from notebook
      date_str = date.strftime("%B")
      assert date_str=="May"

result = DateTestFixture().execute_tests()
print(result.to_string())
is_job = dbutils.notebook.entry_point.getDbutils().notebook().getContext().currentRunId().isDefined()
print(is_job)
result.exit(dbutils)
if is_job:
    print("ici")
    result.exit(dbutils)


# COMMAND ----------


