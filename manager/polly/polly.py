import logging
import os
import boto3
from botocore.exceptions import ClientError

class CreateSound:

    def __init__(self):
        self.ACCESS_KEY = os.environ['ACCESS_KEY']
        self.SECRET_KEY = os.environ['SECRET_KEY']
        self.REGION_NAME = os.environ['REGION_NAME']
        self.BUCKETS_NAME = os.environ['BUCKETS_NAME']
        self.ROOT = os.environ['ROOT']
        self.polly_client = boto3.Session(aws_access_key_id=self.ACCESS_KEY,
                                          aws_secret_access_key=self.SECRET_KEY,
                                          region_name=self.REGION_NAME).client('polly')
        self.s3_client = boto3.Session(aws_access_key_id=self.ACCESS_KEY,
                                         aws_secret_access_key=self.SECRET_KEY,
                                         region_name=self.REGION_NAME).client('s3')

    def polly_task(self, text: str):
        response = self.polly_client.start_speech_synthesis_task(
            Engine='neural',
            LanguageCode='en-US',
            OutputS3BucketName=self.BUCKETS_NAME,
            OutputFormat='mp3',
            SampleRate='24000',
            VoiceId='Salli',
            Text=text)
        task_id = response['SynthesisTask']['TaskId'] + ".mp3"
        name_file = text.replace(" ", "_") + ".mp3"

        print(task_id, name_file)

        return task_id, name_file


    def get_url_sound(self, object_name: str, expiration=600):
        try:
            response = self.s3_client.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': self.BUCKETS_NAME, 'Key': object_name},
                                                             ExpiresIn=expiration)
        except ClientError as e:
            logging.error(e)
            return None
        return response

    def create_sound(self, text):
        task_id, name_file = self.polly_task(text)
        url_file_sound = self.get_url_sound(task_id)
        return url_file_sound, name_file
