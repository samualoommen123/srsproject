import boto3
from botocore.exceptions import ClientError

import sys
import subprocess

ec2 = boto3.resource('ec2')

function instanceEIP(){
  instanceCreate();
}

function instanceCreate(){
    instance = ec2.create_instances(
                ImageId = 'ami-07d0cf3af28718ef8',
                MinCount = 1,
                MaxCount = 1,
                InstanceType = 't2.micro',
                KeyName = 'lambda',
				  SubnetId = 'subnet-04cfee2a')
  print (instance[0].id)
  var instanceID = instance[0].id
  var params = {
        InstanceIds: [instanceID]
  };
  ec2.waitFor('instanceRunning', params, function(err, data){
  if (err){
    console.log(err, err.stack);
                }// an error occurred
  else {
                    console.log("Instance IS Running" + JSON.stringify(data));
                    instanceEipAlloc();
                }         // successful response
            });
  }

function instanceEipAlloc(){
 try:
    allocation = ec2.allocate_address(Domain='vpc-4648272e')
    response = ec2.associate_address(AllocationId=allocation['AllocationId'],
                                     InstanceId=instanceID)
    print(response)
 except ClientError as e:
    print(e)
}

module.exports.handler = instanceEIP;

