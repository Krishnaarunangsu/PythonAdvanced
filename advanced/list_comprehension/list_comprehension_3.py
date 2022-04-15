# The list comprehensions are more efficient both computationally and in terms of coding space and time than a for
# loop. Typically, they are written in a single line of code. The below program depicts the difference between for
# loops and list comprehension based on performance.

# Import required module

import time


# define function to implement for loop
def for_loop(n: int):
    result = []
    for i in range(n):
        result.append(i ** 2)

    return result


# define function to implement list comprehension
def limit_comprehension(n: int):
    result = [i ** 2 for i in range(n)]
    return result


# Driver Code

# Calculate time taken by for loop
begin = time.time()
for_loop(10 ** 6)
end = time.time()

# Display time taken by for loop
print("Time taken by for-loop:", round(end - begin, 2))

# Calculate time taken by list comprehension
begin = time.time()
limit_comprehension(10 ** 6)
end = time.time()

# Display time taken by for loop
print("Time taken by list comprehension:", round(end - begin, 2))
