import math

# ฟังก์ชันคำนวณระยะห่างระหว่างจุด 2 จุด (Pythagorean theorem)
def cal_distance(x1, y1, x2, y2):
    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)
    result = math.sqrt(diff_x**2 + diff_y**2)
    return result

# ฟังก์ชันตรวจสอบตำแหน่งสัมพัทธ์ในแนวแกน X (Nested/Conditional check)
def check_relative_position(origin_x, target_x):
    offset = target_x - origin_x
    if offset > 0:
        return "Target is on the RIGHT (Positive)"
    elif offset < 0:
        return "Target is on the LEFT (Negative)"
    else:
        return "Target is at the SAME X position (Zero)"

# รับค่าพิกัดจากผู้ใช้
x1, y1 = 200, 200
x2 = float(input("Enter target X coordinate: "))
y2 = float(input("Enter target Y coordinate: "))

# เรียกใช้ฟังก์ชันและแสดงผล
dist = cal_distance(x1, y1, x2, y2)
position_status = check_relative_position(x1, x2)

print("Distance:", round(dist, 2))
print("Status:", position_status)