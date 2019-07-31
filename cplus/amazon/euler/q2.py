def fib(n):
    f1, f2 = 1, 2 
    yield f1  

    while f2 < n: 
        yield f2 
        f1, f2 = f2, f1+f2 

for i in fib(20): 
    if i % 2: 
        print(i) 

result = 0 
for i in fib(4000000): 
    if i % 2 == 0: 
        result += i 
print("result is ", result) 


