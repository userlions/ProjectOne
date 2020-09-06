# Author : Prabhu Prasad Behera
# Date : 05-Sep-2020

# Variable declaration style 1: No data type with data
a = None
print(a)

# Variable declaration style 2:
# Question: How come int is accepting string data?
# In Python it accepts any type of datatypes but shows warning as it is showing currently in Problems pane.
a: int = "String appended"
print(a)

if None:
    print("None means true")
else:
    print("Hey, None means false")

# Demonstration of boolean data
b: bool = True
c: bool = "Hello I am a string and going into boolean varialbe with warning"

# Note: keywords in python are case sensitive so True works and true fails

