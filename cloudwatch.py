import boto3
import time


client = boto3.client('logs')

LOG_GROUP='cloudwatch_customlog'
LOG_STREAM='{}-{}'.format(time.strftime('%Y-%m-%d'),'logstream')

try:
   client.create_log_group(logGroupName=LOG_GROUP)
except client.exceptions.ResourceAlreadyExistsException:
   pass

try:
   client.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)
except client.exceptions.ResourceAlreadyExistsException:
   pass

response = client.describe_log_streams(
   logGroupName=LOG_GROUP,
   logStreamNamePrefix=LOG_STREAM
)

event_log = {
   'logGroupName': 'ProgramaticLog',
   'logStreamName': 'TestStream',
   'logEvents': [
       {
           'timestamp': int(round(time.time() * 1000)),
           'message': time.strftime('%Y-%m-%d %H:%M:%S')+'\t Your custom log messages'
       }
   ],
}

if 'uploadSequenceToken' in response['logStreams'][0]:
   event_log.update({'sequenceToken': response['logStreams'][0] ['uploadSequenceToken']})

response = client.put_log_events(**event_log)
print(response)