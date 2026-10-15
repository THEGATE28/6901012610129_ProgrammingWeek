import getpass

# 1. ระบบจำกัดจำนวนครั้งการกรอกรหัสผ่าน (Password Attempt Limiter)
max_tries = 3
count = 0
login_success = False

while count < max_tries and not login_success:
    user_password = getpass.getpass("Enter your password: ")
    if user_password == "secret123":
        print("Access granted :)\n")
        login_success = True
    else:
        count = count + 1
        remaining = max_tries - count
        print(f"Access denied! Remaining attempts: {remaining}")

# 2. คำนวณผลรวม 1 ถึง n เมื่อล็อกอินสำเร็จ (Sum from 1 to n)
if login_success:
    n = int(input("Enter positive integer n for summation: "))
    current = 1
    total_sum = 0
    
    while current <= n:
        total_sum = total_sum + current
        current = current + 1
        
    print(f"Sum from 1 to {n} is: {total_sum}")
else:
    print("Account locked due to too many failed attempts.")