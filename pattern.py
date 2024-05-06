
shape = input("Enter a shape right triangle, left triangle or diamond: ")

def right_triangle():
    i = 0
    while i < 4:
        j = 0
        while j <= i:
            print ("#",end="")
            j = j+1
        i = i+1
        print()


def left_triangle():
    i = 0
    while i < 4:
        j = 4
        while j >= i:
          if j != i:
             print(" ",end="")
             j = j-1
          else:
             n = 0
             while n <= i:
              print("#",end="")
              n = n+1
             j = j-1
        i = i+1
        print()


def diamond ():
   for i in range(1,5):
      print (" " * (4-i) + "*" * i + "*" * i )

   for i in range (4,0,-1):
      print (" " * (4-i) + "*" * i + "*" * i)


if shape.lower() == "right triangle" :
    right_triangle()

if shape.lower() == "left triangle" :
    left_triangle()

if shape.lower() == "diamond" :
    diamond()