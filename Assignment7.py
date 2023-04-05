k =[]
l=int(input("write the no of strings u want to  add"))
for s in range (l):
    k.append(input("Enter the strings"))
res = [s[::-1] for s in k]
print(res)