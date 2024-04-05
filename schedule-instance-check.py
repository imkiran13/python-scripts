import boto3
import schedule
def check_instance_health():
    # Create an EC2 client
    client = boto3.client('ec2')

    # Describe instance status
    response = client.describe_instance_status()

    # Extract instance status information
    instance_statuses = response.get('InstanceStatuses', [])

    # Check instance health
    for instance_status in instance_statuses:
        instance_id = instance_status['InstanceId']
        state = instance_status['InstanceState']['Name']
        status = instance_status['InstanceStatus']['Status']
        system_status = instance_status['SystemStatus']['Status']

        print(f"Instance ID: {instance_id}")
        print(f"State: {state}")
        print(f"Instance Status: {status}")
        print(f"System Status: {system_status}")
        print()



if __name__ == "__main__":
    check_instance_health()
    
schedule.every(1).minutes.do(check_instance_health)

while True:
      schedule.run_pending()