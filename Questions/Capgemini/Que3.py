# (IMPORTANT)

'''
Capgemini in its online written test has a coding question, wherein the students are given a 
string with multiple characters that are repeated consecutively. You’re supposed to reduce the 
size of this string using mathematical logic given as in the example below:
Input :
aabbbbeeeeffggg
Output:
a2b4e4f2g3
Input :
abbccccc
Output:
ab2c5
'''

'''
inpList = list(input())
uniqueElement = list(set(inpList))
uniqueElement.sort()
# print(inpList)
# print(uniqueElement)

outList = []
for i in uniqueElement:
    outList.append(i)
    count = inpList.count(str(i))
    if count == 1:
        continue
    else:
        outList.append(str(count))

# print(outList)
print("".join(outList))
'''


input_string = input()

if (input_string == ""):
    compresses_string = ""
else:
    compresses_string = ""
    current_char = input_string[0]
    count = 1
    for i in range(1,len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            if count>1:
                compresses_string += ((current_char) + str(count))
            else:
                compresses_string += current_char

            current_char = input_string[i]
            count = 1
    
    # for the last caracter if block of for loop is executed but else is not
    # executed at the end because after the end of string it does'nt get the character to compare
    if count>1:
        compresses_string += ((current_char) + str(count))
    else:
        compresses_string += current_char

    print(compresses_string)





























