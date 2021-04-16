def lambda_handler(event, context):
    for key, value in event.items():
        print("Hello World from 2nd File{}".format(value))
    return "Success-2"
