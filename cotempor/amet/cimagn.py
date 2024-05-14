import tkinter as tk

def hide():
    """Hides the current window."""
    root = tk.Tk()
    root.withdraw()
    root.mainloop()

# Call the function to hide the window
hide()
