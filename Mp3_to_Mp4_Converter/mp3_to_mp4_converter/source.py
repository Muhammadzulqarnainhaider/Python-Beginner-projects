import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import moviepy.editor as mp

class VideoToAudioConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video to Audio Converter")
        self.geometry("500x200")


        self.create_widgets()

    def create_widgets(self):
        # Video file selection
        self.video_path_label = tk.Label(self, text="Select the video file to convert:")
        self.video_path_label.pack()
        self.video_path_entry = tk.Entry(self, width=50)
        self.video_path_entry.pack()
        self.video_path_button = tk.Button(self, text="Browse...", command=self.browse_video_file)
        self.video_path_button.pack()

        # Audio file save location
        self.save_path_label = tk.Label(self, text="Select where to save the converted audio file:")
        self.save_path_label.pack()
        self.save_path_entry = tk.Entry(self, width=50)
        self.save_path_entry.pack()
        self.save_path_button = tk.Button(self, text="Browse...", command=self.browse_save_location)
        self.save_path_button.pack()

        # Conversion buttons
        self.convert_button = tk.Button(self, text="Convert", command=self.convert_video_to_audio)
        self.convert_button.pack()
        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_button.pack()

    def browse_video_file(self):
        video_file = askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv")])
        if video_file:
            self.video_path_entry.insert(0, video_file)

    def browse_save_location(self):
        save_location = asksaveasfilename(filetypes=[("Audio Files", "*.mp3")], defaultextension=".mp3")
        if save_location:
            self.save_path_entry.insert(0, save_location)

    def convert_video_to_audio(self):
        video_path = self.video_path_entry.get()
        save_path = self.save_path_entry.get()

        if not video_path or not save_path:
            tk.messagebox.showerror("Error", "Please select video file and save location.")
            return

        try:
            video = mp.VideoFileClip(video_path)
            audio = video.audio
            audio.write_audiofile(save_path, codec='mp3')
            tk.messagebox.showinfo("Conversion Complete", "Video converted to audio successfully.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = VideoToAudioConverter()
    app.mainloop()
