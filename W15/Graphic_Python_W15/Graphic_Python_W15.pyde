balloons = []

class Balloon(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def show(self):
        stroke(40)
        strokeWeight(2)
        line(self.x, self.y, self.x, self.y + 100)
        fill(100, 180, 240)
        ellipse(self.x, self.y, self.r, self.r)

    def move(self):
        self.y = self.y - 3
        if self.y < -self.r - 100:
            self.y = height + 50

def setup():
    size(600, 600)
    
    # Initialize 5 balloons using a loop
    for i in range(5):
        rx = int(random(80, 520))
        ry = int(random(400, 650))
        rr = int(random(40, 70))
        balloons.append(Balloon(rx, ry, rr))

def draw():
    background(240)
    
    for b in balloons:
        b.show()
        b.move()
