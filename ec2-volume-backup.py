import boto3
import schedule
import time

# Initialize an EC2 client
client = boto3.client('ec2')

# Define a function to create snapshots of volumes tagged with 'prod' or 'stag'
def backup_volumes():
    # Describe volumes based on specified filters
    volumes = client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod', 'stag']
            },
        ],
    )
    # Iterate through each volume
    for volume in volumes['Volumes']:
        # Create a new snapshot for the volume
        new_snapshot = client.create_snapshot(
            VolumeId=volume['VolumeId'],
        )
        # Print information about the new snapshot
        print(new_snapshot)
        # Add a delay of 10 seconds between each snapshot creation
        time.sleep(10)

# Schedule the backup_volumes function to run every day 
schedule.every(10).seconds.do(backup_volumes)

# Continuously check for scheduled tasks and run them
while True:
    schedule.run_pending()
