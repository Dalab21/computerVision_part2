import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class VideoCaptureApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        self.vid = cv2.VideoCapture(self.video_source)
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.btn_snapshot = ttk.Button(window, text="Capture", command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.btn_start_stop = ttk.Button(window, text="Start/Stop", command=self.start_stop)
        self.btn_start_stop.pack(anchor=tk.CENTER, expand=True)

        self.btn_change_source = ttk.Button(window, text="Change Source", command=self.change_source)
        self.btn_change_source.pack(anchor=tk.CENTER, expand=True)

        self.progress = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(anchor=tk.CENTER, expand=True)

        self.label_captures = tk.Label(window, text="Captures: 0")
        self.label_captures.pack(anchor=tk.CENTER, expand=True)

        self.captures = 0
        self.streaming = True

        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.vid.read()
        if ret:
            self.captures += 1
            self.label_captures.config(text=f"Captures: {self.captures}")
            cv2.imwrite(f"frame-{self.captures}.jpg", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.progress['value'] = 0
            self.window.update_idletasks()
            for i in range(100):
                self.progress['value'] += 1
                self.window.update_idletasks()
                self.window.after(10)

    def start_stop(self):
        self.streaming = not self.streaming
        if self.streaming:
            self.update()

    def change_source(self):
        self.streaming = False
        self.vid.release()
        new_source = tk.simpledialog.askstring("Change Source", "Enter new video source (0 for webcam or file path):")
        try:
            self.video_source = int(new_source)
        except ValueError:
            self.video_source = new_source
        self.vid = cv2.VideoCapture(self.video_source)
        self.streaming = True
        self.update()

    def update(self):
        if self.streaming:
            ret, frame = self.vid.read()
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.window.after(self.delay, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

def main():
    root = tk.Tk()
    app = VideoCaptureApp(root, "Video Capture")

if __name__ == "__main__":
    main()
