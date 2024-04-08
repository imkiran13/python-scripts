import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Define the instance IDs of the development servers
dev_server_instance_ids = ['instance_id_1', 'instance_id_2']  # Add your instance IDs here

def start_dev_servers():
    # Start the development servers
    ec2.start_instances(InstanceIds=dev_server_instance_ids)
    print("Development servers started.")

def stop_dev_servers():
    # Stop the development servers
    ec2.stop_instances(InstanceIds=dev_server_instance_ids)
    print("Development servers stopped.")

if __name__ == "__main__":
    choice = input("Enter 'start' to start dev servers or 'stop' to stop dev servers: ").strip().lower()
    if choice == 'start':
        start_dev_servers()
    elif choice == 'stop':
        stop_dev_servers()
    else:
        print("Invalid choice. Please enter 'start' or 'stop'.")
