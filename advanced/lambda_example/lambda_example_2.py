# Lambda functions can have 0 or 1 expression, not more.

# No expression : contains no expression, will give the same output for all arguments.
from typing import Callable, Any, Union

x: Callable[[], str] = lambda: "Hello World"
print('Variable Type:', x)
print('Lambda no argument Value:', x())

# Single expression: They can contain either one expression or no expression. We cannot put more than one expression
# in a lambda function.


lambda_single: Callable[[Any], Union[int, Any]] = lambda x: (x % 2)
print('Lambda single argument Value:', lambda_single(10))
