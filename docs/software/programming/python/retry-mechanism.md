---
published: true
---
# Retry mechanism
If your code depends on external factors (e.g. the availability of web services or the network connection) you may want to retry in case of failures.

> [!info] Title
> The code on this page uses the following demo scenario: A list of numbers is iterated and used as denominators. If the number is 0 (and a `ZeroDivisionError` is raised) the code retries up to three times (in reality you would try to fix the root cause).

## For loop

```python
import time
attempts_max = 3
wait_between = 2.0
denominator = [1, 2, 0, 3]
for d in denominator:
    for _ in range(attempts_max):
        try:
            # Execute logic
            print(f'1/{d} = {1 / d}')
        except ZeroDivisionError:
            # Logic failed (take neccesary steps before retry)
            time.sleep(wait_between)
            print('retry')
        else:
            # Logic successful
            break
    else:
        # Max. number of attempts failed
        raise RuntimeError('max number of attempts failed')
```

## While loop

```python
attempts_max = 3
denominator = [1, 2, 0, 3]
def retry_while_loop():
i = 0
attempt_count = 0
while i < len(denominator):
    d = denominator[i]
    try:
        # Execute logic
        print(f'1/{d} = {1 / d}')
    except ZeroDivisionError:
        if attempt_count >= attempts_max:
            # Max. number of attempts failed
            raise RuntimeError('max number of attempts failed')
        attempt_count += 1
        # Logic failed (take neccesary steps before retry)
        time.sleep(wait_between)
        print('retry')
        continue
    i += 1
```

## Wrapper function

```python
import functools
import time

def retry(num_tries: int, wait_between: float):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            for _ in range(num_tries-1):
                try:
                    return func(*args, **kwargs, retry_error=RetryError)
                except ZeroDivisionError:
                    # Logic failed (take neccesary steps before retry)
                    time.sleep(wait_between)
            # Last try.
            return func(*args, **kwargs)
        return wrapper_retry
    return decorator_retry

@retry(num_tries=3, wait_between=2.0)
def retry_decorated():
    denominator = [1, 2, 0, 3]
    for d in denominator:
        print(f'1/{d} = {1 / d}')
```