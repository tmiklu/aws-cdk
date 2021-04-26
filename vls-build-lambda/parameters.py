import boto3

client = boto3.client('ssm')

def put_platform(platform):
    response = client.put_parameter(
        Name='PLATFORM',
        Description='aws compute platform',
        Value=platform,
        Type='String',
        Overwrite=True
    )
    return response


def put_component(components):
    response = client.put_parameter(
        Name='COMPONENT',
        Description='List of component releases',
        Value=components,
        Type='StringList',
        Overwrite=True,
    )