import tkinter as tk

# Event Handler: ทำงานเมื่อปุ่ม Button ถูกคลิก
def calculate():
    try:
        # อ่านค่าจากช่อง Entry ทั้ง 2 ช่อง
        price = float(entry_price.get())
        qty = float(entry_qty.get())
        
        # ประมวลผลคำนวณค่าผลคูณ
        total = price * qty
        
        # ปรับปรุงการแสดงผลของ Label ผ่าน .config()
        label_result.config(
            text=f"Total Amount: {total:,.2f} THB",
            fg="#1A73E8"
        )
    except ValueError:
        label_result.config(
            text="Please enter valid numbers!",
            fg="#D93025"
        )

# 1. สร้างหน้าต่างหลักและกำหนดค่าขนาด/ชื่อหน้าต่าง
window = tk.Tk()
window.title("Product Price Estimator")
window.geometry("450x420")
window.configure(bg="#F8F9FA")

# 2. ป้ายข้อความส่วนหัว
header_label = tk.Label(
    window,
    text="Cost Calculation Tool",
    font=("Arial", 16, "bold"),
    bg="#F8F9FA",
    fg="#202124"
)
header_label.pack(pady=20)

# คำอธิบายช่องกรอกข้อมูล
input_hint = tk.Label(
    window,
    text="Enter Unit Price (THB) and Quantity:",
    font=("Arial", 11),
    bg="#F8F9FA",
    fg="#5F6368"
)
input_hint.pack(pady=5)

# 3. จัดกลุ่ม Entry ด้วย Frame เพื่อวางขนานกันในแนวนอน
entry_frame = tk.Frame(window, bg="#F8F9FA")
entry_frame.pack(pady=15)

entry_price = tk.Entry(entry_frame, width=12, font=("Arial", 12), justify="center")
entry_price.pack(side="left", padx=10)
entry_price.insert(0, "150.0")

entry_qty = tk.Entry(entry_frame, width=12, font=("Arial", 12), justify="center")
entry_qty.pack(side="left", padx=10)
entry_qty.insert(0, "3")

# 4. ปุ่มสั่งคำนวณผลลัพธ์ เชื่อมโยงฟังก์ชันด้วยพารามิเตอร์ command
btn_calc = tk.Button(
    window,
    text="Calculate Total",
    font=("Arial", 11, "bold"),
    bg="#1A73E8",
    fg="white",
    padx=15,
    pady=6,
    relief="flat",
    cursor="hand2",
    command=calculate
)
btn_calc.pack(pady=25)

# 5. ป้ายแสดงผลลัพธ์ที่จะถูกอัปเดตด้วย .config()
label_result = tk.Label(
    window,
    text="Total Amount: 0.00 THB",
    font=("Arial", 14, "bold"),
    bg="#F8F9FA",
    fg="#3C4043"
)
label_result.pack(pady=15)

# 6. เริ่มการวนลูปเพื่อรอรับ Event จากผู้ใช้
window.mainloop()