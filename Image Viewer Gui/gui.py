from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

window = Tk()

# Action menu
def open_image():
    filetypes = (("Image files", ".jpg;.jpeg;*.png"), ("All files", "."))
    filename = filedialog.askopenfilename(title="Select Image", filetypes=filetypes)

    if filename:
        global current_image
        current_image = Image.open(filename)
        current_image = current_image.resize((420, 420), Image.LANCZOS)
        photo = ImageTk.PhotoImage(current_image)

        label_photo.configure(image=photo)
        label_photo.image = photo

def exit_app():
    window.quit()

menu = Menu(window)
window.config(menu=menu)

action_menu = Menu(menu, tearoff=0)
action_menu.add_command(label="Open Image", command=open_image)
action_menu.add_separator()
action_menu.add_command(label="Exit", command=exit_app)

menu.add_cascade(label="Action", menu=action_menu)

#Geemetry and Title
window.geometry("820x620")
window.title("Image Viewer")

# Photo Icon
icon = PhotoImage(file='vwww.png')
window.iconphoto(True, icon)

# Windows Background
window.config(background="#110040")

# Original Photo
default_image = Image.open('orig.png')
# Resize the original image
resized_default_image = default_image.resize((420, 420))
default_photo = ImageTk.PhotoImage(resized_default_image)


# Create a frame to hold the labels
frame = Frame(window, bg='black', bd=0)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Label text of Image Viewer
label_text = Label(frame,
                   text="Image Viewer",
                   font=('Arial', 20, 'bold'),
                   fg='white',
                   bg='black')
label_text.pack(pady=(20, 0))

# Main photo label
label_photo = Label(frame,
                    image=default_photo,
                    compound='bottom')
label_photo.pack(pady=20)

# Store the current image
current_image = default_image


# Browse function
def browse():
    # Open file dialog to choose an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    # Check if a file was selected
    if file_path:
        # Open the selected image file
        image = Image.open(file_path)

        # Size of the image
        resized_image = image.resize((420, 420))
        photo = ImageTk.PhotoImage(resized_image)

        # Update the main photo with the selected photo
        label_photo.configure(image=photo)
        label_photo.image = photo

        # Update the current image
        global current_image
        current_image = image


# Browse button
browse_photo = Image.open('add.png')
browse_photo = browse_photo.resize((80, 80), Image.LANCZOS)
browse_image = ImageTk.PhotoImage(browse_photo)

browse_button = Button(window,
                       image=browse_image,
                       bg="black",
                       bd=3,
                       command=browse,
                       cursor="hand2",  # Set cursor to hand click
                       activebackground="#110040",  # Set active background color
                       relief=FLAT)  # Remove button border
browse_button.place(relx=0.1, rely=0.14, anchor=CENTER)

# Define the hover color change functions
def on_enter_browse(e):
    browse_button.configure(bg="#520b78")

def on_leave_browse(e):
    browse_button.configure(bg="black")

# Bind the Enter and Leave events to the browse button
browse_button.bind("<Enter>", on_enter_browse)
browse_button.bind("<Leave>", on_leave_browse)


# Close function
def close():
    # Close the image
    label_photo.configure(image=default_photo)
    label_photo.image = default_photo

    # Reset the current image
    global current_image
    current_image = default_image


# Close button
close_photo = Image.open('close.png')
close_photo = close_photo.resize((80, 80), Image.LANCZOS)
close_image = ImageTk.PhotoImage(close_photo)

close_button = Button(window,
                      image=close_image,
                      bg="black",
                      bd=3,
                      command=close,
                      activebackground="#8a0303",
                      cursor="hand2",  # Set cursor to hand click
                      relief=FLAT)  # Remove button border
close_button.place(relx=0.9, rely=0.14, anchor=CENTER)

# Define the hover color change functions
def on_enter_close(e):
    close_button.configure(bg="red")

def on_leave_close(e):
    close_button.configure(bg="black")

# Bind the Enter and Leave events to the close button
close_button.bind("<Enter>", on_enter_close)
close_button.bind("<Leave>", on_leave_close)


# Rotate left function
def rotate_left():
    global current_image
    if current_image != default_image:
        # Rotate the image left
        current_image = current_image.rotate(90, expand=True)

        # Resize the rotated image to maintain size
        resized_image = current_image.resize((420, 420))
        photo = ImageTk.PhotoImage(resized_image)

        # Update the main photo with the rotated image
        label_photo.configure(image=photo)
        label_photo.image = photo


