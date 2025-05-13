import tkinter as tk
from math import sqrt, sin, log

def calculate_function(event=None):
    try:
        a = float(entry_a.get().replace(',', '.'))
        b = float(entry_b.get().replace(',', '.'))
        c = float(entry_c.get().replace(',', '.'))

        if b <= 0:
            label_result.config(text="Помилка: логарифм від ≤ 0")
            return

        result = (sqrt(b * c + a**2) / log(b)) + sin(a)
        format_result = "{:.2f}".format(result)
        label_result.config(text="Результат: " + format_result)
    except Exception as e:
        label_result.config(text="Помилка: " + str(e))

root = tk.Tk()
root.title("Обчислення функції")
root.geometry("400x300")

root.configure(bg="lavender")

label_image=tk.Label()
photo=tk.PhotoImage(file="11.gif")
label_image.configure(image=photo)
label_image.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Введіть значення a:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Введіть значення b:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Введіть значення c:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_c = tk.Entry(root)
entry_c.grid(row=3, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="Обчислити")
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)
button_calculate.bind('<Button-1>', calculate_function)

# Обробка натискання Enter в останньому полі
entry_c.bind('<Return>', calculate_function)

label_result = tk.Label(root, text="")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()