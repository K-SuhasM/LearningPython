# # import threading
# # import time

# # def makepizza():
# #     print("Putting in the oven")
# #     time.sleep(2)
# #     print("Pizza done")
# # def makepizza2():
# #     print("Putting in the oven second")
# #     time.sleep(2)
# #     print("Pizza done sec")
# # def makepizza3():
# #     print("Putting in the oven thi")
# #     time.sleep(2)
# #     print("Pizza done thi")

# # # makepizza()

# # t1=threading.Thread(target=makepizza)
# # t2=threading.Thread(target=makepizza2)
# # t3=threading.Thread(target=makepizza3)

# # t1.start()
# # t2.start()
# # t3.start()

# # t1.join()
# # t2.join()
# # t3.join()

# # print("Waiting")

# # import threading
# # import time

# # def download():
# #     print("Downloading...")
# #     time.sleep(3)
# #     print("Done")

# # t1 = threading.Thread(target=download)
# # t2 = threading.Thread(target=download)

# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()

# # import asyncio
# # async def task():
# #     print("Start")
# #     await asyncio.sleep(2)
# #     print("End")
# # asyncio.run(task())


# # import time
# # def task():
# #     print("start")
# #     time.sleep(2)
# #     print("end")
# # task()

# # import asyncio
# # async def task1():
# #     print("Task 1 started")
# #     await asyncio.sleep(10)
# #     print("Task 1 finished")

# # async def task2():
# #     print("Task 2 started")
# #     await asyncio.sleep(5)
# #     print("Task 2 finished")

# # async def main():
# #     await asyncio.gather(
# #         task1(),
# #         task2()
# #     )
# # asyncio.run(main())

# from multiprocessing import Process
# import time

# def task(n):
#     print(f"Task {n} started")
#     time.sleep(5)
#     print(f"Task {n} Finished")
# if __name__ == '__main__':
#     p1= Process(target=task, args=[1])
#     p2= Process(target=task, args=[2])

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

