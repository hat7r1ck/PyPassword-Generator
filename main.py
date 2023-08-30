import random
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = int(letters_entry.get())
    nr_symbols = int(symbols_entry.get())
    nr_numbers = int(numbers_entry.get())

    password = []

    for char in range(nr_letters):
        password += random.choice(letters)

    for num in range(nr_numbers):
        password += random.choice(numbers)

    for sym in range(nr_symbols):
        password += random.choice(symbols)
    random.shuffle(password)

    password_final = ""
    for char in password:
        password_final += char

    result_label.config(text=f"Your password is:\n{password_final}")
    copy_button.config(state="normal")
    generated_password.set(password_final)

def copy_to_clipboard():
    pyperclip.copy(generated_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

app = tk.Tk()
app.title("PyPassword Generator")
app.geometry("400x350")  # Set fixed size

# Dark mode appearance
app.configure(bg="#212121")
for widget in app.winfo_children():
    widget.configure(bg="#212121", fg="white", font=("Helvetica", 12))

header_label = tk.Label(app, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#212121", fg="white")
header_label.pack(pady=10)

letters_label = tk.Label(app, text="Number of letters:", bg="#212121", fg="white")
letters_label.pack()
letters_entry = tk.Entry(app)
letters_entry.pack()

numbers_label = tk.Label(app, text="Number of numbers:", bg="#212121", fg="white")
numbers_label.pack()
numbers_entry = tk.Entry(app)
numbers_entry.pack()

symbols_label = tk.Label(app, text="Number of symbols:", bg="#212121", fg="white")
symbols_label.pack()
symbols_entry = tk.Entry(app)
symbols_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white")
generate_button.pack(pady=10)

result_label = tk.Label(app, text="Generated Password:", bg="#212121", fg="white", font=("Helvetica", 12))
result_label.pack()

generated_password = tk.StringVar()
copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=10)

app.mainloop()
