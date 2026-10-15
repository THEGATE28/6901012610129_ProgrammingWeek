# Array to store multiple polymorphic objects
balloons = []

# Base Class: standard floating balloon
class Balloon(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def show(self):
        # Draw balloon string and body
        stroke(50)
        strokeWeight(2)
        line(self.x, self.y, self.x, self.y + 100)
        fill(255, 100, 100)
        ellipse(self.x, self.y, self.r, self.r)

    def move(self):
        # Float upwards
        if self.y > height / 2:
            self.y = self.y - 2
        else:
            self.y = self.y - 4
            
        # Reset position when off-screen
        if self.y < -self.r - 100:
            self.y = height + 50

# Subclass: balloon with expanding and shrinking behavior
class EsBalloon(Balloon):
    def __init__(self, x, y, r):
        # Call superclass constructor with Jython/Processing syntax
        super(EsBalloon, self).__init__(x, y, r)
        self.change = 1

    def expand_shrink(self):
        # Oscillate balloon radius between 30 and 70
        self.r = self.r + self.change
        if self.r >= 70:
            self.change = -1
        elif self.r <= 30:
            self.change = 1

    def show(self):
        # Distinct color for pulsating balloon
        stroke(50)
        strokeWeight(2)
        line(self.x, self.y, self.x, self.y + 100)
        fill(80, 200, 220)
        ellipse(self.x, self.y, self.r, self.r)

    # Method Overriding: include both upward movement and pulsing animation
    def move(self):
        super(EsBalloon, self).move()
        self.expand_shrink()

def setup():
    size(600, 600)
    
    # Instantiate mixed objects into the same array
    balloons.append(Balloon(150, 500, 50))
    balloons.append(EsBalloon(300, 550, 45))
    balloons.append(Balloon(450, 520, 50))

def draw():
    background(245)
    
    # Polymorphic call: same method names behave differently per instance
    i = 0
    while i < len(balloons):
        balloons[i].show()
        balloons[i].move()
        i = i + 1
