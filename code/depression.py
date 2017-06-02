# depression.py


# this is our device that produces new value every function call
def calculator():
    value = 0
    def calculate(expr=''):
        nonlocal value
        if not expr:
            return value
        if not expr[0].isdigit():
            expr = str(value) + expr
        value = eval(expr)
        return value
    return calculate


# provides an interface to the device
# creates an iterator, which yields results from device
def controller(device):
    d = device()
    try:
        while(1):
            command = input('~ ')
            yield d(command)
    except KeyboardInterrupt:
        print('(end)')
