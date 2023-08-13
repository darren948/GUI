from tkinter import *
from tkinter import filedialog
import os
from tkinter import Tk, Button, FLAT
from tkinter.simpledialog import askstring
from PIL import ImageTk, Image, ImageDraw
from PIL import ImageFont


window = Tk()

# ACTION MENU
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

def select_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")

    if folder_path:
        global folder_images, current_image_index, current_image
        folder_images = []
        current_image_index = 0

        # Collect image files from the selected folder
        image_extensions = (".jpg", ".jpeg", ".png")
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(image_extensions):
                image_path = os.path.join(folder_path, file_name)
                image = Image.open(image_path)
                folder_images.append(image)

        # Set the current image to the first image in the folder
        if folder_images:
            current_image = folder_images[0]
            current_image = current_image.resize((420, 420), Image.LANCZOS)
            photo = ImageTk.PhotoImage(current_image)

            label_photo.configure(image=photo)
            label_photo.image = photo

def exit_app():
    window.quit()

def apply_black_white_filter():
    global current_image
    if current_image:
        # Apply black and white filter to the image
        current_image = current_image.convert("L")

        # Resize the filtered image to maintain size
        resized_image = current_image.resize((420, 420))
        photo = ImageTk.PhotoImage(resized_image)

        # Update the main photo with the filtered image
        label_photo.configure(image=photo)
        label_photo.image = photo

def apply_contrast_filter():
    global current_image
    if current_image:
        # Apply contrast filter to the image
        current_image = current_image.convert("RGB")
        current_image = current_image.point(lambda p: p * 1.5)

        # Resize the filtered image to maintain size
        resized_image = current_image.resize((420, 420))
        photo = ImageTk.PhotoImage(resized_image)

        # Update the main photo with the filtered image
        label_photo.configure(image=photo)
        label_photo.image = photo

def apply_brightness_filter():
    global current_image
    if current_image:
        # Apply brightness filter to the image
        current_image = current_image.convert("RGB")
        current_image = current_image.point(lambda p: p + 50)

        # Resize the filtered image to maintain size
        resized_image = current_image.resize((420, 420))
        photo = ImageTk.PhotoImage(resized_image)

        # Update the main photo with the filtered image
        label_photo.configure(image=photo)
        label_photo.image = photo

