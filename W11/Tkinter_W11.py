import tkinter as tk

# คลาสลูกโป่งเชิงวัตถุสำหรับ Tkinter
class Balloon:
    def __init__(self, canvas, x, y, radius, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = radius
        self.color = color
        
        # วาดตัวลูกโป่งและสายเชือกบน Canvas
        self.oval_id = self.canvas.create_oval(
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r,
            fill=self.color, outline="black", width=2
        )
        self.line_id = self.canvas.create_line(
            self.x, self.y + self.r,
            self.x, self.y + self.r + 90,
            fill="black", width=2
        )

    # เมทอดควบคุมการเคลื่อนที่ขึ้นด้านบน
    def move(self, speed=3):
        self.y = self.y - speed
        self.canvas.move(self.oval_id, 0, -speed)
        self.canvas.move(self.line_id, 0, -speed)
        
        # วนกลับลงด้านล่างเมื่อลอยพ้นขอบจอด้านบน
        if self.y < -self.r - 90:
            reset_distance = 620
            self.y = self.y + reset_distance
            self.canvas.move(self.oval_id, 0, reset_distance)
            self.canvas.move(self.line_id, 0, reset_distance)

# สร้างหน้าต่างหลักและ Canvas
root = tk.Tk()
root.title("Tkinter OOP Floating Balloons")
canvas = tk.Canvas(root, width=500, height=500, bg="#E8F0F8")
canvas.pack()

# สร้าง Array of Objects ตามแนวทางของสไลด์
balloons = [
    Balloon(canvas, 120, 420, 35, "#FF6B6B"),
    Balloon(canvas, 250, 470, 45, "#4ECDC4"),
    Balloon(canvas, 380, 440, 30, "#FFD166")
]

# ฟังก์ชันวนลูปแอนิเมชันสำหรับ Tkinter
def animate():
    i = 0
    while i < len(balloons):
        balloons[i].move(speed=2 + i)
        i = i + 1
    root.after(30, animate)

animate()
root.mainloop()