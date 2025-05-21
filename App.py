import tkinter as tk


window = tk.Tk()
window.geometry("420x420")
window.title("App")

frame = tk.Frame(window)
frame.grid(row=0, column=0)


if __name__ == "__main__":
    window.mainloop()