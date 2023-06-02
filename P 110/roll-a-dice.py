import random
responce="y"

while responce=="y":
    no=random.randint(1,3)

    if no==1:
      print(".....")
      print("__1__")
      print(".....")

    if no==2:
      print(".....")
      print("__2__")
      print(".....")

    if no==3:
       print(".....")
       print("__3__")
       print(".....")



responce=input('press y to roll again & n to close')
print("/n")
