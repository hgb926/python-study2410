def add(x,y):
    return x+y

def sub(a,b):
    return a-b

number1=[1,2,3,4]
number2=[5,6,3,4,5,]
result1=map(add,number1,number2)
result2=map(sub,number2,number1)
print(list(result1))
print(list(result2))