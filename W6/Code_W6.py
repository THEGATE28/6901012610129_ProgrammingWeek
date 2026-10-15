def analyze_and_shift(text, shift_val=1):
    result = ""
    i = 0
    print("Index\tChar\tASCII\tType")
    print("-" * 32)
    
    # วนลูปตรวจสอบทีละตัวอักษรตามความยาว len(text)
    while i < len(text):
        ch = text[i]
        ascii_code = ord(ch)
        
        # ตรวจสอบประเภทตัวอักษรด้วย String Method
        if ch.isalpha():
            char_type = "Letter"
            # แปลงรหัส ASCII ถัดไปด้วย chr()
            shifted_char = chr(ascii_code + shift_val)
        elif ch.isdigit():
            char_type = "Digit"
            shifted_char = ch
        else:
            char_type = "Symbol"
            shifted_char = ch
            
        print(f"{i}\t{ch}\t{ascii_code}\t{char_type}")
        
        # เนื่องจาก String เป็น Immutable จึงต้องใช้วิธีสร้างและต่อสตริงใหม่
        result = result + shifted_char
        i = i + 1
        
    return result

original = "KMUTNB46"
transformed = analyze_and_shift(original, 1)

print("\nOriginal   :", original)
print("Transformed:", transformed)