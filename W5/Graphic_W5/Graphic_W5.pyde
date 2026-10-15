# Number of particles
n = 35

# Parallel lists for coordinates and fall speed
x = []
y = []
s = []

def setup():
    # Set canvas dimensions
    size(600, 500)
    
    # Initialize lists using a while loop and append()
    i = 0
    while i < n:
        x.append(random(20, width - 20))
        y.append(random(0, height))
        s.append(random(2, 6))
        i = i + 1

def draw_circle(cx, cy, r):
    # Custom circle drawing function
    ellipse(cx, cy, r * 2, r * 2)

def draw():
    # Refresh background
    background(30, 35, 45)
    
    i = 0
    while i < n:
        # Draw particle
        noStroke()
        fill(180, 215, 255, 200)
        draw_circle(x[i], y[i], 5)
        
        # Update vertical position by its own speed
        y[i] = y[i] + s[i]
        
        # Reset position to top when falling past screen boundary
        if y[i] > height:
            y[i] = 0
            x[i] = random(20, width - 20)
            
        i = i + 1
