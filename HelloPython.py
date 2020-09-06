print("Hello");
x='true';
if (x=='false'):
    print ('Testing conditional statements.');
elif (x=='true'):
    print ('Testing reached else');
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print (factorial(5));

def factorial(num):
    if num!=0:
        res=num*factorial(num-1);
        return res;
    return 1;
print (factorial(5));