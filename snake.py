from turtle import Turtle

start = [(0, 0), (-20, 0), (-40, 0)]
d = 20
up = 90
left = 180
down = 270
right = 0

class Snake:
    def __init__(self):
        self.segs = []
        self.create()
        self.head = self.segs[0]
        
    def create(self):
        for pos in start:
            self.add_seg(pos)
            
    def add_seg(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        self.segs.append(seg)
        seg.goto(position)
        
    def reset(self):
        for seg in self.segs:
            seg.goto(1000, 1000)
        self.segs.clear()
        self.create()
        self.head = self.segs[0]
            
    def extend(self):
        self.add_seg(self.segs[-1].position())
    
    def move(self):
        for i in range(len(self.segs) - 1, 0, -1):
            new_x = self.segs[i - 1].xcor()
            new_y = self.segs[i - 1].ycor()
            self.segs[i].goto(new_x, new_y)
        self.segs[0].forward(d)
        
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
        
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)