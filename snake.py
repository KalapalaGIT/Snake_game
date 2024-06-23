from turtle import Turtle
START_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
         self.Segments = []
         self.Create_snake()
         self.head=self.Segments[0]

    def Create_snake(self):
        for position in START_POSITIONS:
            self.Add_segment(position)

    def Add_segment(self,position):
            new_segment=Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.Segments.append(new_segment)

    def Extend(self):
        self.Add_segment(self.Segments[-1].position())

    def Reset(self):
         for seg in self.Segments:
              seg.goto(1000,1000)
         self.Segments.clear()
         self.Create_snake()
         self.head=self.Segments[0]
        

    def Move(self):    
        for seg_num in range(len(self.Segments)-1,0,-1):
                new_y=self.Segments[seg_num-1].ycor()
                new_x=self.Segments[seg_num-1].xcor()
                self.Segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
         if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
