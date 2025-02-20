import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันในการคำนวณความถี่และแสดงข้อมูล
def information():
    try:
        v = float(entry_v.get())  # รับค่า v
        λ = float(entry_lambda.get())  # รับค่า λ
        
        frequency = v / λ  # คำนวณความถี่
        result_label.config(text=f"ความถี่: {frequency:.2f} Hz", fg="blue")  # แสดงผลความถี่
        
        # เช็คค่าความถี่และแสดงคำแนะนำ
        if frequency > 7:
            advice_label.config(text="ตรวจสอบหลอดเลือด", fg="red")
        elif 2 < frequency <= 7:
            advice_label.config(text="ตรวจสอบอวัยวะภายใน", fg="green")
        else:
            advice_label.config(text="ตรวจสอบทารก", fg="purple")
    
    except ValueError:
        messagebox.showerror("ข้อผิดพลาดในการป้อนข้อมูล", "กรุณาป้อนตัวเลขที่ถูกต้อง.")

# ฟังก์ชันในการล้างข้อมูล
def clear():
    entry_v.delete(0, tk.END)  # ล้างช่องกรอก v
    entry_lambda.delete(0, tk.END)  # ล้างช่องกรอก λ
    result_label.config(text="ความถี่: ", fg="black")  # ล้างผลลัพธ์
    advice_label.config(text="", fg="black")  # ล้างคำแนะนำ

# ฟังก์ชันในการปิดโปรแกรม
def exit_program():
    root.destroy()  # ใช้ destroy แทน quit เพื่อปิดหน้าต่าง

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Frequency for physical examination")

# ขยายขนาดหน้าต่าง
root.geometry("400x350")

# ตั้งค่าให้หน้าต่างอยู่ตรงกลาง
root.resizable(False, False)  # ปิดการปรับขนาด

# ตั้งพื้นหลังของหน้าต่าง
root.config(bg="#f0f8ff")  # สีฟ้าอ่อน

# สร้างกรอบหลักสำหรับการจัดตำแหน่งทั้งหมด
frame = tk.Frame(root, bg="#f0f8ff")  # กรอบมีพื้นหลังสีฟ้าอ่อน
frame.pack(expand=True)

# สร้างช่องป้อนข้อมูล
tk.Label(frame, text="ป้อนค่า v (ความเร็ว):", bg="#f0f8ff", font=("Arial", 12, "bold")).pack(padx=10, pady=5)
entry_v = tk.Entry(frame, font=("Arial", 12), bd=2, relief="solid")
entry_v.pack(padx=10, pady=5)

tk.Label(frame, text="ป้อนค่า λ (ความยาวคลื่น):", bg="#f0f8ff", font=("Arial", 12, "bold")).pack(padx=10, pady=5)
entry_lambda = tk.Entry(frame, font=("Arial", 12), bd=2, relief="solid")
entry_lambda.pack(padx=10, pady=5)

# ป้ายแสดงผลความถี่
result_label = tk.Label(frame, text="ความถี่: ", fg="black", font=("Arial", 12, "bold"), bg="#f0f8ff")
result_label.pack(pady=10)

# ป้ายแสดงคำแนะนำ
advice_label = tk.Label(frame, text="", fg="black", font=("Arial", 12), bg="#f0f8ff")
advice_label.pack(pady=10)

# สร้างกรอบสำหรับปุ่ม
button_frame = tk.Frame(frame, bg="#f0f8ff")
button_frame.pack(pady=10)

# ปุ่มคำนวณ
calculate_button = tk.Button(button_frame, text="คำนวณ", command=information, bg="blue", fg="white", font=("Arial", 10, "bold"), relief="raised")
calculate_button.pack(side=tk.LEFT, padx=10)

# ปุ่มล้างข้อมูล
clear_button = tk.Button(button_frame, text="ล้างข้อมูล", command=clear, bg="green", fg="white", font=("Arial", 10, "bold"), relief="raised")
clear_button.pack(side=tk.LEFT, padx=10)

# ปุ่มออก
exit_button = tk.Button(button_frame, text="ออก", command=exit_program, bg="red", fg="white", font=("Arial", 10, "bold"), relief="raised")
exit_button.pack(side=tk.LEFT, padx=10)

# รันแอปพลิเคชัน
root.mainloop()

