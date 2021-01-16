from turtle import *

logo1 = [
    (-165, -15), (-165, 0), (-165, 15), (-165, 30), (-165, 45),
    (-150, -45), (-150, -30), (-150, -15), (-150, 0), (-150, 15), (-150, 30), (-150, 45), (-150, 60), (-150, 75),
    (-135, -60), (-135, -45), (-135, -30), (-135, -15), (-135, 0), (-135, 15), (-135, 30), (-135, 45), (-135, 60),
    (-135, 75), (-135, 90),
    (-120, -60), (-120, -45), (-120, -30), (-120, -15), (-120, 0), (-120, 15), (-120, 30), (-120, 45), (-120, 60),
    (-120, 75), (-120, 90),
    (-105, -60), (-105, -45), (-105, -30), (-105, -15), (-105, 0), (-105, 15), (-105, 30), (-105, 45), (-105, 60),
    (-105, 75), (-105, 90),
    (-90, 0), (-90, 15), (-90, 30), (-90, 45), (-90, 60), (-90, 75), (-90, 90), (-90, 120), (-90, 135),
    (-75, 15), (-75, 30), (-75, 45), (-75, 60), (-75, 75), (-75, 90), (-75, 120), (-75, 135), (-75, 150),
    (-60, 15), (-60, 30), (-60, 45), (-60, 60), (-60, 75), (-60, 90), (-60, 120), (-60, 150),
    (-45, 15), (-45, 30), (-45, 45), (-45, 60), (-45, 75), (-45, 90), (-45, 120), (-45, 135), (-45, 150), (-45, 165),
    (-30, 15), (-30, 30), (-30, 45), (-30, 60), (-30, 75), (-30, 90), (-30, 120), (-30, 135), (-30, 150), (-30, 165),
    (-15, 15), (-15, 30), (-15, 45), (-15, 60), (-15, 75), (-15, 90), (-15, 105), (-15, 120), (-15, 135), (-15, 150),
    (-15, 165),
    (0, 15), (0, 30), (0, 45), (0, 60), (0, 75), (0, 90), (0, 105), (0, 120), (0, 135), (0, 150), (0, 165),
    (15, 15), (15, 30), (15, 45), (15, 60), (15, 75), (15, 90), (15, 105), (15, 120), (15, 135), (15, 150), (15, 165),
    (30, 15), (30, 30), (30, 45), (30, 60), (30, 75), (30, 90), (30, 105), (30, 120), (30, 135), (30, 150), (30, 165),
    (45, 15), (45, 30), (45, 45), (45, 60), (45, 75), (45, 90), (45, 105), (45, 120), (45, 135), (45, 150),
    (60, 15), (60, 30), (60, 45), (60, 60), (60, 75), (60, 90), (60, 105), (60, 120), (60, 135), (60, 150),
    (75, 30), (75, 45), (75, 60), (75, 75), (75, 90), (75, 105), (75, 120), (75, 135),
]
logo2 = [
    (-75, -135), (-75, -120), (-75, -105), (-75, -90), (-75, -75), (-75, -60), (-75, -45), (-75, -30),
    (-60, -150), (-60, -135), (-60, -120), (-60, -105), (-60, -90), (-60, -75), (-60, -60), (-60, -45), (-60, -30),
    (-60, -15),
    (-45, -150), (-45, -135), (-45, -120), (-45, -105), (-45, -90), (-45, -75), (-45, -60), (-45, -45), (-45, -30),
    (-45, -15),
    (-30, -165), (-30, -150), (-30, -135), (-30, -120), (-30, -105), (-30, -90), (-30, -75), (-30, -60), (-30, -45),
    (-30, -30), (-30, -15),
    (-15, -165), (-15, -150), (-15, -135), (-15, -120), (-15, -105), (-15, -90), (-15, -75), (-15, -60), (-15, -45),
    (-15, -30), (-15, -15),
    (0, -165), (0, -150), (0, -135), (0, -120), (0, -105), (0, -90), (0, -75), (0, -60), (0, -45), (0, -30), (0, -15),
    (15, -165), (15, -150), (15, -135), (15, -120), (15, -105), (15, -90), (15, -75), (15, -60), (15, -45), (15, -30),
    (15, -15),
    (30, -165), (30, -150), (30, -135), (30, -120), (30, -90), (30, -75), (30, -60), (30, -45), (30, -30), (30, -15),
    (45, -165), (45, -150), (45, -135), (45, -120), (45, -90), (45, -75), (45, -60), (45, -45), (45, -30), (45, -15),
    (60, -150), (60, -120), (60, -90), (60, -75), (60, -60), (60, -45), (60, -30), (60, -15),
    (75, -150), (75, -135), (75, -120), (75, -90), (75, -75), (75, -60), (75, -45), (75, -30), (75, -15),
    (90, -135), (90, -120), (90, -90), (90, -75), (90, -60), (90, -45), (90, -30), (90, -15), (90, 0),
    (105, -90), (105, -75), (105, -60), (105, -45), (105, -30), (105, -15), (105, 0), (105, 15), (105, 30), (105, 45),
    (105, 60), (105, 75),
    (120, -90), (120, -75), (120, -60), (120, -45), (120, -30), (120, -15), (120, 0), (120, 15), (120, 30), (120, 45),
    (120, 60), (120, 75),
    (135, -90), (135, -75), (135, -60), (135, -45), (135, -30), (135, -15), (135, 0), (135, 15), (135, 30), (135, 45),
    (135, 60), (135, 75),
    (150, -75), (150, -60), (150, -45), (150, -30), (150, -15), (150, 0), (150, 15), (150, 30), (150, 45), (150, 60),
    (165, -45), (165, -30), (165, -15), (165, 0), (165, 15), (165, 30),
]

t = Turtle()

t.shape("classic")
bgcolor("black")

t.pensize()
t.penup()
t.speed(4000)


def square():
    t.pendown()
    for i in range(4):
        t.forward(15)
        t.left(90)

    t.penup()


for x in range(len(logo1)):
    t.color("#4584b6")
    t.goto(logo1[x])
    square()

for x in range(len(logo2)):
    t.color("#ffde57")
    t.goto(logo2[x])
    square()

t.begin_fill()
t.goto(-60, 135)
t.color("#4584b6")
square()
t.end_fill()

t.begin_fill()
t.goto(60, -135)
t.color("#ffde57")
square()
t.end_fill()

# write "Python" under logo

t.goto(-60, -220)
test = ("L1pixel", "31")
t.color("white")
# noinspection PyTypeChecker
t.write("Python", font=test)

done()
