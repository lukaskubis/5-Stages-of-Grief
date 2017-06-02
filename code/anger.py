# anger.py

def counter():
    value = 0
    def count():
        nonlocal value
        value += 1
        return value
    return count
