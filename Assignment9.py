k =[]
l=int(input("write the no of strings u want to  add"))
for s in range (l):
    k.append(input("Enter the strings"))
check = 'A'
print("Given list : ", k)
res= [i for i in k if i.lower().startswith(check.lower())]
print("List elements starting with matching letter : A ", res)