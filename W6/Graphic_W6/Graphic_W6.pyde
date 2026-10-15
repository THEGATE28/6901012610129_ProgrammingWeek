message = "KMUTNB"

def setup():
    # Set canvas dimensions
    size(600, 400)
    textAlign(CENTER, CENTER)

def draw():
    # Refresh background each frame
    background(240)
    
    # Draw interactive floating text following mouse coordinates
    fill(40, 80, 180)
    textSize(54)
    text(message, mouseX, mouseY)
    
    # Display individual characters and their ASCII codes at the bottom
    fill(60)
    textSize(16)
    i = 0
    while i < len(message):
        ch = message[i]
        code = ord(ch)
        info = str(i) + ": " + ch + " (" + str(code) + ")"
        text(info, 70 + (i * 90), 360)
        i = i + 1
