import boto3

ec2_client_mumbai = boto3.client('ec2', region_name="ap-south-1")
ec2_resource_mumbai = boto3.resource('ec2', region_name="ap-south-1")

ec2_client_virginia = boto3.client('ec2', region_name="us-east-1")
ec2_resource_virginia = boto3.resource('ec2', region_name="us-east-1")

instance_id_mumbai = []
instance_id_virginia = []

reservations_mumbai = ec2_client_mumbai.describe_instances()["Reservations"]
for reservation in reservations_mumbai:
    instances = reservation['Instances']
    for instance in instances:
        instance_id_mumbai.append(instance['InstanceId'])

response = ec2_resource_mumbai.create_tags(
    DryRun=False,  # Set to True if you want to perform a dry run
    Resources=instance_id_mumbai,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)



reservations_virginia = ec2_client_virginia.describe_instances()["Reservations"]
for reservation in reservations_virginia:
    instances = reservation['Instances']
    for instance in instances:
        instance_id_virginia.append(instance['InstanceId'])

response = ec2_resource_virginia.create_tags(
    DryRun=False,  # Set to True if you want to perform a dry run
    Resources=instance_id_virginia,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
