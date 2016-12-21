import boto3
import datetime
import random
import retrying

class Retryer(object):

    def __init__(self, volume_id):
        self.volume_id = volume_id
        self.client = boto3.client('ec2')


    def go(self):
        snapshot_id = self._attempt()
        return snapshot_id


    @retrying.retry(
        stop_max_attempt_number=5,
        wait_exponential_multiplier=1000,
        wait_exponential_max=10000,
        wait_random_min=1000,
        wait_random_max=5000)
    def _attempt(self):
        desc = '{0}-{1}'.format('snap', datetime.datetime.now().isoformat())
        response = self.client.create_snapshot(Description=desc, VolumeId=self.volume_id)
        return response['SnapshotId']

