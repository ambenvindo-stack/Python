import turtle

emo = turtle.Turtle()


# to make center of circle -- face of emoji

emo.up()
emo.goto(0,-100)
emo.down()

# fill the yellow color in the circle

emo.begin_fill()
emo.pendown()  # it is used to fill the pixel basically it trace the points like circle over here
emo.fillcolor('yellow') # as all emoji are mostly yellow color so we will also fill as yellow color
emo.circle(100)
emo.end_fill()

#semicircle smile in emoji

emo.up()
emo.goto(-67,-40)
emo.setheading(-60)
emo.width(5)
emo.down()
emo.circle(80,120)
emo.fillcolor("black")  # black color for smile


# to make eyes
for i in range(-35, 105, 70):
    emo.up()
    emo.goto(i, 35)
    emo.setheading(0)
    emo.down()
    emo.begin_fill()
    emo.circle(10)
    emo.end_fill()
emo.penup()  # we will take pen as up so after it goes to end point it will not affect our smiley
emo.goto(0, -150)  # minus is for downside and positive is for upside -- here we will send cursor to bottom
# we will not use hide turtle because it wil destroy screen as soon as it will complete it drawing part
# to reamin screen on we will use mainloop

turtle.mainloop()