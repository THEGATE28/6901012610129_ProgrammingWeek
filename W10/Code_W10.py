# 1. ฟังก์ชันแสดงผล 2D Array ในรูปแบบตาราง (Nested While Loop)
def print_grid(matrix, title):
    print(f"\n--- {title} ---")
    i = 0
    while i < len(matrix):
        j = 0
        row_str = ""
        while j < len(matrix[i]):
            row_str += f"{matrix[i][j]:>6.1f} "
            j = j + 1
        print(row_str)
        i = i + 1

# 2. ฟังก์ชันบวกเมทริกซ์ 2 ตัวเข้าด้วยกัน (Matrix Addition)
def add_matrices(mat_a, mat_b):
    result = []
    i = 0
    while i < len(mat_a):
        row = []
        j = 0
        while j < len(mat_a[i]):
            # นำค่าที่ตำแหน่งเดียวกันมาบวกกัน
            row.append(mat_a[i][j] + mat_b[i][j])
            j = j + 1
        result.append(row)
        i = i + 1
    return result

# 3. ฟังก์ชันปรับค่าใน List โดยตรง (สาธิต Pass-by-reference / List Mutation)
def apply_calibration(matrix, offset):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            matrix[i][j] = matrix[i][j] + offset
            j = j + 1
        i = i + 1

# 4. ฟังก์ชันคำนวณผลรวมอุณหภูมิทั้งหมดใน 2D Array (2D Sum)
def sum_all_sensors(matrix):
    total = 0.0
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            total = total + matrix[i][j]
            j = j + 1
        i = i + 1
    return total

# 5. ฟังก์ชันนับจำนวนเซนเซอร์ที่ค่าเกินเกณฑ์เตือนภัย (2D Count / Threshold Search)
def count_warning_zones(matrix, threshold):
    count = 0
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] >= threshold:
                count = count + 1
            j = j + 1
        i = i + 1
    return count

# --- ส่วนการทำงานหลัก (Main Program) ---

# ตารางอุณหภูมิเริ่มต้นจากเซนเซอร์ 9 จุด (3x3 Grid)
raw_sensors = [
    [35.5, 36.0, 38.2],
    [34.8, 39.1, 41.0],
    [33.0, 37.4, 40.5]
]

# ตารางค่าปรับแก้สภาพแวดล้อม (Calibration Matrix)
env_offset = [
    [0.5, 0.2, -0.2],
    [0.4, 0.8,  1.0],
    [0.0, 0.5,  0.7]
]

print_grid(raw_sensors, "Raw Sensor Readings (°C)")
print_grid(env_offset, "Environmental Offset Matrix")

# รวมตารางเพื่อหาค่าจริง
calibrated_grid = add_matrices(raw_sensors, env_offset)
print_grid(calibrated_grid, "Calibrated Sensor Grid (°C)")

# สาธิตการปรับแต่งค่าระดับระบบ (+1.5°C ให้ทุกจุดผ่านฟังก์ชันแบบ In-place)
apply_calibration(calibrated_grid, 1.5)
print_grid(calibrated_grid, "After Sensor Drift Calibration (+1.5°C)")

# วิเคราะห์ค่าทางสถิติของตาราง
total_temp = sum_all_sensors(calibrated_grid)
sensor_count = len(calibrated_grid) * len(calibrated_grid[0])
avg_temp = total_temp / sensor_count
hot_spots = count_warning_zones(calibrated_grid, threshold=40.0)

print("\n--- Diagnostic Report ---")
print(f"Total Grid Temperature Sum : {total_temp:.2f} °C")
print(f"Average Grid Temperature    : {avg_temp:.2f} °C")
print(f"Warning Alert Sensors (>=40°C): {hot_spots} nodes")