import boto3

client = boto3.client('ecs')
ssm    = boto3.client('ssm')


def create_service():
    response = ssm.get_parameters(
            Names=[
                'COMPONENT',
            ],
            WithDecryption=False
        )
    for name in response['Parameters'][0]['Value'].split(','):
        response = client.create_service(
            cluster='vls-demo-fargate',
            serviceName=name,
            taskDefinition=name,
            
            desiredCount=1,
            launchType='FARGATE',
            
            platformVersion='1.4.0',
            
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': [
                        'subnet-0d5ea679e732e4b50',
                    ],
                    'assignPublicIp': 'DISABLED'
                }
            },
            tags=[
                {
                    'key': 'env',
                    'value': 'dev'
                },
            ]
        )