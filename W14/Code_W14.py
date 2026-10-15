# 1. Data (The Raw Facts): ข้อมูลดิบชั่วโมงการหยุดทำงานของเครื่องจักรแต่ละเครื่อง
machines = ["Machine A", "Machine B", "Machine C", "Machine D", "Machine E", "Machine F"]
downtime_hours = [4.5, 3.0, 5.0, 26.5, 4.0, 6.0]  # มี Machine D ที่หยุดนานผิดปกติ

def calculate_mean(values):
    total = 0.0
    i = 0
    while i < len(values):
        total = total + values[i]
        i = i + 1
    return total / len(values)

def detect_outliers(names, values, threshold_factor=2.0):
    # คำนวณค่าเฉลี่ยตั้งต้น
    avg = calculate_mean(values)
    outliers = []
    
    # ตรวจหาค่าที่สูงกว่าค่าเฉลี่ยเกินเกณฑ์ที่กำหนด (Outlier)
    i = 0
    while i < len(values):
        if values[i] > (avg * threshold_factor):
            outliers.append((names[i], values[i]))
        i = i + 1
    return avg, outliers

# --- 2. Information (Processed Data): ประมวลผลและสรุปตัวเลขสถิติ ---
avg_downtime, detected_outliers = detect_outliers(machines, downtime_hours)

print("=== Factory Machine Downtime Report (Monthly) ===")
i = 0
while i < len(machines):
    print(f"- {machines[i]:<10}: {downtime_hours[i]:>5.1f} hours")
    i = i + 1

print("-" * 50)
print(f"Average Downtime across all machines: {avg_downtime:.2f} hours")

# --- 3. Knowledge (Actionable Understanding): วิเคราะห์เชิงลึกเพื่อการตัดสินใจ ---
print("\n=== Maintenance Insights & Knowledge ===")
if len(detected_outliers) > 0:
    print(f"Found {len(detected_outliers)} anomaly/outlier case(s):")
    i = 0
    while i < len(detected_outliers):
        name, val = detected_outliers[i]
        print(f"  * [ALERT] {name} has {val:.1f} hours downtime (Investigate motor failure)")
        i = i + 1
    print("\nAction: Do not automatically delete this record; inspect Machine D history")
    print("        to determine if scheduled overhaul or replacement is required.")
else:
    print("All machines operate within acceptable downtime limits.")