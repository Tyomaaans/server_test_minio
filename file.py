from minio import Minio
from minio.error import S3Error

client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

b_name = "testbucket"

try:
    if not client.bucket_exists(b_name):
        client.make_bucket(b_name)
        print('Bucket Created')
    else:
        print('Bucket Cannnot Created')
except S3Error as e:
    print(f"Error: {e}")