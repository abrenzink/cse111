import random

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_oval, draw_rectangle, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    min_diam = 2
    max_diam = 7

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_background(canvas, scene_width, scene_height,
    min_diam, max_diam)

    #Drawing buildings
    draw_buildings(canvas, scene_width)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_background(canvas, w, h, min, max):
    """Draw the sky and all the objects in the sky."""
    draw_sky(canvas, w, h)
    draw_clouds(canvas, w, h)
    draw_stars(canvas, w, h, min, max)
    draw_moon(canvas)
 
def draw_sky(canvas, w, h):
    """Draw the sky"""
    draw_rectangle(canvas, 0, 0, w, h, width=0, fill="slateBlue1")
    draw_rectangle(canvas, 0, 0, w, 3*h/4, width=0, fill="slateBlue2")
    draw_rectangle(canvas, 0, 0, w, h/2, width=0, fill="slateBlue3")
    draw_rectangle(canvas, 0, 0, w, h/4, width=0, fill="slateBlue4")

def draw_stars(canvas, w, h, min, max):
    for i in range(200):
        x = random.randint(0, w)
        y = random.randint(0, h)
        diameter = random.randint(min, max)
        draw_oval(canvas, x, y, x + diameter, y + diameter,width=0, fill="white")

def draw_moon(canvas):
    draw_oval(canvas, 570, 310, 690, 430, width=0, fill="white")
    draw_oval(canvas, 570, 310, 690, 430, width=0, fill="white")

def draw_buildings(canvas, w):
    for i in range(0, w, 25):
        x = random.randint(40, 250)
        draw_rectangle(canvas, i, 0, i+24, x, width=0, fill="black")
        for j in range(0, x, 25):
            draw_rectangle(canvas, i+24, 0, i+19, x, width=0, fill="white")
            draw_rectangle(canvas, i, x-5, i+20, x, width=0, fill="white")
            
def draw_clouds(canvas, w, h):
    for i in range(100):
        x = random.randint(0, w)
        y = random.randint(h/4, h)
        diameter = random.randint(50,100)
        draw_oval(canvas, x, y, x + diameter, y + diameter, width=0,
                fill="mediumPurple1")

# Call the main function so that
# this program will start executing.
main()