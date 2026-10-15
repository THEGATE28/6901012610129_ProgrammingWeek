data_values = []

def setup():
    # Set canvas size
    size(600, 450)
    
    # Create sample data file if not present
    with open("chart_data.txt", "w") as f:
        f.write("45\n80\n60\n95\n30\n70\n")
    
    # Read numbers line-by-line from file into a list
    global data_values
    with open("chart_data.txt", "r") as f:
        for line in f:
            clean_str = line.strip()
            if clean_str.isdigit():
                data_values.append(int(clean_str))

def draw():
    # Clear screen each frame
    background(245)
    
    # Draw title and instructions
    fill(40)
    textSize(18)
    text("File Data Visualization (Bar Chart)", 40, 40)
    
    # Draw bars and data labels based on loaded file content
    bar_width = 50
    spacing = 30
    start_x = 60
    base_y = 350
    
    i = 0
    while i < len(data_values):
        val = data_values[i]
        x = start_x + (i * (bar_width + spacing))
        bar_height = val * 2.5
        y = base_y - bar_height
        
        # Draw bar
        fill(70, 130, 220)
        rect(x, y, bar_width, bar_height)
        
        # Display value label on top of each bar
        fill(20)
        textSize(14)
        text(str(val), x + 15, y - 10)
        
        i = i + 1
        
    # Baseline line
    stroke(100)
    line(40, base_y, 560, base_y)
    
    # Interactive string display following mouse cursor
    noStroke()
    fill(200, 50, 50)
    textSize(16)
    info_text = "Mouse: (" + str(mouseX) + ", " + str(mouseY) + ")"
    text(info_text, mouseX, mouseY - 15)
