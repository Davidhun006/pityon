with open("10ef.txt","w",encoding="utf-8" ) as file:
    file.write("Csordásné Kovács Judit")

wr=open('10e2f.txt',"w")
wr.write("Csordásné Kovács Judit")
wr.close()

re=open('10e2f.txt',"r")
line=re.readline()
print(line)
re.close() 


re=open('10e2f.txt',"r")
line=re.readline()
while line !="":
    line=line.strip()
    print(line)
    line=re.readline()
re.close()