import boto3
import sys

key_pair_name = 'ec2'


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


def createKeyPair():
    ec2 = boto3.resource('ec2')
    key = ec2.create_key_pair(KeyName=key_pair_name)
    with open('./key.pem', 'w') as file:
        file.write(key.key_material)
    print(key.key_fingerprint)


def createEC2(number):
    ec2 = boto3.resource('ec2')
    try:
        print(f'creating {number} instances... \n')
        ec2.create_instances(
            ImageId="ami-053b0d53c279acc90",
            MinCount=1,
            MaxCount=int(number),
            InstanceType="t2.micro",
            KeyName=key_pair_name,
            SecurityGroupIds=['sg-0dd85863e893a17d1']
        )
    except Exception as e:
        raise
    print("new instance(s) id(s): \n")
    print(describeEC2s())


# running only
def describeEC2s():

    running_instances= []
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if instance['State']['Name'] != 'terminated':
                x = (instance["InstanceId"])
                # print(x)
                running_instances.append(x)
    return running_instances


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
