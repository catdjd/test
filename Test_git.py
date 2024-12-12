import pandas as pd
import boto3
from io import BytesIO

# Test connect minio python
# s3_client = boto3.client(
#     's3',
#     aws_access_key_id="BKky9mVTl8KoPVCmZZ78",
#     aws_secret_access_key="ZszY0hLzFcJscU8fwAg1bLYSMuWHwpyDpWwfhtmA",
#     endpoint_url="http://18.140.117.93:9000" , 
#     region_name='us-east-1' 
# )

# bucket_name = "raw"
# file_path = "CRMUSER_ACCOUNTS.csv"

# # Đọc dữ liệu từ MinIO
# response = s3_client.get_object(Bucket=bucket_name, Key=file_path)

# # Đọc dữ liệu từ response và chuyển thành DataFrame nếu là CSV
# csv_data = response['Body'].read()
# df = pd.read_csv(BytesIO(csv_data))

# df.head()

# Test read file local 
csv_path = "CRMUSER_ACCOUNTS.csv"
df = pd.read_csv(BytesIO(csv_data)) 
df.head()
