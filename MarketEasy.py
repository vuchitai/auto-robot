import os
import datetime as dt

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def DisplayTerminal():
    clear_screen()
    print("Cảm ơn bạn đã mua hàng tại cửa hàng!")

    print("--------------------------------------") # alt + shift + ->
    print("Hoá đơn")
    for item in gio_hang:
        print(item)
    print("--------------------------------------") # alt + shift + ->
    print(f"Tổng giá trị các lần mua: {total_purchase} VND")
    print("--------------------------------------") # alt + shift + ->

def LichSuMuaHang():
    now = dt.datetime.now()  # Sử dụng dt thay cho datetime
    with open("hoadon.txt", "a", encoding="utf-8") as f:  # Sử dụng chế độ "a" (append)
        f.write("\nThời gian mua hàng: " + now.strftime("%d-%m-%Y %H:%M"))
        f.write("\n")
        f.write("Thông tin hóa đơn: ")
        f.write("\n\n")
        for item in gio_hang:
            f.write(item + "\n")
        f.write("\n")
        f.write("Tổng giá trị các lần mua: " + str(total_purchase) + "\n")
        f.write("-" * 30 + "\n")
gao_price = 10000
thit_price = 20000
rau_price = 5000
total_purchase = 0
gio_hang = []  # Danh sách lưu thông tin giỏ hàng

while True:
    clear_screen()
    print("Cửa hàng chúng tôi gồm có: ")
    print("1. Gạo")
    print("2. Thịt")
    print("3. Rau")
    print("4. Xem giỏ hàng")
    print("5. Thoát")

    choice = int(input("Nhập số để chọn món ăn: "))
    clear_screen()

    if choice == 1:
        print("Bạn đã chọn Gạo")
        kg = int(input("Bạn muốn mua bao nhiêu kg gạo? "))
        total_price = gao_price * kg
        total_purchase += total_price
        gio_hang.append(f"{kg} kg gạo - {total_price} VND")
        print(f"Bạn đã chọn mua {kg} kg gạo")
        print(f"Giá 1 kg gạo là: {gao_price} VND")
        print(f"Tổng tiền: {total_price} VND")

    elif choice == 2:
        print("Bạn đã chọn Thịt")
        kg = int(input("Bạn muốn mua bao nhiêu kg thịt? "))
        total_price = thit_price * kg
        total_purchase += total_price
        gio_hang.append(f"{kg} kg thịt - {total_price} VND")
        print(f"Bạn đã chọn mua {kg} kg thịt")
        print(f"Giá 1 kg thịt là: {thit_price} VND")
        print(f"Tổng tiền: {total_price} VND")

    elif choice == 3:
        print("Bạn đã chọn Rau")
        kg = int(input("Bạn muốn mua bao nhiêu kg rau? "))
        total_price = rau_price * kg
        total_purchase += total_price
        gio_hang.append(f"{kg} kg rau - {total_price} VND")
        print(f"Bạn đã chọn mua {kg} kg rau")
        print(f"Giá 1 kg rau là: {rau_price} VND")
        print(f"Tổng tiền: {total_price} VND")

    elif choice == 4:
        clear_screen()
        if len(gio_hang) == 0:
            print("Giỏ hàng trống.")
        else:
            print("Giỏ hàng:")
            for item in gio_hang:
                print(item)
        input("Nhấn Enter để tiếp tục...")
        continue

    elif choice == 5:
        break

    cont = input("Tiếp tục mua hàng? (có/không): ")
    if cont.lower() != 'có':
        break

DisplayTerminal()
LichSuMuaHang()