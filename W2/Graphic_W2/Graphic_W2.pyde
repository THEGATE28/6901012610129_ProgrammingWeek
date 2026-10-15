# Initial balloon position
x = 100

def setup():
    # Set window size (called once)
    size(500, 500)

# User-defined function to draw a balloon at (x, y)
def draw_balloon(x, y):
    ellipse(x, y, 100, 100)           # Balloon body
    line(x, y + 50, x, y + 200)       # Balloon string

def draw():
    # Called repeatedly for animation
    global x
    
    # Clear background to prevent trailing
    background(220)
    
    # Draw balloon moving horizontally and following mouse Y
    draw_balloon(x, mouseY)
    
    # Move balloon to the right
    x = x + 5
    
    # Reset position when balloon leaves the screen
    if x > width + 50:
        x = -50
