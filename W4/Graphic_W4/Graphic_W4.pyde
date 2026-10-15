def setup():
    # Setup canvas size and animation speed
    size(500, 500)
    frameRate(4)

# Helper function to draw a circle using radius
def draw_circle(x, y, r):
    ellipse(x, y, r * 2, r * 2)

# Function to draw vertical fence lines using a while loop
def draw_vertical_lines(x1, y1, x2, y2):
    space = abs(x1 - x2) / 6
    curr_x = x1
    while curr_x <= x2:
        line(curr_x, y1 - 40, curr_x, y1 + 40)
        curr_x = curr_x + space

# Function to draw n random raindrops using a while loop
def draw_rain_drops(n):
    i = 0
    while i < n:
        rx = random(50, 450)
        ry = random(50, 300)
        r = random(3, 15)
        fill(70, 130, 240, 150)
        noStroke()
        draw_circle(rx, ry, r)
        i = i + 1

def draw():
    # Clear screen each frame
    background(230)
    
    # Draw raindrops using fixed loop iterations
    draw_rain_drops(20)
    
    # Draw fence structure at the bottom
    stroke(80)
    strokeWeight(2)
    draw_vertical_lines(50, 400, 450, 400)
    line(40, 400, 460, 400)
