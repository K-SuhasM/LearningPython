Tasks = []
done = []

print("\n Enter your choice:\n \n 1. Add task. \n 2. View tasks. \n 3. Mark as complete a task. \n 4. Remove a task. \n 5. Cancel. \n")

choice = int(input())

if choice not in (1,2,3,4,5): raise ValueError("Please choose from the options.")

if choice==1:
    while True:
        t = input("Enter task to add, enter 'done' after done: \n    ")
        Tasks.append(t)
        if t.lower() == "done":
            break   
    print("\n Your updated To-Do list is: \n")
    for i in Tasks:
        print(i)

if choice==2:
    for i in Tasks:
        print(i) 
    for i in done:
        print(i) 
        

if choice==3:
    mark = int(input("Which task to mark as done? \n"))
    for i in Tasks:
        i = 1
        print(i) 
    done.append(Tasks[mark])
     
if choice==4:
    rem = int(input("Which task to remove? \n"))
    for i in Tasks:
            i = 1
            print(i) 
    Tasks.remove(rem)

if choice==5:
    print("Exited...")
