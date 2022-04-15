# Lambda functions can be Immediately Invoked You can implement a lambda function without using a variable name. You
# can also directly pass the argument values into the lambda function right after defining it using parenthesis. This
# cannot be done using def functions.


(lambda x, y, z: print("Multiplied Value:", x*y*z))(5, 6, 7)
# https://www.machinelearningplus.com/python/lambda-function/