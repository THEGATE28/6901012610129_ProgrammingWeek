class FixedIntBuffer:
    def __init__(self, capacity):
        # 1. จำลองการสร้าง Fixed-size Array เริ่มต้นด้วยค่า 0 เหมือน int[] b = new int[5]
        self.capacity = capacity
        self.data = [0] * capacity
        self.count = 0

    # จำลองฟังก์ชัน Parsing ข้อความ คล้าย Integer.parseInt()
    def parse_and_insert(self, str_val):
        if self.count >= self.capacity:
            print(f"[Error] Buffer Full! Cannot insert: {str_val}")
            return False
        
        try:
            # String parsing และ type casting เป็น int
            parsed_num = int(str_val.strip())
            self.data[self.count] = parsed_num
            self.count = self.count + 1
            return True
        except ValueError:
            print(f"[Error] Type mismatch: Cannot parse '{str_val}' to integer")
            return False

    # คำนวณค่ากึ่งกลางระหว่างสมาชิกตัวแรกและตัวล่าสุด (Integer vs Float Division)
    def calculate_middle_values(self):
        if self.count < 2:
            return None, None
        
        first = self.data[0]
        last = self.data[self.count - 1]
        
        # เปรียบเทียบผลลัพธ์ Integer Division (แบบ Java 5/2 = 2) กับ Float Division (5/2.0 = 2.5)
        int_div_result = (first + last) // 2
        float_div_result = (first + last) / 2.0
        return int_div_result, float_div_result

    # แสดงผลสมาชิกในอาร์เรย์ทั้งหมด
    def print_elements(self):
        print("Buffer Content (Array): [", end="")
        for i in range(len(self.data)):
            print(self.data[i], end=", " if i < len(self.data) - 1 else "")
        print("]")

# --- ส่วนทดสอบการทำงานหลัก ---
buffer = FixedIntBuffer(capacity=5)

raw_inputs = ["15", "8", "invalid_text", "22", "30", "99"]

print("=== Processing Input Stream into Fixed Buffer ===")
for item in raw_inputs:
    buffer.parse_and_insert(item)

buffer.print_elements()

int_mid, float_mid = buffer.calculate_middle_values()
print("\n--- Division Behavior Demonstration ---")
print(f"Integer Division result (//) : {int_mid}")
print(f"Floating Division result (/)  : {float_mid}")