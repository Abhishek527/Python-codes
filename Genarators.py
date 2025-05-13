def disp():
    print("start")
    yield 10
    print("mid")
    print("mid")
    yield 20
    print("end")
    yield 30

res = disp()
print(res)
print(res.__next__())    
print(res.__next__()) 
print(res.__next__()) 
print(res.__next__()) 