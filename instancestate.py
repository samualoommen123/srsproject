import boto3
from botocore.exceptions import ClientError

import sys
import subprocess

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
                ImageId = 'ami-07d0cf3af28718ef8',
                MinCount = 1,
                MaxCount = 1,
                InstanceType = 't2.micro',
                KeyName = 'lambda',
                SubnetId = 'subnet-04cfee2a')
print (instance[0].id)
i = instance[0].id
print ("Instance: " + i)

response = instance.start()

for instance in ec2.instances.all():
    if instance.id == i:
            print (instance.id , instance.state)
            stCd = response.CurrentState['Name']
            print (stCd)

while stCd == 0:
        opt = int(raw_input("Select option: 1. Wait 2. Exit :"))
        print (stCd)
        if opt == 1:
                print("Waiting for the instance to be up and running")
        elif opt == 2:
                sys.exit()

