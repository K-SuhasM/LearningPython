
# p= open("text.txt", "w")
# p.write("Hello hello hello hello") 

# p.truncate(5)

# p.close()


# with open("text.txt", "r") as f:
#     # f.seek(4)
#     # print(f.tell())
#     c= f.read()
#     print(c)

# sum= lambda x,y: x+y
# avg = lambda x,y,z,p : x+y+z+p / 4


# def sumo(f,val):
#     return (f(val)+6)


# sum= lambda x: x*x*x*x*x*x*x*x
# print(sumo(sum,2))
# print(sum("hel","loo"))


# l= [1, 2, 3, 4, 5]
# # lc=[]
# # for i in l:
# #     lc.append(i**3) 
# lc = list(map(l**3))
# print(lc)

def cube(x):
    return x>0

l=[1,2,3,4,5]

nl= list(filter(cube,l))
print(nl)