import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove  # pip install rembg onnxruntime

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")

        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Frame for input path
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Input Image Path:").pack(side=tk.LEFT)
        tk.Entry(input_frame, textvariable=self.input_path, width=50).pack(side=tk.LEFT)
        tk.Button(input_frame, text="Browse", command=self.browse_input).pack(side=tk.LEFT)

        # Frame for output path
        output_frame = tk.Frame(self.root)
        output_frame.pack(pady=10)

        tk.Label(output_frame, text="Output Image Path:").pack(side=tk.LEFT)
        tk.Entry(output_frame, textvariable=self.output_path, width=50).pack(side=tk.LEFT)
        tk.Button(output_frame, text="Browse", command=self.browse_output).pack(side=tk.LEFT)

        # Buttons
        tk.Button(self.root, text="Remove Background", command=self.remove_background).pack(pady=10)
        tk.Button(self.root, text="Save Image", command=self.save_image).pack(pady=10)
        tk.Button(self.root, text="Close", command=self.root.quit).pack(pady=10)

        # Canvas to display image
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack(pady=10)

    def browse_input(self):
        self.input_path.set(filedialog.askopenfilename())

    def browse_output(self):
        self.output_path.set(filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")]))

    def remove_background(self):
        input_path = self.input_path.get()
        if not input_path:
            messagebox.showerror("Error", "Please select an input image.")
            return

        try:
            input_img = Image.open(input_path)
            output_img = remove(input_img)
            self.display_image(output_img)
            self.output_img = output_img
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove background: {e}")

    def save_image(self):
        output_path = self.output_path.get()
        if not output_path:
            messagebox.showerror("Error", "Please select an output path.")
            return

        try:
            self.output_img.save(output_path)
            messagebox.showinfo("Success", "Image saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {e}")

    def display_image(self, img):
        img.thumbnail((500, 500))
        self.tk_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()

