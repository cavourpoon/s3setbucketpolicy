import requests
import json
import boto3
import policy

bucket='your.s3.bucket'
client=boto3.client('s3')

def getPublicIp():
    data = requests.get("http://ip.jsontest.com/").json()
    return data['ip']

def getPolicy(bucket):
    try:
        print('Start getting bucket policy')
        response = client.get_bucket_policy(
            Bucket=bucket
        )
        if response['ResponseMetadata']['HTTPStatusCode']==200:
            print(response['Policy'])
            return True
    except:
        print('Cannot get policy')
        return False

def deletePolicy(buket):
    try:
        print('Start getting bucket policy')
        response = client.get_bucket_policy(
            Bucket=bucket
        )
        if response['ResponseMetadata']['HTTPStatusCode']==200:
            print(response['Policy'])
            return True
    except:
        print('Cannot get policy')
        return False

def updatePolicy(buket):
    try:
        publicip=getPublicIp()
        s3policy=policy.s3AllowPolicy(bucket,publicip)
        policystring=json.dumps(s3policy)
        response = client.put_bucket_policy(
            Bucket=buket,
            Policy=policystring
        )
        if str(response['ResponseMetadata']['HTTPStatusCode']).startswith('20'):
            print('Update successfully')
    except:
        print('Update not successful')

updatePolicy(bucket)