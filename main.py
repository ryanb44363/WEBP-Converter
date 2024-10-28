import os
from tkinter import Tk, Label, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageOps

# Define the valid image file extensions
VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'}

def convert_to_webp(file_path):
    """
    Convert the image at file_path to WebP format.
    """
    try:
        img = Image.open(file_path)
        # Apply EXIF orientation if available to ensure correct orientation
        img = ImageOps.exif_transpose(img)
        webp_path = os.path.splitext(file_path)[0] + ".webp"
        img.save(webp_path, "webp")
        return webp_path
    except Exception as e:
        print(f"Error converting {file_path} to WebP: {e}")
        return None

def handle_files(event):
    """
    Handle the dropped files for conversion.
    """
    files = root.tk.splitlist(event.data)
    converted_files = []
    for file_path in files:
        # Check if the file is an image and has a valid extension
        if os.path.isfile(file_path) and os.path.splitext(file_path.lower())[1] in VALID_EXTENSIONS:
            webp_path = convert_to_webp(file_path)
            if webp_path:
                converted_files.append(webp_path)
    
    if converted_files:
        messagebox.showinfo("Conversion Complete", f"Converted files:\n" + "\n".join(converted_files))
    else:
        messagebox.showwarning("No Valid Images", "No valid image files were converted. Ensure the files are in supported formats.")

# Set up the main application window
root = TkinterDnD.Tk()
root.title("Image to WebP Converter")
root.geometry("400x200")
root.resizable(False, False)

# Add drag-and-drop label
label = Label(root, text="Drag and drop image files here", font=("Helvetica", 14), padx=10, pady=50)
label.pack(expand=True)

# Bind drop event
root.drop_target_register(DND_FILES)
root.dnd_bind("<<Drop>>", handle_files)

# Run the main loop
root.mainloop()
