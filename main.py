import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageDraw
from PIL import ImageFont
def upload():
    filename = filedialog.askopenfilename(filetypes=[("Obrazy", "*.*")])
    if filename:
        image = Image.open(filename)
        image = image.resize((400, 300))
        zdjecie.image_path = filename
        photo = ImageTk.PhotoImage(image)
        zdjecie.config(image=photo)
        zdjecie.image = photo
def save():
    text = watermark_entry.get()
    image = Image.open(zdjecie.image_path)
    image = image.resize((400, 300))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 40)
    draw.text((180, 130), text, fill="black", font=font)
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")])
    if save_path:
        image.save(save_path)
        print(f"Image saved: {save_path}")
window = tkinter.Tk()
window.title("Watermark App")
window.config(padx=100, pady=100)
window.resizable(False, False)
zdjecie = tkinter.Label(window)
zdjecie.grid(row=0, column=0, columnspan=2, pady=10)
watermark_label = tkinter.Label(window, text="Watermark:", font=("Arial", 14))
watermark_label.grid(row=1, column=0, sticky="e", padx=5)
watermark_entry = tkinter.Entry(window, width=30)
watermark_entry.grid(row=1, column=1, padx=5, pady=5)
save_button = tkinter.Button(window, text="Save", command=save)
save_button.grid(row=1, column=2, padx=5, pady=5)
upload_button = tkinter.Button(window, text="Upload photo", command=upload)
upload_button.grid(row=2, column=0, columnspan=2, pady=10)
window.mainloop()