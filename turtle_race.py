import turtle
import random

def random_num(outcomes):
    num = random.choice(outcomes)
    return num

def finish_line(racer1_pos, racer2_pos):
    finish = 300.00
    pos1, pos2 = racer1_pos[0], racer2_pos[0]
    if pos1 >= finish:
        return 1
    elif pos2 >= finish:
        return 1
    else:
        return 0

def getpos(racer1, racer2):
    return (racer1.pos(), racer2.pos())

def main():

    pos1, pos2 = turtle1.pos(), turtle2.pos()
    print(pos1, pos2)
    line = finish_line(pos1, pos2)
    while line != 1:
        f1, f2 = random_num(die), random_num(die)
        print(f1, f2)
        turtle1.forward(f1)
        turtle2.forward(f2)
        line = finish_line(turtle1.pos(), turtle2.pos())
        print(line)

    p1, p2 = getpos(turtle1, turtle2)

    winner = max(p1, p2)
    if p1 == winner:
        print("racer 1 won")
        return ""
    else:
        print("racer 2 won")
        return ""




if __name__ == "__main__":
    screen = turtle.Screen()
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle1.shape("turtle")
    turtle2.shape("turtle")
    turtle1.fillcolor("red")
    turtle2.fillcolor("green")


    turtle1.penup()
    turtle1.goto(-300, 0)
    turtle1.pendown()
    turtle2.penup()
    turtle2.goto(-300, 100)
    turtle2.pendown()

    die = [1,2,3,4,5,6]

    main()
    screen.exitonclick()
