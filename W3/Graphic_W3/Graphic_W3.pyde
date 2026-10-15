# Initial balloon position
balloon_x = 250
balloon_y = 200

def setup():
    # Setup window size and background
    size(500, 500)

# Helper function to draw circle from center with radius r
def draw_circle(x, y, r):
    ellipse(x, y, r * 2, r * 2)

# User-defined function for drawing a balloon
def draw_balloon(x, y, radius):
    draw_circle(x, y, radius)
    line(x, y + radius, x, y + radius * 3)

# Function to calculate Euclidean distance between two points
def cal_distance(x1, y1, x2, y2):
    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)
    result = sqrt(diff_x * diff_x + diff_y * diff_y)
    return result

def draw():
    # Clear screen each frame
    background(220)
    
    # Draw balloon at base coordinate
    draw_balloon(balloon_x, balloon_y, 40)
    
    # Calculate distance from balloon center to current mouse position
    d = cal_distance(balloon_x, balloon_y, mouseX, mouseY)
    
    # Draw distance guide line on the side matching mouse position
    if mouseX > balloon_x:
        line(balloon_x, balloon_y, balloon_x + d, balloon_y)
    else:
        line(balloon_x, balloon_y, balloon_x - d, balloon_y)
