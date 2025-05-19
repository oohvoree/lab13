import tkinter as tk
import math

def summa():
    try:
        x = float(entry1.get())
        сума = sum(math.sin(x**k) / (4 * k) for k in range(1, 9))
        label2.config(text=f"Сума: {сума:.5f}")
    except ValueError:
        label2.config(text="Введіть коректне число для x")

root = tk.Tk()
root.title("Проєкт «Сума»")

label_image=tk.Label()
photo=tk.PhotoImage(file="33.gif")
label_image.configure(image=photo)
label_image.grid(row=0, column=0, columnspan=2, pady=10)

label1= tk.Label(root, text="Введіть x:")
label1.grid(row=1, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=10)

button1 = tk.Button(root, text="Обчислити", command=summa)
button1.grid(row=2, column=0, columnspan=1, pady=10)

label2 = tk.Label(root, text="Сума:")
label2.grid(row=3, column=0, columnspan=1, pady=10)

root.mainloop()
