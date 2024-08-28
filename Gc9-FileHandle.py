# ข้อที่ 1: สร้างไฟล์ .txt
with open('task1.txt', 'w') as file:
    file.write('Hello, Python!')

# ข้อที่ 2: เขียนข้อความเพิ่มในไฟล์
with open('task1.txt', 'a') as file:
    file.write("\nLet's learn file handling.")

# ข้อที่ 3: อ่านข้อมูลจากไฟล์
with open('task1.txt', 'r') as file:
    content = file.read()
    print(content)

# ข้อที่ 4: ลบข้อมูลในไฟล์
with open('task1.txt', 'w') as file:
    file.write('')

# ข้อที่ 5: เขียนโปรแกรม loop for ตัวเลขลงในไฟล์
with open('task5.txt', 'w') as file:
    for i in range(1, 1001):
        file.write(f'{i}\n')

# ข้อที่ 6: อ่านและแสดงตัวเลขจากไฟล์
with open('task5.txt', 'r') as file:
    numbers = file.read()
    print(numbers)
