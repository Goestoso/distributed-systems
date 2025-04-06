
global x
x=0

def fun1():
   global x
   for i in range(5000):
     for j in range(10000):
        x=x+1

def fun2():
   global x
   for i in range(5000):
     for j in range(10000):
        x=x+1

fun1()
fun2()
print(x)


