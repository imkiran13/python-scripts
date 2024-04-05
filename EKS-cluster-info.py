import boto3


# Create an EKS client
client = boto3.client('eks',region_name="ap-south-1")

# Retrieve information about EKS clusters
clusters = client.list_clusters()

for cluster in clusters:
    response = client.describe_cluster(
    name='cluster'
)
    
    cluster_info=response['cluster']
    cluster_status=cluster_info['status']
    cluster_endpoint=cluster_info['endpoint']
    cluster_version=cluster_info['version']
    
    print(f"cluster {cluster} status is {cluster_status} ")
    print(f"cluster endpoint is: {cluster_endpoint} ")
    print(f"cluster  version is: {cluster_version} ")