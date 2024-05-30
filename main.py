import tkinter as tk

def execute():
    input_text = entry.get()
    output_label.config(text=input_text)

def clear():
    entry.delete(0, tk.END)
    output_label.config(text="")

# Создание главного окна
root = tk.Tk()
root.title("программа")

# Создание виджетов
entry_label = tk.Label(root, text="Введите текст ->")
entry = tk.Entry(root, width=50)
execute_button = tk.Button(root, text="Выполнить", command=execute)
clear_button = tk.Button(root, text="Очистить", command=clear)
output_label = tk.Label(root, text="", font=("Arial", 12))

# Размещение виджетов на экране
entry_label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
execute_button.grid(row=1, column=0, padx=10, pady=10)
clear_button.grid(row=1, column=1, padx=10, pady=10)
output_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Запуск основного цикла обработки событий
root.mainloop()
