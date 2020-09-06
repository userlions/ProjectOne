"""
    Program for calculating factorial of a number.
"""
#   Date of creation:11-July-2020
#   Author: Prabhu Prasad Behera.

class CalculateFactorial:

    def factorial(num):
        if num!=0:
            res=num*CalculateFactorial.factorial(num-1);
            return res;
        return 0;
    print (CalculateFactorial.factorial(5));
   # def factorial(n):
   #     if n == 1:
   #         return 1;
   #     else:
   #         return n * CalculateFactorial.factorial(n-1)
