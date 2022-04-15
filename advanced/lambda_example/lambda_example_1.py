# Calculate squares using lambda
from typing import Callable, Any

squares: Callable[[Any], Any] = lambda x: x * x
print('Using lambda: ', squares(5))

(lambda x: print('Using print within lambda: ', x * x))(6)
