import os

# 1. นิยามคลาสสำหรับจัดการไฟล์บันทึก (Encapsulation)
class LogFileManager:
    def __init__(self, filename, service_name):
        # แอตทริบิวต์ประจำอ็อบเจกต์ (Attributes)
        self.filename = filename
        self.service_name = service_name
        self.write_count = 0

    # เมทอดสำหรับบันทึกข้อความลงไฟล์จริง
    def write_log(self, message):
        with open(self.filename, "a") as f:
            f.write(f"[{self.service_name}] {message}\n")
        self.write_count = self.write_count + 1

    # เมทอดดึงขนาดไฟล์ปัจจุบันจากระบบปฏิบัติการ
    def get_file_size(self):
        if os.path.exists(self.filename):
            return os.path.getsize(self.filename)
        return 0

    # เมทอดแสดงสถานะและข้อมูลของไฟล์
    def display_status(self):
        size_bytes = self.get_file_size()
        print(f"Service: {self.service_name:<12} | File: {self.filename:<16} | Entries: {self.write_count:<3} | Size: {size_bytes} bytes")


# 2. การทำงานหลัก: ใช้งาน List of Objects ร่วมกับ While Loop
def main():
    # สร้างกลุ่มอ็อบเจกต์ (Array of Objects)
    logs = [
        LogFileManager("auth_service.log", "Authentication"),
        LogFileManager("db_service.log", "Database"),
        LogFileManager("network_io.log", "Network Gateway")
    ]

    # จำลองการส่งข้อมูลเข้าบันทึกผ่านเมทอดของแต่ละอ็อบเจกต์
    logs[0].write_log("User admin logged in successfully.")
    logs[0].write_log("Token refreshed for session #402.")
    logs[1].write_log("Connection pool initialized with 10 clients.")
    logs[2].write_log("Packet inbound latency within normal threshold.")

    print("=== Server Log Files Summary ===")
    
    # วนลูปอ่านค่าจากอาร์เรย์ของอ็อบเจกต์
    total_size = 0
    i = 0
    while i < len(logs):
        logs[i].display_status()
        total_size = total_size + logs[i].get_file_size()
        i = i + 1

    print("-" * 65)
    print(f"Total Storage Used: {total_size} bytes")

if __name__ == "__main__":
    main()