# 5 Stages of Grief (notes)
Notes from my lecture on python functions for [engeto.cz](http://engeto.cz).

The 5 stages are used as a narrative medium through which we showcase various implementations of abstract constructs using functions only.

### 1.Denial
We start off by denying the existence of custom types. The goal gere is to create a customisable logger, which works as follows:

1.We set up our loggers for each log type
```python
>>> log = logger('LOG')
>>> warning = logger('WARNING')
>>> error = logger('ERROR')
```

2.Then we call our loggers to log our messages
```python
>>> log('something happened')
>>> warning('careful!')
>>> error('oops')
```
Expected example output:
```
[2017-05-30 20:54:53.812624] LOG: something happened
[2017-05-30 20:55:30.898678] WARNING: careful
[2017-05-30 20:56:32.687967] ERROR: oops
```
Code:
[denial.py](https://github.com/lukaskubis/5-Stages-of-Grief/blob/master/code/denial.py)

### 2.Anger
### 3.Bargaining
### 4.Depression
### 5.Acceptance
