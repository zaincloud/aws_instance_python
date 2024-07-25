# EC2 Instance Creation Script

This Python script uses Boto3 to create EC2 instances on AWS. It allows you to specify instance type, image ID, security group, and other parameters.

## Prerequisites
- AWS credentials (access key and secret key)
- Python installed
- Boto3 library installed (`pip install boto3`)

## Usage
1. Replace the placeholders in the script (e.g., `access_key`, `secret_key`, etc.) with your actual credentials.
2. Run the script.
3. Instances will be launched, tagged, and their public IP addresses retrieved.

## Configuration
- `instance_type`: The EC2 instance type (e.g., t2.micro).
- `image_id`: The AMI ID for the desired image.
- `region`: The AWS region (e.g., us-east-1).
- `security_group`: The security group ID.
- `key_name`: The key pair name.
- `num_instances`: Number of instances to create.




