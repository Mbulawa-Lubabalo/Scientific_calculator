import tkinter as tk

def nth_fibonacciWindow(frame, go_back_callback):

    label_entry = tk.Label(frame, text="Index: ")
    label_entry.grid(row=0, column=0)

    entry = tk.Entry(frame)
    entry.grid(row=0, column=1)

    fibinacci_nthValue = tk.Label(frame, text="nth Value: ")
    fibinacci_nthValue.grid(row=1, column=0, columnspan=2)


    def nth_fibonacci():
        num = entry.get()

        try:
            num = int(num)
            if num < 0:
                fibinacci_nthValue.config(text="Enter a positive integer.")
                return
            else:
                results = calculate(num)
                fibinacci_nthValue.config(text=f"nth Value: {results}")

        except ValueError:
            fibinacci_nthValue.config(text="Invalid input. Enter a number.")


    button = tk.Button(frame, text="Calculate", command=nth_fibonacci)
    button.grid(row=2, column=0, columnspan=2)

    # Back button
    back_button = tk.Button(frame, text="Back", command=go_back_callback, bg="gray")
    back_button.grid(row=3, column=0, columnspan=2, pady=10)



def calculate(n):
    if n < 0:
        return "Enter a positive integer."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate(n-1) + calculate(n-2)