def save_image():
    global current_image
    if current_image:
        filetypes = (("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("All files", "*.*"))
        filename = filedialog.asksaveasfilename(title="Save Image As", filetypes=filetypes, defaultextension=".png")
        if filename:
            current_image.save(filename)

menu = Menu(window)
window.config(menu=menu)

action_menu = Menu(menu)
menu.add_cascade(label="Actions", menu=action_menu)
action_menu.add_command(label="Open Image", command=open_image)
action_menu.add_command(label="Select Folder", command=select_folder)
action_menu.add_command(label="Save Image", command=save_image)
action_menu.add_separator()

filter_menu = Menu(action_menu)
action_menu.add_cascade(label="Apply Filters", menu=filter_menu)
filter_menu.add_command(label="Black and White", command=apply_black_white_filter)
filter_menu.add_command(label="Contrast", command=apply_contrast_filter)
filter_menu.add_command(label="Brightness", command=apply_brightness_filter)

action_menu.add_command(label="Exit", command=exit_app)

# GEOMETRY AND TITLE
window.geometry("820x620")
window.title("Image Viewer")

# PHOTO ICON
icon = PhotoImage(file='vwww.png')
window.iconphoto(True, icon)

# WINDOWS BACKGROUND
window.config(background="black")

# ORIG PHOTO
default_image = Image.open('orig.png')
# Resize the original image
resized_default_image = default_image.resize((420, 420))
default_photo = ImageTk.PhotoImage(resized_default_image)


#FRAME OF LABEL
frame = Frame(window, bg='black', bd=1)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#LABEL TEXT OF IMAGE VIEWER
label_text = Label(frame,
                   text="Image Viewer",
                   font=('Arial', 20, 'bold'),
                   fg='white',
                   bg='black')
label_text.pack(pady=(20, 0))

# MAIN PHOTO LABEL
label_photo = Label(frame,
                    image=default_photo,
                    compound='bottom')
label_photo.pack(pady=20)

# Store the current image
current_image = default_image

# Store the folder images and current image index
folder_images = []
current_image_index = 0


# BROWSE BUTTON FUNCTION
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

        # Clear the folder images and current image index
        global folder_images, current_image_index
        folder_images = []
        current_image_index = 0


# BROWSE BUTTON
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


# FOLDER SELECT BUTTON FUNCTION
def select_folder_button():
    select_folder()

# FOLDER SELECT BUTTON
folder_photo = Image.open('folder.png')
folder_photo = folder_photo.resize((80, 80), Image.LANCZOS)
folder_image = ImageTk.PhotoImage(folder_photo)

folder_button = Button(window,
                       image=folder_image,
                       bg="black",
                       bd=3,
                       command=select_folder_button,
                       cursor="hand2",  # Set cursor to hand click
                       activebackground="#110040",  # Set active background color
                       relief=FLAT)  # Remove button border
folder_button.place(relx=0.1, rely=0.32, anchor=CENTER)

# Define the hover color change functions
def on_enter_folder(e):
    folder_button.configure(bg="#520b78")

def on_leave_folder(e):
    folder_button.configure(bg="black")

# Bind the Enter and Leave events to the folder button
folder_button.bind("<Enter>", on_enter_folder)
folder_button.bind("<Leave>", on_leave_folder)

# CLOSE FUNCTION
def close():
    # Close the image
    label_photo.configure(image=default_photo)
    label_photo.image = default_photo

    # Reset the current image
    global current_image
    current_image = default_image

    # Clear the folder images and current image index
    global folder_images, current_image_index
    folder_images = []
    current_image_index = 0


# CLOSE BUTTON
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

# FLIP FUNCTION
def flip():
    global current_image
    if current_image != default_image:
        # Flip the image horizontally
        current_image = current_image.transpose(Image.FLIP_LEFT_RIGHT)

        # Resize the flipped image to maintain size
        resized_image = current_image.resize((420, 420))
        photo = ImageTk.PhotoImage(resized_image)

        # Update the main photo with the flipped image
        label_photo.configure(image=photo)
        label_photo.image = photo

# FLIP BUTTON
flip_photo = Image.open('flip.png')
flip_photo = flip_photo.resize((80, 80), Image.LANCZOS)
flip_image = ImageTk.PhotoImage(flip_photo)

flip_button = Button(window,
                     image=flip_image,
                     bg="black",
                     bd=3,
                     command=flip,
                     cursor="hand2",  # Set cursor to hand click
                     activebackground="#110040",  # Set active background color
                     relief=FLAT)  # Remove button border
flip_button.place(relx=0.9, rely=0.32, anchor=CENTER)

# Define the hover color change functions
def on_enter_flip(e):
    flip_button.configure(bg="#520b78")

def on_leave_flip(e):
    flip_button.configure(bg="black")

# Bind the Enter and Leave events to the flip button
flip_button.bind("<Enter>", on_enter_flip)
flip_button.bind("<Leave>", on_leave_flip)


# NEXT LEFT BUTTON FUNCTION
def next_left():
    global current_image_index
    if current_image_index > 0:
        current_image_index -= 1
        load_current_image()


# NEXT LEFT BUTTON
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
next_left_button.place(relx=0.1, rely=0.50, anchor=CENTER)

# Define the hover color change functions
def on_enter_next_left(e):
    next_left_button.configure(bg="#520b78")

def on_leave_next_left(e):
    next_left_button.configure(bg="black")

# Bind the Enter and Leave events to the next left button
next_left_button.bind("<Enter>", on_enter_next_left)
next_left_button.bind("<Leave>", on_leave_next_left)


# NEXT RIGHT BUTTON FUNCTION
def next_right():
    global current_image_index, folder_images
    if current_image_index < len(folder_images) - 1:
        current_image_index += 1
        load_current_image()


# NEXT RIGHT BUTTON
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
next_right_button.place(relx=0.9, rely=0.50, anchor=CENTER)

# Define the hover color change functions
def on_enter_next_right(e):
    next_right_button.configure(bg="#520b78")

def on_leave_next_right(e):
    next_right_button.configure(bg="black")

# Bind the Enter and Leave events to the next right button
next_right_button.bind("<Enter>", on_enter_next_right)
next_right_button.bind("<Leave>", on_leave_next_right)

# DOWNLOAD BUTTON FUNCTION
def download_image():
    global current_image
    if current_image:
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if filename:
            current_image.save(filename)

# DOWNLOAD BUTTON
download_photo = Image.open('download.png')
download_photo = download_photo.resize((80, 80), Image.LANCZOS)
download_image_icon = ImageTk.PhotoImage(download_photo)

download_button = Button(window,
                         image=download_image_icon,
                         bg="black",
                         bd=3,
                         command=download_image,
                         cursor="hand2",  # Set cursor to hand click
                         activebackground="#110040",  # Set active background color
                         relief=FLAT)  # Remove button border
download_button.place(relx=0.1, rely=0.68, anchor=CENTER)

# Define the hover color change functions
def on_enter_download(e):
    download_button.configure(bg="#520b78")

def on_leave_download(e):
    download_button.configure(bg="black")

# Bind the Enter and Leave events to the download button
download_button.bind("<Enter>", on_enter_download)
download_button.bind("<Leave>", on_leave_download)

# Define the add_text() function
def add_text():
    global current_image

    if current_image:
        # Get the text from the user
        text = askstring("Add Text", "Enter the text:")

        # Check if the user entered text
        if text:
            # Create a text overlay on the image
            image_with_text = current_image.copy()
            draw = ImageDraw.Draw(image_with_text)

            # Set the font properties
            font_size = 30
            font = ImageFont.truetype("arial.ttf", font_size)

            # Calculate the text position and size using textbbox
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = (image_with_text.width - text_width) // 2
            text_y = (image_with_text.height - text_height) // 2

            # Draw the text on the image
            draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

            # Resize the image with the text overlay to maintain size
            resized_image = image_with_text.resize((420, 420))
            photo = ImageTk.PhotoImage(resized_image)

            # Update the main photo with the image containing the text overlay
            label_photo.configure(image=photo)
            label_photo.image = photo

# Define the text_button() function
def text_button():
    add_text()

# Load the image for the text button
text_photo = Image.open('text.png')
text_photo = text_photo.resize((80, 80), Image.LANCZOS)
text_image = ImageTk.PhotoImage(text_photo)

# Create the text button
text_button = Button(window,
                     image=text_image,
                     bg="black",
                     bd=3,
                     command=text_button,
                     cursor="hand2",
                     activebackground="#110040",
                     relief=FLAT)
text_button.place(relx=0.9, rely=0.68, anchor="center")


# ROTATE LEFT BUTTON FUNCTION
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

# Define the hover color change functions
def on_enter_left(e):
    text_button.configure(bg="#520b78")

def on_leave_left(e):
    text_button.configure(bg="black")

# Bind the Enter and Leave events to the left button
text_button.bind("<Enter>", on_enter_left)
text_button.bind("<Leave>", on_leave_left)


# ROTATE LEFT BUTTON
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
left_button.place(relx=0.1, rely=0.86, anchor=CENTER)

# Define the hover color change functions
def on_enter_left(e):
    left_button.configure(bg="#520b78")

def on_leave_left(e):
    left_button.configure(bg="black")

# Bind the Enter and Leave events to the left button
left_button.bind("<Enter>", on_enter_left)
left_button.bind("<Leave>", on_leave_left)


# ROTATE RIGHT BUTTON FUNCTION
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


# ROTATE RIGHT BUTTON
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
right_button.place(relx=0.9, rely=0.86, anchor=CENTER)

# Define the hover color change functions
def on_enter_right(e):
    right_button.configure(bg="#520b78")

def on_leave_right(e):
    right_button.configure(bg="black")

# Bind the Enter and Leave events to the right button
right_button.bind("<Enter>", on_enter_right)
right_button.bind("<Leave>", on_leave_right)

# Load the current image from the folder images
def load_current_image():
    global current_image, current_image_index, folder_images

    current_image = folder_images[current_image_index]
    current_image = current_image.resize((420, 420), Image.LANCZOS)
    photo = ImageTk.PhotoImage(current_image)

    label_photo.configure(image=photo)
    label_photo.image = photo


window.mainloop()
