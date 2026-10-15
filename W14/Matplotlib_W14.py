import matplotlib.pyplot as plt

machines = ['Machine A', 'Machine B', 'Machine C', 'Machine D', 'Machine E', 'Machine F']
downtime_hours = [4.5, 3.0, 5.0, 26.5, 4.0, 6.0]

# คำนวณค่าเฉลี่ย
avg_val = sum(downtime_hours) / len(downtime_hours)

# กำหนดสีแท่งกราฟ: หากเป็น Outlier (> 15 ชม.) ให้เป็นสีแดงอมส้ม ส่วนปกติใช้สีน้ำเงินสุภาพ
bar_colors = []
for h in downtime_hours:
    if h > 15:
        bar_colors.append('#E63946')  # Outlier color
    else:
        bar_colors.append('#457B9D')  # Normal color

# สร้าง Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(machines, downtime_hours, color=bar_colors, width=0.6)

# ลากเส้นประแสดงระดับค่าเฉลี่ย (Average Line)
plt.axhline(avg_val, color='#E76F51', linestyle='--', linewidth=1.5, label=f'Average ({avg_val:.1f} hrs)')

# กำหนดชื่อเรื่องและป้ายกำกับแกน
plt.title('Machine Downtime Analysis (Outlier Detection)', fontsize=14, fontweight='bold')
plt.xlabel('Factory Machinery', fontsize=11)
plt.ylabel('Downtime (Hours)', fontsize=11)
plt.legend()
plt.tight_layout()

# แสดงผลกราฟ
plt.show()