#! /usr/bin/env python3
import boto3,json,os,glob 

#specify that we want to use S3 as a resource
#and the name of the bucket that we want to create
resource=boto3.resource('s3')
bucket=resource.Bucket('bucket1')

#Create the actual resources 
response=bucket.create(
        ACL='private',
        CreateBucketConfiguration={
            'LocationConstraint':'us-east-1'
            },
        )


#how many buckets we have created so far 
list=(resource.buckets.all())
len(list)


#the name of all the buckets we have created 
for x in resource.buckets.all():
    print(x.name)


#Get creation date of aws bucket as well as name
client=boto3.client('s3')
for x in client.list_buckets()['Buckets']:
    print(x['Name'])
    print(x['CreationDate'])


#set policy for s3 
bucket_policy={
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"PublicRead",
      "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject","s3:GetObjectVersion"],
      "Resource":["arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"]
    }
  ]
}
#set the policy as a json dump 
bucket_policy=json.dump(bucket_policy)
#upload the policy to your bucket 
client.put_buckey_policy(Bucket='Bucketname',Policy=bucket_policy)


#getting the policy of your bucket 
client.get_bucket_policy(Bucket='Bucketname')['Policy']


#deleting buckets policy
client.delete_bucket_policy(Bucket="Bucketname")


#uploading files to bucket
#filename is the how you want to name the uploaded file 
#bucket is the bucket you want to upload the file to 
#key is where the file is located in your system
client.upload_file(
        Filename='filename.png',
        Bucket='Bucketname',
        Key='filename.png'
)


#uploading multiple files 
#get your current working directory 
cwd = os.getcwd()
#get the files in your directory 
files = glob.glob(cwd+'.png')
#loop through all files and upload it 
for x in files :
    client.upload_file(
            Filename=x,
            Bucket='Bucketname',
            Key=file.split("/")[-1]
            )
    
#get all the objects in your bucket 
objects = client.list_objects(Bucket='Bucketname')['Contents']
for x in objects:
    print(object['Key'])


#delete single objecct in a bucket 
client.delete_object(Bucket="Bucketname",Key="nameofobject.png")
#delete multiple obejcts in a bucket 
objects1 = client.list_objects(Bucket="Bucketname")['Contents']
for x in object2 :
    client.delete_object(Bucket="Bucketname",Key = x)


#download single file from s3 bucket 
client.download_file(Bucket='Bucketname',
        Key="filename.png",
        Filename='filename.png'
)
#download multiple files from s3 bucket
files=client.list_objects(Bucket='Bucketname')["Contents"]
for x in files:
    client.download_file(Bucket="Bucketname",
            Key=x["Key"],
            Filename=x["Key"]
        )























