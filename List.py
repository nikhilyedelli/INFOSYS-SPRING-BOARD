a=[1,2,3,4,5]
for a in a:
    print(a)
    
a=["a","b","c"]
b=' '.join(a)
print(b)
a=[1,2,3,4,5]
b=sum(a)
print(b)
a=[1,2,3,4,5]
b=max(a)
print(b)

a=["a","b","c"]
a_to_find="s"
if a_to_find in a:
    print("found")
else:
    print("not found")
import turtle
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("rabbit")    # alex looks like a turtle

alex.color("green")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,4):
    alex.circle(20*counter)

alex.color("red")
alex.left(120)
alex.circle(50)
for cntr in range(1,4):
    alex.circle(20*cntr)

alex.color("blue")
alex.right(240)
alex.circle(50)
for c in range(1,4):
    alex.circle(20*c)