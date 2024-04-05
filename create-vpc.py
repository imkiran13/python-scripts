import boto3

# Create an EC2 client 
client = boto3.client('ec2')

# Create an EC2 resource
resource = boto3.resource('ec2')

# Create a new VPC
new_vpc = resource.create_vpc(
    CidrBlock='10.0.0.0/16'
)

# Create a subnet within the VPC
subnet1 = new_vpc.create_subnet(
    CidrBlock='10.0.1.0/24'
)

# Create another subnet within the VPC
subnet2 = new_vpc.create_subnet(
    CidrBlock='10.0.2.0/24'
)

# Apply tags to the VPC
new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        },
        # You can add more tags if needed
    ]
)
