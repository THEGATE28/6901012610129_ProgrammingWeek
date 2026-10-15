# คลาสแม่ (Superclass / Base Class)
class Person:
    def __init__(self, name, weight_kg, height_m):
        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m

    # เมทอดคำนวณค่า BMI
    def get_bmi(self):
        return self.weight_kg / (self.height_m ** 2)

    # เมทอดแสดงข้อมูลพื้นฐาน
    def show_info(self):
        print(f"Name: {self.name:<10} | BMI: {self.get_bmi():.1f}", end="")

# คลาสลูก (Subclass) สำหรับนักศึกษา
class Student(Person):
    def __init__(self, name, weight_kg, height_m, student_id, activity_hours):
        # เรียกใช้ Constructor ของ Superclass
        super().__init__(name, weight_kg, height_m)
        self.student_id = student_id
        self.activity_hours = activity_hours

    # Method Overriding: ขยายการแสดงผลของ show_info()
    def show_info(self):
        super().show_info()
        print(f" | Role: Student  | ID: {self.student_id} | Activity: {self.activity_hours} hrs")

# คลาสลูก (Subclass) สำหรับบุคลากร
class Employee(Person):
    def __init__(self, name, weight_kg, height_m, staff_id, staff_discount_rate):
        super().__init__(name, weight_kg, height_m)
        self.staff_id = staff_id
        self.staff_discount_rate = staff_discount_rate

    # Method Overriding: ขยายการแสดงผลของ show_info()
    def show_info(self):
        super().show_info()
        print(f" | Role: Employee | ID: {self.staff_id} | Welfare Discount: {self.staff_discount_rate}%")

# --- ส่วนการทำงานหลัก (Polymorphism Demonstration) ---
members = [
    Student("Karan", 62.0, 1.72, "ST6701", 18),
    Employee("Somsak", 75.5, 1.68, "EM9041", 15),
    Student("Araya", 51.0, 1.60, "ST6745", 24),
    Employee("Pim", 58.0, 1.65, "EM9082", 20)
]

print("=== University Community Health & Profile List ===")
i = 0
# วนลูปอ่านข้อมูลผ่าน Array of Objects ด้วย while loop
while i < len(members):
    # เรียกเมทอดชื่อเดียวกัน แต่ทำงานตามพฤติกรรมของ Subclass แต่ละตัว (Polymorphism)
    members[i].show_info()
    i = i + 1