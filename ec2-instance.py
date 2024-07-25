import boto3

# Configure AWS credentials (replace with your actual keys)
access_key = "" #aws access key
secret_key = "" #aws secret key
 
# Desired configuration (replace with your desired values)
instance_type = "t2.micro"
image_id = "ami-0a0e5d9c7acc336f1"
region = "us-east-1"
security_group = "sg-038aaa893cd9676ef"
key_name = "cloud"
num_instances = int(input("Enter the Number of Instance to Create: "))

# Create EC2 client
ec2_client = boto3.client("ec2", aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)

# Launch instances
response = ec2_client.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=[security_group],
    MinCount=num_instances,
    MaxCount=num_instances
)

# Extract instance IDs
instance_ids = [instance['InstanceId'] for instance in response['Instances']]

# Tag instances with names
for i, instance_id in enumerate(instance_ids, start=1):
    ec2_client.create_tags(
        Resources=[instance_id],
        Tags=[{'Key': 'Name', 'Value': f'MyInstance-{i}'}]
    )

# Wait for instances to be in running state
ec2_client.get_waiter('instance_running').wait(InstanceIds=instance_ids)

# Retrieve public IP addresses and names
instances = ec2_client.describe_instances(InstanceIds=instance_ids)
instance_details = []
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        name = next(tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name')
        instance_details.append({
            "Name": name,
            "PublicIpAddress": instance.get('PublicIpAddress')
        })

# Print the details
print(f"Instance details:\n{instance_details}")
