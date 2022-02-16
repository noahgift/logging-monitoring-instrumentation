import json
import boto3

# Create CloudWatchEvents client
cloudwatch_events = boto3.client('events')

# Put an event
response = cloudwatch_events.put_events(
    Entries=[
        {
            'Detail': json.dumps({'key1': 'value1', 'key2': 'value2'}),
            'DetailType': 'appRequestSubmitted',
            'Resources': [
                'RESOURCE_ARN',
            ],
            'Source': 'com.company.myapp'
        }
    ]
)
print(response['Entries'])