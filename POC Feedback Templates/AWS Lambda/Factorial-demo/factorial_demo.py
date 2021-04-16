import calculateFactorial as Factorial

def lambda_handler(event, context):
    ls = list()
    for value in event.values():
        fact = Factorial.Nfactorial(int(value))
        print("Factorial of {} is {}".format(value, fact))
        ls.append(fact)
    return ls
