import boto3  # Importing the boto3 library for AWS interactions
from operator import itemgetter

# Creating an EC2 client
client = boto3.client('ec2')

# Describe volumes with the tag 'prod'
volumes = client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['prod']
        },
    ],
)

# Iterate through each volume
for volume in volumes['Volumes']:
    # Describe snapshots for the volume
    snapshots = client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]
            },
        ]
    )

    # Sort snapshots by start time in descending order
    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)
    
    # Keep the two most recent snapshots and delete the rest
    for snap in sorted_by_date[2:]:
        # Delete snapshot
        response = client.delete_snapshot(
            SnapshotId=snap['SnapshotId'],
        )
        # Print response
        print(response)
