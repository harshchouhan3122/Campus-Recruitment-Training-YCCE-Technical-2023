string = input("String : ")
list1 = []
list1.append(string[0])
last = string[0]
count = 0
for i in string:
    if i==last:
        count+=1
    else:
        list1.append(str(count))
        last = i
        list1.append(last)
        count = 1
list1.append(str(count))
print("".join(list1))