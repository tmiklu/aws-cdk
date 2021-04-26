import boto3

client = boto3.client('ecs')
ssm    = boto3.client('ssm')

def create_task():
    response = ssm.get_parameters(
            Names=[
                'COMPONENT',
            ],
            WithDecryption=False
        )
    for name in response['Parameters'][0]['Value'].split(','):
        response = client.register_task_definition(
            family=name,
            taskRoleArn='arn:aws:iam::028960685088:role/ecsTaskExecutionRole',
            executionRoleArn='arn:aws:iam::028960685088:role/ecsTaskExecutionRole',
            networkMode='awsvpc',
            containerDefinitions=[
                {
                    'name': 'vls-dev',
                    'image': '028960685088.dkr.ecr.us-east-1.amazonaws.com/vls-repository:openjdk11-base',
                    'cpu': 256,
                    'memory': 512,
                    'memoryReservation': 256,
                    'portMappings': [
                        {
                            'containerPort': 8081,
                            'hostPort': 8081,
                            'protocol': 'tcp'
                        },
                    ],
                    'essential': True,
                    'startTimeout': 10,
                    'stopTimeout': 10,
                    'user': '1001:1001',
                    'workingDirectory': '/home',
                    'disableNetworking': False,
                    'privileged': False,
                    'readonlyRootFilesystem': False,
        
                    'interactive': False,
                    'pseudoTerminal': False,
        
                },
            ],
        
            requiresCompatibilities=[
                'FARGATE',
            ],
            cpu='256',
            memory='512',
            tags=[
                {
                    'key': 'env',
                    'value': 'dev'
                },
            ],
        )