from turtle import Turtle

class Stick(Turtle):
    def __init__(self,x,y) :
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()
        self.goto(x,y)
    

    

    def go_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
     