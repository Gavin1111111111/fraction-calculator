import tkinter as tk
import fractions_logic  # this imports your math file

def on_calculate():
    try:
        num1 = int(entry_num1.get())
        denom1 = int(entry_denom1.get())
        num2 = int(entry_num2.get())
        denom2 = int(entry_denom2.get())

        result = fractions_logic.add_fractions(num1, denom1, num2, denom2)

        if result is None:
            label_result.config(text="Denominator cannot be 0.")
        else:
            n, d = result
            label_result.config(text=f"Result: {n} / {d}") 

    except ValueError: #invalid input
        label_result.config(text="Please enter valid integers.")

#create the window
root = tk.Tk()
root.title("Fraction Calculator")
root.configure(bg="white")

frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Fraction 1", bg="white").grid(row=0, column=0, columnspan=2)
tk.Label(frame, text="Numerator:", bg="white").grid(row=1, column=0)
entry_num1 = tk.Entry(frame)
entry_num1.grid(row=1, column=1)

tk.Label(frame, text="Denominator:", bg="white").grid(row=2, column=0)
entry_denom1 = tk.Entry(frame)
entry_denom1.grid(row=2, column=1)

tk.Label(frame, text="Fraction 2", bg="white").grid(row=3, column=0, columnspan=2)
tk.Label(frame, text="Numerator:", bg="white").grid(row=4, column=0)
entry_num2 = tk.Entry(frame)
entry_num2.grid(row=4, column=1)

tk.Label(frame, text="Denominator:", bg="white").grid(row=5, column=0)
entry_denom2 = tk.Entry(frame)
entry_denom2.grid(row=5, column=1)

btn = tk.Button(frame, text="Add Fractions", command=on_calculate)
btn.grid(row=6, column=0, columnspan=2, pady=10)

label_result = tk.Label(frame, text="Result:", bg="white", font=("Arial", 12))
label_result.grid(row=7, column=0, columnspan=2)

root.mainloop()
