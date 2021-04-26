import boto3

client = boto3.client('ecs')

def create_fargate():
    
    # check if cluster exists
    response         = client.list_clusters()
    get_cluster_name = response['clusterArns']
    
    for cluster in get_cluster_name:
        if cluster.split('/')[1] == 'vls-demo-fargate':
            raise RuntimeError('cluster exist')

    print('Creating cluster vls-demo-fargate')
    response = client.create_cluster(
        clusterName='vls-demo-fargate',
            tags=[
                {
                    'key': 'env',
                    'value': 'prod'
                },
            ],
            
            configuration={
                'executeCommandConfiguration': {
                    'logging': 'OVERRIDE',
                    'logConfiguration': {
                        'cloudWatchLogGroupName': 'ECS-FARGATE-LOG',
                        'cloudWatchEncryptionEnabled': False,
                        's3BucketName': 'string',
                        's3EncryptionEnabled': False,
                        's3KeyPrefix': 'fargate-'
                    }
                }
            },
            capacityProviders=[
                'FARGATE',
            ],
            defaultCapacityProviderStrategy=[
                {
                    'capacityProvider': 'FARGATE',
                    'weight': 0,
                    'base': 0
                },
            ]
        )
    return response