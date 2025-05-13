def disp():
    yield 10
    yield 20
    yield 30

res = disp()
print(res)
print(res.__next__())    
print(res.__next__()) 
print(res.__next__()) 
print(res.__next__()) 