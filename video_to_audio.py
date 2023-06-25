import moviepy.editor
from tkinter.filedialog import *

vid = "Dekha Tenu Pehli Pehli Baar Ve _ Random Jam _ Acoustic Cover _ Mubeen Butt(720P_HD).mp4"
video = moviepy.editor.VideoFileClip(vid)
aud = video.audio
aud.write_audiofile("audio.mp3")

print("Task completed")



