import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

class VideoProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyseur de Vidéo MP4")

        self.video_path = None
        self.cap = None
        self.images = []
        self.is_playing = False

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Bouton pour uploader une vidéo
        self.btn_upload = ttk.Button(self.root, text="Uploader une vidéo MP4", command=self.upload_video)
        self.btn_upload.pack(pady=10)

        # Labels pour les informations
        self.lbl_status = tk.Label(self.root, text="Aucune vidéo chargée.", fg="red")
        self.lbl_status.pack()

        self.lbl_frames = tk.Label(self.root, text="Nombre de frames : --")
        self.lbl_frames.pack()

        self.lbl_fps = tk.Label(self.root, text="FPS : --")
        self.lbl_fps.pack()

        self.lbl_duration = tk.Label(self.root, text="Durée : --")
        self.lbl_duration.pack()

        # Boutons de lecture et extraction
        self.btn_play = ttk.Button(self.root, text="Lire la vidéo", command=self.play_video, state=tk.DISABLED)
        self.btn_play.pack(pady=5)

        self.btn_extract = ttk.Button(self.root, text="Extraire les images", command=self.extract_images, state=tk.DISABLED)
        self.btn_extract.pack(pady=5)

        self.btn_save_images = ttk.Button(self.root, text="Enregistrer les images extraites", command=self.save_images, state=tk.DISABLED)
        self.btn_save_images.pack(pady=5)

        # Zone pour afficher les images extraites
        self.frame_images = tk.Frame(self.root)
        self.canvas_images = tk.Canvas(self.frame_images)
        self.scrollbar = ttk.Scrollbar(self.frame_images, orient=tk.HORIZONTAL, command=self.canvas_images.xview)
        self.canvas_images.configure(xscrollcommand=self.scrollbar.set)
        self.canvas_images.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.frame_images.pack(pady=10)

        # Zone pour afficher un graphique
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(pady=10)

    def upload_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4"), ("All Files", "*.*")])
        if not self.video_path:
            return

        # Charger la vidéo
        self.cap = cv2.VideoCapture(self.video_path)
        if not self.cap.isOpened():
            self.lbl_status.config(text="Erreur : Impossible d'ouvrir la vidéo.")
            return

        # Informations sur la vidéo
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.duration = self.total_frames / self.fps

        self.lbl_status.config(text=f"Vidéo chargée : {self.video_path}")
        self.lbl_frames.config(text=f"Nombre de frames : {self.total_frames}")
        self.lbl_fps.config(text=f"FPS : {self.fps}")
        self.lbl_duration.config(text=f"Durée : {self.duration:.2f} secondes")

        self.btn_play.config(state=tk.NORMAL)
        self.btn_extract.config(state=tk.NORMAL)

    def play_video(self):
        if not self.cap or not self.video_path:
            return

        self.is_playing = True
        cv2.namedWindow("Lecture de la vidéo", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Lecture de la vidéo", 800, 600)

        while self.cap.isOpened() and self.is_playing:
            ret, frame = self.cap.read()
            if not ret:
                break

            cv2.imshow("Lecture de la vidéo", frame)
            key = cv2.waitKey(25)
            if key == ord('q'):
                break

        cv2.destroyWindow("Lecture de la vidéo")

    def stop_video(self):
        self.is_playing = False

    def extract_images(self):
        if not self.cap or not self.video_path:
            return

        self.images = []
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        for i in range(0, self.total_frames, 2 * self.fps):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.images.append(frame)

        self.lbl_status.config(text="Images extraites.")
        self.btn_save_images.config(state=tk.NORMAL)
        self.display_images()
        self.plot_brightness()

    def display_images(self):
        for widget in self.canvas_images.winfo_children():
            widget.destroy()

        x_offset = 0
        for img in self.images:
            img = Image.fromarray(img)
            img.thumbnail((150, 150))
            img_tk = ImageTk.PhotoImage(img)

            lbl_img = tk.Label(self.canvas_images, image=img_tk)
            lbl_img.image = img_tk
            lbl_img.place(x=x_offset, y=0)
            x_offset += 160

        self.canvas_images.config(scrollregion=(0, 0, x_offset, 150))

    def plot_brightness(self):
        brightness_values = []

        for img in self.images:
            grayscale = cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)
            brightness_values.append(grayscale.mean())

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(brightness_values, marker='o')
        ax.set_title("Variation de la luminosité")
        ax.set_xlabel("Images (2s d'intervalle)")
        ax.set_ylabel("Luminosité moyenne")
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, self.graph_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def save_images(self):
        if not self.images:
            return

        folder_path = filedialog.askdirectory()
        if not folder_path:
            return

        for idx, img in enumerate(self.images):
            img = Image.fromarray(img)
            img.save(os.path.join(folder_path, f"frame_{idx}.jpg"))

        self.lbl_status.config(text="Images enregistrées avec succès.")

# Lancer l'application
root = tk.Tk()
app = VideoProcessorApp(root)
root.mainloop()








###_________________________ Version Simple________________ ######

# import tkinter as tk
# from tkinter import filedialog
# from tkinter import ttk
# import cv2
# from PIL import Image, ImageTk

# def process_video():
#     file_path = filedialog.askopenfilename(
#         filetypes=[("MP4 Files", "*.mp4"), ("All Files", "*.*")]
#     )
#     if not file_path:
#         return
    
#     # Charger la vidéo avec OpenCV
#     cap = cv2.VideoCapture(file_path)
#     if not cap.isOpened():
#         lbl_status.config(text="Erreur : Impossible d'ouvrir la vidéo.")
#         return
    
#     # Obtenir des informations sur la vidéo
#     total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#     duration = total_frames / fps

#     lbl_status.config(text=f"Vidéo chargée : {file_path}")
#     lbl_frames.config(text=f"Nombre de frames : {total_frames}")
#     lbl_fps.config(text=f"FPS : {fps}")
#     lbl_duration.config(text=f"Durée : {duration:.2f} secondes")

#     # Afficher une image toutes les 2 secondes
#     images = []
#     for i in range(0, total_frames, 2 * fps):
#         cap.set(cv2.CAP_PROP_POS_FRAMES, i)
#         ret, frame = cap.read()
#         if ret:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             images.append(frame)
    
#     # Libérer la vidéo
#     cap.release()

#     # Afficher les images dans l'interface
#     display_images(images)

# def display_images(images):
#     for widget in frame_images.winfo_children():
#         widget.destroy()
    
#     for img in images:
#         img = Image.fromarray(img)
#         img.thumbnail((200, 200))  # Redimensionner l'image pour l'affichage
#         img_tk = ImageTk.PhotoImage(img)
#         lbl_img = tk.Label(frame_images, image=img_tk)
#         lbl_img.image = img_tk  # Préserver la référence pour éviter le garbage collection
#         lbl_img.pack(side=tk.LEFT, padx=5, pady=5)

# # Interface Tkinter
# root = tk.Tk()
# root.title("Analyseur de Vidéo MP4")

# # Widgets
# btn_upload = ttk.Button(root, text="Uploader une vidéo MP4", command=process_video)
# btn_upload.pack(pady=10)

# lbl_status = tk.Label(root, text="Aucune vidéo chargée.", fg="red")
# lbl_status.pack()

# lbl_frames = tk.Label(root, text="Nombre de frames : --")
# lbl_frames.pack()

# lbl_fps = tk.Label(root, text="FPS : --")
# lbl_fps.pack()

# lbl_duration = tk.Label(root, text="Durée : --")
# lbl_duration.pack()

# frame_images = tk.Frame(root)
# frame_images.pack(pady=10)

# # Lancer l'application
# root.mainloop()
