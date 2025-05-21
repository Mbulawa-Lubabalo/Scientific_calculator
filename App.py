import tkinter as tk
from Features.factorial import factorial_window
from Features.nthFibonacciValue import nth_fibonacciWindow

def main_menu():
    """
    Displays the main menu on the application window.

    Clears any existing widgets from the frame and adds a button
    to navigate to the factorial window.
    """
    for widget in frame.winfo_children():
        widget.destroy()

    # Create an empty row and column for spacing
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    # Add main menu content
    factorial_button = tk.Button(frame, text="Factorial", command=open_factorial_window)
    factorial_button.grid(row=1, column=0)

    factorial_button = tk.Button(frame, text="Fib(n)", command=open_nthFibonacci_window)
    factorial_button.grid(row=1, column=1)


def open_factorial_window():
    """
    Opens the factorial feature window.

    Clears current widgets from the frame and calls the factorial_window
    function to load the factorial UI, passing a reference to main_menu
    as the callback for the "back" action.
    """
    for widget in frame.winfo_children():
        widget.destroy()

    # Load the factorial UI and pass the 'back' function
    factorial_window(frame, main_menu)

def open_nthFibonacci_window():
    # Clear the existing widgets from the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Load the factorial UI and pass the 'back' function
    nth_fibonacciWindow(frame, main_menu)


window = tk.Tk()
window.geometry("420x420")
window.title("App")

frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky="")

# Make the frame expand and fill the window
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

main_menu()

if __name__ == "__main__":
    window.mainloop()