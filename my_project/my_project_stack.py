from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_codebuild as cb
)


class MyProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        #workload_vpc = ec2.Vpc(
        #    self, 'demo',
        #    cidr = '10.0.0.0/16'
        #)

        #cluster = ecs.Cluster(
        #    self, 'Cluster',
        #    cluster_name = 'vls-demo-cluster',
        #    vpc = 'worload_vpc'
        #)

        my_lambda = _lambda.Function(
            self, 'vls-build',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('vls-build-lambda'),
            function_name='vls-build',
            handler='lambda_function.handler',
            timeout=core.Duration.seconds(15),
            environment = {
                'JIRA': 'https://jira.dtvlaops.net/rest/api/2/issue/',
                'ROLE_ARN': 'arn:aws:iam::028960685088:role/service-role/AWSCodePipelineServiceRole-us-east-1-',
                'SECRET': 'c2EtamlyYS1jaWNkOmRLTVo5YmF6'
            }
        )

        apigw.LambdaRestApi(
            self, 'vls-trigger-jira-build-API',
            handler=my_lambda,
        )

        #codebuild = cb.Project(
        #
        #)
