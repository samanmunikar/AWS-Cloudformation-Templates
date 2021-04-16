def lambda_handler(event, context):
    for key, value in event.items():
        print("Hello World from 1st file {}".format(value))
    return "Success-1"
