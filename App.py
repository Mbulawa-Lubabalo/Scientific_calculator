import tkinter as tk
from Features.factorial import factorial_window
from Features.nthFibonacciValue import nth_fibonacciWindow
# from login import draw_login_form


def main_menu(frame, back_callback):
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
    # Add main menu content
    factorial_button = tk.Button(
        frame, text="Factorial",
        command=lambda: open_factorial_window(frame, back_callback)
    )
    factorial_button.grid(row=1, column=0)

    fib_button = tk.Button(
        frame, text="Fib(n)",
        command=lambda: open_nthFibonacci_window(frame, back_callback)
    )
    fib_button.grid(row=1, column=1)

    logout_button = tk.Button(frame, text="Logout", command=back_callback)
    logout_button.grid(row=2, column=0)  # , columnspan=2, pady=20


def open_factorial_window(frame, back_callback):
    """
    Opens the factorial feature window.

    Clears current widgets from the frame and calls the factorial_window
    function to load the factorial UI, passing a reference to main_menu
    as the callback for the "back" action.
    """
    for widget in frame.winfo_children():
        widget.destroy()

    # Load the factorial UI and pass the 'back' function
    factorial_window(frame, lambda: main_menu(frame, back_callback))


def open_nthFibonacci_window(frame, back_callback):
    # Clear the existing widgets from the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Load the factorial UI and pass the 'back' function
    nth_fibonacciWindow(frame, lambda: main_menu(frame, back_callback))