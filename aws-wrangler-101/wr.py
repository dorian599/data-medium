import awswrangler as wr
import pandas as pd

# Read remote CSV file into a Pandas data frame
#
df = pd.read_csv("http://csv-url-here.com/file.csv")

# Inspect the first 10 records of the dataframe
#
df.head()

# Write the Dataframe to a S3 bucket in CSV format
#
wr.s3.to_csv(df, "s3://BUCKET_NAME/file.csv",index=False, line_terminator='\n')

# Write the Dataframe to a S3 bucket in Parquet format
#
wr.s3.to_parquet(df, "s3://BUCKET_NAME/file.parquet")
