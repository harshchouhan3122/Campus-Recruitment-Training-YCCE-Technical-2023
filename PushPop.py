CAPACITY = 10

def pop():
    print("Pop Function Called.")
    
def peek():
    print("Peek Function Called.")
    
def display():
    print("Display Function Called.")

def push():
        # print("Push Function Called.")
        ele = input("Enter the Element : ")
        if (top==CAPACITY-1):
            return 1
        else:
            return 0

        

print("\n Menu Driven Program!")

while(1):
    choise = int(input("\n 1.Push() \n 2.Pop() \n 3.Peek() \n 4.Display \n 5.Exit \n\n"))

    if choise==5:
        print("Thank You! \n")
        break

    elif choise==1:
        push()

    elif choise==2:
        pop()

    elif choise==3:
        peek()

    elif choise==4:
        display()