# Left button
left_photo = Image.open('left.png')
left_photo = left_photo.resize((80, 80), Image.LANCZOS)
left_image = ImageTk.PhotoImage(left_photo)

left_button = Button(window,
                     image=left_image,
                     bg="black",
                     bd=3,
                     command=rotate_left,
                     cursor="hand2",  # Set cursor to hand click
                     activebackground="#110040",  # Set active background color
                     relief=FLAT)  # Remove button border
left_button.place(relx=0.1, rely=0.3, anchor=CENTER)

# Define the hover color change functions
def on_enter_left(e):
    left_button.configure(bg="#520b78")

def on_leave_left(e):
    left_button.configure(bg="black")

# Bind the Enter and Leave events to the left button
left_button.bind("<Enter>", on_enter_left)
left_button.bind("<Leave>", on_leave_left)


# Rotate right function
def rotate_right():
    global current_image
    if current_image != default_image:
        # Rotate the image right
        current_image = current_image.rotate(-90, expand=True)

        # Resize the rotated image to maintain size
        resized_image = current_image.resize((420, 420))
        photo = ImageTk.PhotoImage(resized_image)

        # Update the main photo with the rotated image
        label_photo.configure(image=photo)
        label_photo.image = photo


# Right button
right_photo = Image.open('right.png')
right_photo = right_photo.resize((80, 80), Image.LANCZOS)
right_image = ImageTk.PhotoImage(right_photo)

right_button = Button(window,
                      image=right_image,
                      bg="black",
                      bd=3,
                      command=rotate_right,
                      cursor="hand2",  # Set cursor to hand click
                      activebackground="#110040",  # Set active background color
                      relief=FLAT)  # Remove button border
right_button.place(relx=0.9, rely=0.3, anchor=CENTER)

# Define the hover color change functions
def on_enter_right(e):
    right_button.configure(bg="#520b78")

def on_leave_right(e):
    right_button.configure(bg="black")

# Bind the Enter and Leave events to the right button
right_button.bind("<Enter>", on_enter_right)
right_button.bind("<Leave>", on_leave_right)


# Next left function
def next_left():
    # Implement your functionality for the next left button here
    pass


# Next left button
next_left_photo = Image.open('nextleft.png')
next_left_photo = next_left_photo.resize((80, 80), Image.LANCZOS)
next_left_image = ImageTk.PhotoImage(next_left_photo)

next_left_button = Button(window,
                          image=next_left_image,
                          bg="black",
                          bd=3,
                          command=next_left,
                          cursor="hand2",  # Set cursor to hand click
                          activebackground="#110040",  # Set active background color
                          relief=FLAT)  # Remove button border
next_left_button.place(relx=0.1, rely=0.46, anchor=CENTER)

# Define the hover color change functions
def on_enter_next_left(e):
    next_left_button.configure(bg="#520b78")

def on_leave_next_left(e):
    next_left_button.configure(bg="black")

# Bind the Enter and Leave events to the next left button
next_left_button.bind("<Enter>", on_enter_next_left)
next_left_button.bind("<Leave>", on_leave_next_left)


# Next right function
def next_right():
    # Implement your functionality for the next right button here
    pass


# Next right button
next_right_photo = Image.open('nextright.png')
next_right_photo = next_right_photo.resize((80, 80), Image.LANCZOS)
next_right_image = ImageTk.PhotoImage(next_right_photo)

next_right_button = Button(window,
                           image=next_right_image,
                           bg="black",
                           bd=3,
                           command=next_right,
                           cursor="hand2",  # Set cursor to hand click
                           activebackground="#110040",  # Set active background color
                           relief=FLAT)  # Remove button border
next_right_button.place(relx=0.9, rely=0.46, anchor=CENTER)

# Define the hover color change functions
def on_enter_next_right(e):
    next_right_button.configure(bg="#520b78")

def on_leave_next_right(e):
    next_right_button.configure(bg="black")

# Bind the Enter and Leave events to the next right button
next_right_button.bind("<Enter>", on_enter_next_right)
next_right_button.bind("<Leave>", on_leave_next_right)


window.mainloop()
