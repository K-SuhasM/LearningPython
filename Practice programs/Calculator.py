while True:
    def add(x,y):
        print(x+y)

    def sub(x,y):
        print(x-y)

    def mul(x,y):
        print(x*y)

    def div(x,y):
        print(x/y)
    
    print("\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Quit ")
    choice = int(input("Enter your choice:  "))
    if choice not in (1,2,3,4,5):
        raise ValueError("Please choose from the values.")

    else:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        if choice == 1:
            add(x,y)
        if choice == 2:
            sub(x,y)
        if choice == 3:
            mul(x,y)
        if choice == 4:
            div(x,y)
        if choice == 5:
            break


