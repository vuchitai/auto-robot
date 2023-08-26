import tkinter as tk
from PIL import ImageTk, Image

# Tạo một đối tượng cửa sổ
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Ứng dụng Tkinter")

# Đặt kích thước cửa sổ
window.geometry("400x300")

# Tải hình ảnh
image = Image.open("C:\\Users\\vuchi\\OneDrive\\Desktop\\picture.png")
image.thumbnail((300, 200))
photo = ImageTk.PhotoImage(image)

# Tạo một nhãn và hiển thị hình ảnh
label = tk.Label(window, image=photo)
label.pack()

# Chạy vòng lặp chính của ứng dụng
window.mainloop()