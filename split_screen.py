from moviepy.editor import *

vid_1 = VideoFileClip("_shorts 1 min reminder from hoblos(1080P_HD).mp4").subclip(00,10)
vid_2 = VideoFileClip("Change your Life Before it_s too Late _ Mohamed Hoblos(720P_HD).mp4").subclip(10,20)
vid_3 = VideoFileClip("doraemon new episode 2019__Doraemon latest episodes in hindi__doraemon__cartoon tv__(360P).mp4").subclip(00,10)
vid_4 = VideoFileClip("Doraemon New Episodes in Hindi _ without zoom effect _ Doreamon in hindi _Urdu _ Doreamon Hungama(360P).mp4").subclip(00,10)


comb = clips_array([[vid_1, vid_2], [vid_3, vid_4]])

comb.write_videofile("split.mp4")
print("task complete successfully")