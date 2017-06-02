# denial.py

from datetime import datetime

time = datetime.now
logform = '[{}], {}: {}'


logger = lambda logtype: lambda msg: print(logform.format(time(), logtype, msg))


# def logger(logtype):
#     return lambda msg: print(logform.format(time(), logtype, msg))


# def logger(logtype):
#     def print_log(msg):
#         return print(logform.format(time(), logtype, msg))
#     return print_log
