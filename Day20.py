# def my_generator ():
#     for i in range(10):
#         yield i

# gen=my_generator()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# for p in gen:
#     print(p)
# import time
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def funs(n):
#     time.sleep(2)
#     return n*5


# print(funs(5))
# print("after 2 seconds")
# print(funs(10))
# print("after 2 seconds")
# print(funs(15))

# print(funs(5))
# print("after 2 seconds")
# print(funs(10))
# print("after 2 seconds")
# print(funs(15))


import re

pattern="recovery"
text='''Download Lineage Recovery. Simply download the latest recovery file, named boot.img.
warning
Important: Other recoveries may not work for installation or updates. We strongly recommend to use the one linked above!
Flash recovery onto your device:
fastboot flash boot boot.img
Now reboot into recovery to verify the installation.
Use the menu to navigate to and to select the Recovery option.
info_outline
Note: Please note that on most devices youll need to use the Volume Buttons to cycle onscreen options and the Power Button to select (Mobile), or by short pressing the Side Button to cycle onscreen options and by long pressing the Side Button to select (Android TV).
info_outline
Note: If your recovery does not show the LineageOS logo  , you accidentally booted into the wrong recovery. Please start at the top of this section!
'''

x=re.finditer(pattern, text)
for i in x:
    print(i) 