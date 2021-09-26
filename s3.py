#! /usr/bin/env python3
import boto3 


resource=boto3.resource('s3')
bucket=resource.Bucket('bucket1')

response=bucket.create(
        ACL='private',
        CreateBucketConfiguration={
            'LocationConstraint':'us-east-1'
            },
        )



