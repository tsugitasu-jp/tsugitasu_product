import os
from typing import List
from config.settings import MEDIA_ROOT

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from boto3.session import Session

class FileManager():
    def __init__(self, file, image_main, image_subs, cid, bid, vid) -> None:
        self.file = file
        self.image_main= image_main
        self.image_subs = image_subs
        self.u_path = f"{cid}/b{bid}/v{vid}"
    
    def test_init(self):
        from config.settings import AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
        # sessionの作成
        self.session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        # s3の用意
        s3 = self.session.resource('s3')
        self.content_bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)

    # mediaパスへのアップロード(template)
    def media_save(self, path, file) -> str:
        name = default_storage.save(path, ContentFile(file.read()))
        return name
    
    # fileのmediaパスへのアップロード
    def file_save_to_media(self):
        path = os.path.join(MEDIA_ROOT, f"{self.u_path}/{self.file.name}")
        return self.media_save(path, self.file).split('/')[-1]
    
    # 見出し画像のmediaパスへのアップロード
    def main_img_save_to_media(self):
        path = os.path.join(MEDIA_ROOT, f"{self.u_path}/{self.image_main.name}")
        return self.media_save(path, self.image_main).split('/')[-1]

    # サブ画像(複数のmediaパスへのアップロード)
    def sub_imgs_save_to_media(self) -> List:
        name_lst = []
        for img in self.image_subs:
            path = os.path.join(MEDIA_ROOT, f"{self.u_path}/{img.name}")
            name_lst.append(self.media_save(path, img).split('/')[-1])
        return name_lst

    # s3への単体アップロード(test時のみ)
    def content_upload_to_s3(self, local_path, path):
        self.content_bucket.upload_file(local_path, path)

    # s3への複数アップロード(test時のみ)
    def contetns_upload_to_s3(self, fileNameList):
        for name in fileNameList:
            path = f"{self.u_path}/{name}"
            local_path = os.path.join(MEDIA_ROOT, path)
            self.content_upload_to_s3(local_path, path)
        