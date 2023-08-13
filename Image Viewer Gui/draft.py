import tkinter as tk
# Create the main window
root = tk.Tk()
# Add a label to the main window
label = tk.Label(root, text="Hello, world!")
label.pack()
# Add a button to the main window
button = tk.Button(root, text="Click Me")
button.pack()
# Start the main loop
root.mainloop()