# def border():
#     print()
#     for i in range(80):
#         print("-",sep=" ",end=' ')
#     print('\n')

# print('1feladat')
# border()
# print('3feladat')
# border()
# print('4feladat')
# border()
# print('6feladat')
# border()
def border(n,s):
    print()
    for i in range(n):
        print(s,sep=" ",end=' ')
    print('\n')
border(80,"*")
print('1feladat')
print('a)feladat')
border(10,"-")
print("b)feladat")
border(80,"*")
print("2.feladat")