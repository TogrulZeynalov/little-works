import turtle
n = input().split(' ')
s = ['1','2','3','4','5','6','7','8','9']
r = 0
for i in n:
    if s.count(i) != 0:
        r = i
if n.count('square') != 0:
    turtle.forward(r)
    turtle.right(90)
    turtle.forward(r)
    turtle.right(90)
    turtle.forward(r)
    turtle.right(90)
    turtle.forward(r)
    turtle.right(90)
    
