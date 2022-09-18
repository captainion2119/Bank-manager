stk = []
choice = "y"

while choice == "y":
    print("Stack operations")
    print("1. Push")
    print("2. Pop")
    print("3. Display stack")
    print("4. Exit")
    ch = int(input("Enter the operation number (1-4): "))
    if ch == 1:
        ap = int(input("Enter element to push to stack: "))
        stk.append(ap)
        print("Success...")
    if ch == 2:
        if stk == []:
            print("Error empty stack... Underflow case...")
        else:
            print("Item popped from stack: ", stk.pop())
    if ch == 3:
        top = len(stk)-1
        print(top)
        for a in range(top-1,-1,-1):
            print(a)
    if ch == 4:
        break
    choice = input("Do you wish to continue? y/n: ")
    