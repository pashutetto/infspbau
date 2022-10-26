import turtle as t

def draw_fractal(sz):
    if sz>=30:
##        t.right(60)
##        t.forward(sz/2.0)
##        draw_fractal(sz/2.0)
##        t.forward(sz/2.0)
##        t.right(120)
##        t.forward(sz)
##        t.right(120)
##        t.forward(sz)
##        t.right(60)
        t.right(60)
        t.forward(sz/2.0)
        draw_fractal(sz/2.0)
        t.right(120)
        t.forward(sz/2.0)
        draw_fractal(sz/2.0)
        t.right(120)
        t.forward(sz/2.0)
        draw_fractal(sz/2.0)
        

scale=900
t.speed(0)
t.tracer(0, 0)
t.pensize(1)
t.penup()
t.color('purple')
t.goto(0,300)
t.pendown()
draw_fractal(scale)
t.update()
t.done()

   
