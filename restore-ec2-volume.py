import boto3
from operator import itemgetter

# Create an EC2 client
client = boto3.client('ec2')

# Create an EC2 resource
resource = boto3.resource('ec2')

# Instance ID
instance_id = 'i-07c29077d84d8070a'

# Describe volumes attached to the instance
volumes = client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        },
    ]
)

# Get the volume attached to the instance
instance_volume = volumes['Volumes'][0]

# Describe snapshots for the volume
snapshots = client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        },
    ]
)

# Sort snapshots by start time in descending order to get the latest snapshot
latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]

# Print the start time of the latest snapshot
print(latest_snapshot['StartTime'])

# Create a new volume from the latest snapshot
new_volume = client.create_volume(
    SnapshotId=latest_snapshot['SnapshotId'],
    AvailabilityZone='ap-south-1a',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                },
            ]
        },
    ],
)

# Wait until the new volume is available
while True:
    vol = resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    if vol.state == 'available':
        # Attach the new volume to the instance
        resource.Instance(instance_id).attach_volume(
            Device='/dev/xvdb',
            VolumeId=new_volume['VolumeId']
        )
        break
