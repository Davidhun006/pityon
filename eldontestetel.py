# 1
# t=[2,5,6,9,10,12,4]
# # print(f'az 5nél nagyobb számok:{count}')
# print("eldöntés - True/False")
# n=len(t)
# ker=5
# i=0
# while i<n and t[i]!=ker:
#     i=i+1
# if i<n:
#     print("Van ilyen",ker)
# else:
#     print("Nincs ilyen", ker)
# 2
# wr=open('eldöntes.txt','w')
# t=[2,5,6,9,10,12,4]
# wr.write("t=[2,5,6,9,10,12,4]")
# n=len(t)
# wr.write(f'{n}')
# ker=5
# wr.write("A keresett szám:{ker}")
# i=0
# while i<n and t[i]!=ker:
#     i=i+1
# if i<n:
#     print("Van ilyen",ker)
#     wr.write(f'Van ilyen')
# else:
#     print("nincs ilyen ",ker)
#     wr.write(f'nincs ilyen')
# wr.close()
# 3
# print("kiválasztás")
# n=len(t)
# ker=5
# i=0
# while t[i]!=ker:
#     i=i+1
# print('ezen a helyen találhato',i+1)
# 4
# print('eldöntés (van-nincs)',kiválsztás tétel (hely megadás)
# t=[2,5,6,9,10,12,4]
# n=len(t)
# print(n)
# ker=5
# i=0
# while i<n and t[i]!=ker:
#     i=i+1
#     if (i<n):
#         print(f'van {ker} elem a listában')
#         print(f'helye {i+1}')
#     else:
#         print(f'nincs {ker} elem a listában')
# 5
# t=[2,5,6,9,10,12,4]
# maxElem=t[0]
# for elem in t:
#     if elem>maxElem:
#         maxElem=elem
# print(maxElem)

# # 6
# minElem=t[0]
# for elem in t:
#     if elem<minElem:
#         minElem=elem
# print(minElem)

# print(f'egyszerű számtani átlag: {(minElem+maxElem)/2}')
# 7
# wr=open('max.txt','w')
# t=[2,4,7,1,8,5,9]
# wr.write(f't=[2,4,7,1,8,5,9]\n')
# maxElem=t[0]
# for elem in t:
#     if elem>maxElem:
#         maxElem=elem
# print(f'{maxElem}\n')
# wr.write(f'{maxElem}\n')
# wr.close
# # 8
# wr=open('min.txt','w')
# t=[2,4,7,1,8,5,9]
# wr.write(f't=[2,4,7,1,8,5,9]\n')
# minElem=t[0]
# for elem in t:
#     if elem<minElem:
#         minElem=elem
# print(f'{minElem}\n')
# wr.write(f'{minElem}\n')
# wr.close
# t=[2,4,7,1,8,5,9]
# b=[]
# c=[]
# d=[]
# def dupla(num):
#     return num*2
# 9
# for elem in t:
#     b.append(dupla(elem))
#     if elem%2==0:
#         c.append(elem)
#     if elem<5:
#         d.append(elem)
# print(b)
# print(c)
# print(d)

# print('kiválogatás')
# 10
# t=[2,4,7,1,8,5,9]
# n=len(t)
# for i in range(n-1,0,-1):
#     for j in range(0,i):
#         if(t[j]>t[j+1]):
#             tmp=t[j+1]
#             t[j+1]=t[j]
#             t[j]=tmp
# print(t)

with open ("10E.txt",'w',encoding="utf-8")as file:
    file.write("csordasne kovacs judit")

wr=open('10e2.txt',"w")
wr.write("csordasne kovacs judit")
wr.close()