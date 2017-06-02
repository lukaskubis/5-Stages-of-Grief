# 5 Stages of Grief (notes)
Notes from my lecture on python functions for [engeto.cz](https://engeto.cz).

### Chapters:
- [Denial](https://github.com/lukaskubis/5-Stages-of-Grief#1denial)
- [Anger](https://github.com/lukaskubis/5-Stages-of-Grief#2anger)
- [Bargaining](https://github.com/lukaskubis/5-Stages-of-Grief#3bargaining)
- [Depression](https://github.com/lukaskubis/5-Stages-of-Grief#4depression)
- [Acceptance](https://github.com/lukaskubis/5-Stages-of-Grief#5acceptance)


These 5 stages are used as a narrative medium through which we showcase various implementations of abstract constructs using functions only. It was inspired by [this video](https://www.youtube.com/watch?v=o9pEzgHorH0) on how to stop writing classes. What can we accomplish if we omit class definitions altogether and use only functions?

### [Slides](https://github.com/lukaskubis/5-Stages-of-Grief/tree/master/slides.pdf)

***Note: these are only complementary to spoken word, don't expect any source of wisdom of any kind.***

---
## 1.Denial
We start off by denying the existence of custom types. The exercise here is to create a simple customisable logger, which works as follows:
We set up our loggers for each log type
```python
>>> log = logger('LOG')
>>> warning = logger('WARNING')
>>> error = logger('ERROR')
```
Then we call our loggers to log our messages
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

### Code: [`denial.py`](https://github.com/lukaskubis/5-Stages-of-Grief/blob/master/code/denial.py)
---
## 2.Anger
As we get annoyed by the fact that `lambda` functions can only consist of one expression, we move on to closures to extend the functionality. We hit a point where using a `nonlocal` statement we're able to change an inner state pf our closure each time we call. We define a simple incrementing counter based on this idea.
```python
>>> c = counter()
>>> c()
1
>>> c()
2
>>> c()
3
>>> # ...
```
**Task 1**: Extend `logger` functionality so that it also logs in file by defining new `log_me` function.
```python
system_log = lambda log: log_me('filename', log)
system_log(warning('Careful!'))
```

**Task 2**: Extend `counter` functionality to a calculator-like device evaluating numerical operations.
```python
>>> c = calculator()
>>> c()
0
>>> c('3+3')
6
>>> c('-7')
-1
>>> c('*7')
-7
>>> # ...
```
### Code: [`anger.py`](https://github.com/lukaskubis/5-Stages-of-Grief/blob/master/code/anger.py)
---
## 3.Bargaining
We're now trying to se whether we can access values stored inside a closure without calling it (some sort of higher power indeed). We decide to try and define a function which takes our closure as argument and inspects its nonlocal variables. This is now a mild introduction to the idea of decorators.

**Task 1**: Define a closure, which references multiple nonlocal values and returns `None`. To see the values, call the `inspect` function with your closure as argument to print the nonlocal values.

```python
>>> c = my_closure(a=3, b=7)
>>> c(a=8, b=10) # this is the way my closure changes its nonlocals
>>> inspect(c)
[8, 10]
>>>
```

**Task 2**: Decorate the closure with `inspect_decorator` in its definition to invoke the `inspector` upon every function call.

```python
>>> c = my_closure(a=3, b=7)
>>> c(a=8, b=10)
[8, 10]
>>>
```
### Code: [`bargaining.py`](https://github.com/lukaskubis/5-Stages-of-Grief/blob/master/code/bargaining.py)
---
## 4.Depression
We become depressed as our numbers cannot be iterated through, even though they come in a controlled sequence. We therefore decide to create a generator, which will provide an interface between us and values popping out of our device. This way, we can have a controller, which prompts us for next operation and yields the result. Because the generator function returns an iterator, we can semantically write
```python
>>> c = controller(device)
>>> for result in c:
...     # do whatever with each result
```
The code will iterate over sequence of values yielded from our generator even though at the time of execution, `c` is not populated by any values. Magic of generators.

**Taks**: Define a generator function, a manager, which will iterate through results from our device after explicitly initialized, like so:
```python
>>> # initialize
... results = manager(controller(device))
>>>
>>> # do whatever in between
...
>>> # start iteration
... next(results)
<prompt>:
...
```
### Code: [`depression.py`](https://github.com/lukaskubis/5-Stages-of-Grief/blob/master/code/depression.py)
---

## 5.Acceptance
... will come as soon as you get used to these kinds of things.
