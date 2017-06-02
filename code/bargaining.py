# bargaining.py

def inspect(func):
    # generate list of all nonlocal variables inside closure
    vals = [c.cell_contents for c in func.__closure__]

    # print the values
    print(vals)


def inspect_decorator(func):
    def print_values(*args, **kwargs):
        # print current values
        inspect(func)

        # do whatever the function does
        # this should update the values
        result = func(*args, **kwargs)

        # print its updated values
        inspect(func)

        # return whatever the function returns
        return result
    return print_values
