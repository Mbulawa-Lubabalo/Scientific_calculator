import tkinter as tk
from tkinter import messagebox



def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome!")
        

        
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")


def draw_login_form():
    """
    Displays the login form inside the main frame.
    """
    # Clear frame before drawing login UI
    for widget in frame.winfo_children():
        widget.destroy()

    # Username
    username_label = tk.Label(frame, text="Username:")
    username_label.grid(row=0, column=0, pady=5, padx=5)
    global username_entry
    username_entry = tk.Entry(frame)
    username_entry.grid(row=0, column=1, pady=5, padx=5)

    # Password
    password_label = tk.Label(frame, text="Password:")
    password_label.grid(row=1, column=0, pady=5, padx=5)
    global password_entry
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, pady=5, padx=5)

    # Login Button
    login_button = tk.Button(frame, text="Login", command=login)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)


    # Main window setup
window = tk.Tk()
window.geometry("420x420")
window.title("Login Page")

# Main frame for all content
frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky="")

# Make frame expand
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Load login form
draw_login_form()

# Start app
window.mainloop()