while True:
    num=input("Enter your numbers: ")
    numb=[]
    for i in num:
        i=int(i)
        numb.append(i)
    print(sum(numb))