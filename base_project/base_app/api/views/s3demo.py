import boto3
# from boto import aws_connection
from boto.s3.key import Key

# create bucket
# client = boto3.client('s3', region_name='us-east-1')
# # bkt_name = "a-bucket-created-for-python"
# # res = client.create_bucket(Bucket = bkt_name)
# list bucket
# res = s3.list_buckets()
# for i in res['Buckets']:
#
#     if i['Name'] == "a-bucket-created-for-python":
#         print(" Bucket detail %s", i)

# # upload csv to s3
# s3 = boto3.resource('s3', region_name='us-east-1')
# s3.Object('a-bucket-created-for-python', 'airport_data.csv').put(Body=open('/tmp/airport_head.csv', 'rb'))



