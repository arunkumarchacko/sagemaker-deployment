import json
import boto3


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    print("Received" + str(body))


    runtime = boto3.Session().client('sagemaker-runtime')

    print('Calling sagemaker with {}'.format(event['body']))

    # Now we use the SageMaker runtime to invoke our endpoint, sending the review we were given
    response = runtime.invoke_endpoint(EndpointName = 'sagemaker-pytorch-2020-08-05-06-53-11-030',    # The name of the endpoint we created
                                       ContentType = 'text/plain',                 # The data format that is expected
                                       Body = event['body'])                       # The actual review

    # print("Response is " + str(response['Body']))
    # The response is an HTTP response whose body contains the result of our inference
    result = response['Body'].read().decode('utf-8')

    print('Result is {}'.format(result))
    return {
        'statusCode' : 200,
        'headers' : { 'Content-Type' : 'text/plain', 'Access-Control-Allow-Origin' : '*' },
        'body' : result
    }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    #     # headers: {'Access-Control-Allow-Origin': '*','Access-Control-Allow-Credentials': 'true'}
    # }

    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
