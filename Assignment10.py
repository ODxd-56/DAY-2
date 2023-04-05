l=[]
c=[]
r=int(input("write the no  u want to  add : "))
for a in range(r):
    l.append(int(input("write the no's : ")))
for a in  l:
    if a % 2==0:
        c.append(a)
print(c)