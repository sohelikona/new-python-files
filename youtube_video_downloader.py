from pytube import YouTube


# url = 'https://www.youtube.com/watch?v=-2HRe9Q_qyk'
# my_video = YouTube(url)

# print(" Video title")
# print(my_video.title)

# print("Thumbnail Image")
# print(my_video.thumbnail_url)


# print("Downloading video")

# my_video = my_video.streams.get_highest_resolution()

# my_video.download()




link = "https://www.youtube.com/watch?v=EAYlckSaviI&t=214s"
youtube_1 = YouTube(link)

print(youtube_1.title)