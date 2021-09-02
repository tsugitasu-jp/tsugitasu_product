import os
from config.settings.product import AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from config.settings.base import MEDIA_ROOT

from boto3.session import Session

session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

s3 = session.resource('s3')
content_bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)

def contetn_upload_to_s3(cid: int, bid: int, vid: int, fileName:str):
    path = f"{cid}/b{bid}/v{vid}/{fileName}"
    local_path = os.path.join(MEDIA_ROOT, path)
    content_bucket.upload_file(local_path, path)