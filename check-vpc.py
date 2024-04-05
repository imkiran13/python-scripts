import boto3

# Create an EC2 client we can change deafult region
client = boto3.client('ec2',region_name="us-east-1")

# Describe all available VPCs
all_available_vpcs = client.describe_vpcs()

# Extract VPCs from the response
vpcs = all_available_vpcs["Vpcs"]

# Iterate over each VPC
for vpc in vpcs:
    # Print the VPC ID
    print(vpc["VpcId"])
    
    # Check if the "CidrBlockAssociationSet" key exists and retrieve its value
    cidr_block_asso_sets = vpc.get("CidrBlockAssociationSet", [])
    
    # Iterate over each association set in the VPC
    for asso_set in cidr_block_asso_sets:
        print(asso_set)
        cidr_state=asso_set["CidrBlockState"]
        print(cidr_state)
