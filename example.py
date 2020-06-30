import os
from google.cloud import storage

# get key here:
# https://console.cloud.google.com/apis/credentials/serviceaccountkey
# export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/my-key.json"
key_path = "gcloud_key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

bucket = 'test-bucket-varmit-stronghold'

text_file = open("hello.txt", "w")
text_file.write("hello world")
text_file.close()

client = storage.Client()
bucket = client.get_bucket(bucket)

blob = bucket.blob('hello_from_file.txt')
blob.upload_from_filename(filename='hello.txt')
print(blob.download_as_string())

blob2 = bucket.blob('hello_from_string.txt')
blob2.upload_from_string('hello again!')
print(blob2.download_as_string())




