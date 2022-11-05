import boto3

client = boto3.client('sns')
response = client.add_permission(
    TopicArn='string',
    Label='string',
    AWSAccountId=[
        'string',
    ],
    ActionName=[
        'string',
    ]
)