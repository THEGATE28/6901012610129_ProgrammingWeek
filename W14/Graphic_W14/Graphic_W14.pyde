# Dataset points with an outlier (x, y)
data_x = [4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]
data_y = [5.3, 5.7, 6.1, 6.4, 6.8, 7.1,  7.5,  7.8,  8.2, 12.8,  8.8]

def setup():
    # Setup canvas dimensions
    size(650, 480)

def draw():
    background(250)
    
    # Title and descriptions
    fill(40)
    textSize(16)
    text("Anscombe's Style Dataset & Outlier Visualization", 40, 40)
    
    # Draw axes
    stroke(150)
    strokeWeight(1.5)
    line(60, 420, 600, 420)  # X-axis
    line(60, 420, 60, 80)    # Y-axis
    
    # Draw linear regression trend line (y = 0.50x + 3.00)
    stroke(220, 60, 60)
    strokeWeight(2)
    # Map coordinates to screen space
    x_start = 60 + (2.0 * 35)
    y_start = 420 - ((0.5 * 2.0 + 3.0) * 25)
    x_end = 60 + (15.0 * 35)
    y_end = 420 - ((0.5 * 15.0 + 3.0) * 25)
    line(x_start, y_start, x_end, y_end)
    
    # Plot data points
    i = 0
    while i < len(data_x):
        px = 60 + (data_x[i] * 35)
        py = 420 - (data_y[i] * 25)
        
        # Check if the point is an outlier
        if data_y[i] > 10.0:
            fill(230, 50, 50)
            stroke(180, 0, 0)
            ellipse(px, py, 14, 14)
            
            # Label the outlier
            fill(200, 20, 20)
            textSize(12)
            text("Outlier (13.0, 12.8)", px + 10, py - 5)
        else:
            fill(70, 130, 220)
            stroke(30, 70, 150)
            ellipse(px, py, 10, 10)
            
        i = i + 1
