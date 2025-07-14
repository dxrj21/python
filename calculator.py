def calculator():
    print("เครื่องคิดเลขภาษา Python")
    print("เลือกการดำเนินการ:")
    print("1. บวก")
    print("2. ลบ")
    print("3. คูณ")
    print("4. หาร")

    choice = input("กรุณาเลือก (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("ป้อนตัวเลขตัวที่ 1: "))
        num2 = float(input("ป้อนตัวเลขตัวที่ 2: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("ไม่สามารถหารด้วยศูนย์ได้")
    else:
        print("เลือกไม่ถูกต้อง กรุณาเลือกใหม่")

# เรียกใช้งานฟังก์ชัน
calculator()