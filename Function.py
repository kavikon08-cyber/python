def factorial(num):
    if num == 0:
        return 1
    else:
        z=num * factorial(num-1)
        return z
a=factorial(90)
print("factorial Ans is:",a)

def total(a,*b):
    c=0
    for d in b:
        c+=d
    print(a+c)
total(5,6,7,8,9,23,12,34)

def collage(**kwargs):
    print(kwargs)
collage(name="VVIT",address="DHARMPURI")    
