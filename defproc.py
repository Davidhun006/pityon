# def proc():
#     global a
#     a=5
#     print(b)
#     print(c)
# b=0
# c=4
# proc()
# print(a)

def proc(x):
    x+=1
    print(x)

proc(3)
a=10
proc(a)
print(a)