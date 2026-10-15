# 1. เขียนข้อมูลตัวเลขลงไฟล์ข้อความ (Write Mode)
with open("scores.txt", "w") as file:
    file.write("78\n")
    file.write("92\n")
    file.write("65\n")
    file.write("88\n")
    file.write("54\n")

# 2. อ่านข้อมูล ประมวลผล และดักจับกรณีไม่พบไฟล์ (Read Mode + Exception Handling)
scores = []
try:
    with open("scores.txt", "r") as file:
        for line in file:
            clean_line = line.strip()
            # ตรวจสอบว่าบรรทัดนี้เป็นตัวเลขหรือไม่ก่อนแปลงชนิดข้อมูล
            if clean_line.isdigit():
                scores.append(int(clean_line))
except FileNotFoundError:
    print("Error: scores.txt is not found")

# 3. คำนวณค่าสถิติพื้นฐานจากข้อมูลในไฟล์
if len(scores) > 0:
    total = sum(scores)
    avg = total / len(scores)
    max_val = max(scores)
    min_val = min(scores)

    print("Scores loaded:", scores)
    print(f"Average: {avg:.2f}")
    print(f"Max: {max_val} | Min: {min_val}")

    # 4. บันทึกผลการวิเคราะห์ต่อท้ายไฟล์เดิม (Append Mode)
    with open("scores.txt", "a") as file:
        file.write(f"\n--- Summary ---\nAverage: {avg:.2f}\nMax: {max_val}\n")
    print("Summary appended successfully.")