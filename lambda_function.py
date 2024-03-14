import boto3
import requests
import pandas as pd

sns_client = boto3.client('sns')
sns_arn = "arn:aws:sns:us-east-1:471112663332:cicd-trigger-notification"

def lambda_handler(event, context):
    
    print("Event Data -> ", event)
    response = requests.get("https://www.google.com/")
    print(response.text)

    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)

    message = "Lambda function triggered via CICD"
    response = sns_client.publish(
        Subject="SUCCESS- Lambda CICD pipeline", 
        TargetArn=sns_arn, 
        Message=message, 
        MessageStructure='text'
    )

    print(df)
    print('Demo Completed !!!')