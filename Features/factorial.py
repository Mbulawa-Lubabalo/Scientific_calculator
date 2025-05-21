import tkinter as tk

def factorial_window(frame,go_back_callback):

    """
    Displays the factorial calculation interface within the given Tkinter frame.

    Args:
        frame (tk.Frame): The parent frame where the widgets will be placed.
        go_back_callback (function): A callback function that is called when 
                                     the user presses the "Back" button. Typically
                                     used to return to the main menu or previous screen.

    The interface includes:
        - An entry field to input a number.
        - A button to calculate the factorial of the input number.
        - A label to display the result.
        - A "Back" button to return to the previous window.
    """
    label_entry = tk.Label(frame, text="Number:")
    label_entry.grid(row=0, column=0)

    entry = tk.Entry(frame)
    entry.grid(row=0, column=1)

    factorial_answer = tk.Label(frame, text="Factorial: ")
    factorial_answer.grid(row=1, column=0, columnspan=2)

    def calculate_factorial():
        """
        Retrieves the user input, validates it, and calculates the factorial
        if the input is a valid non-negative integer. Displays the result
        or an appropriate error message.
        """
        num = entry.get()
        try:
            num = int(num)

            if num < 0:
                factorial_answer.config(text="Enter a positive integer.")
                return

            factorial = 1
            for i in range(1, num + 1):
                factorial *= i
            factorial_answer.config(text=f"Factorial: {factorial}")
        except ValueError:
            factorial_answer.config(text="Invalid input. Enter a number.")

    button = tk.Button(frame, text="Calculate", command=calculate_factorial)
    button.grid(row=2, column=0, columnspan=2)

    # Back button
    back_button = tk.Button(frame, text="Back", command=go_back_callback, bg="gray")
    back_button.grid(row=3, column=0, columnspan=2, pady=10)
