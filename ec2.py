import boto3
import sys


def turnEC2(action, instanceId):
    instances = []
    ec2 = boto3.client('ec2')
    if instanceId == "all":
        instances = describeEC2s()
    else:
        instances = instanceId.split(',')

    if action == "ON":
        try:
            ec2.start_instances(InstanceIds=instances)
            print("Starting..")
        except Exception as e:
            raise
    else:
        try:
            ec2.stop_instances(InstanceIds=instances)
            print("Stopping...")
        except Exception as e:
            raise


def createEC2(number):
    try:
        print(f'creating {number} instances... \n')
        ec2 = boto3.resource('ec2')
        ec2.create_instances(
            ImageId="ami-053b0d53c279acc90",
            MinCount=1,
            MaxCount=int(number),
            InstanceType="t2.micro",
            KeyName="ec2"
        )
    except Exception as e:
        raise
    print("new instance(s) id(s): \n")
    print(describeEC2s())


def describeEC2s():
    instances = []
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            instances.append(i['InstanceId'])
    print(instances)
    return instances


def terminateEC2(ids):
    instances = []
    ec2 = boto3.client('ec2')
    try:
        if ids == "all":
            print("terminating all: \n")
            instances = describeEC2s()
            ec2.terminate_instances(InstanceIds=instances)
        else:
            ec2.terminate_instances(InstanceIds=ids.split(','))
    except Exception as e:
        raise


if __name__ == '__main__':
    args = sys.argv
    globals()[args[1]](*args[2:])
