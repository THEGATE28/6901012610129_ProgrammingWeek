# Array to store balloon objects
balloons = []

class Balloon:
    def __init__(self, x, y, r):
        # Assign attributes from parameters
        self.x = x
        self.y = y
        self.r = r

    def show(self):
        # Render balloon string and body
        stroke(60)
        strokeWeight(2)
        line(self.x, self.y, self.x, self.y + 100)
        fill(255, 120, 80)
        ellipse(self.x, self.y, self.r, self.r)

    def move(self):
        # Float upwards with acceleration near the top
        if self.y > height / 2:
            self.y = self.y - 2
        else:
            self.y = self.y - 4
            
        # Reset position when off-screen
        if self.y < -self.r:
            self.y = height + 100

def setup():
    # Set canvas window dimensions
    size(600, 600)
    
    # Initialize array of objects using coordinate lists
    x_positions = [150, 300, 450]
    y_positions = [520, 580, 540]
    
    i = 0
    while i < len(x_positions):
        balloons.append(Balloon(x_positions[i], y_positions[i], 60))
        i = i + 1

def draw():
    # Refresh screen
    background(240, 245, 250)
    
    # Loop through array of objects and invoke methods
    i = 0
    while i < len(balloons):
        balloons[i].show()
        balloons[i].move()
        i = i + 1
