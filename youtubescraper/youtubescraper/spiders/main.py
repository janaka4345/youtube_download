# from pytube import YouTube
from pytube import YouTube

url = "https://www.youtube.com/watch?v=wQDklcWKzRA"

ytres = YouTube(url)
print(ytres.author)
print(ytres.age_restricted)
print(ytres.title)
# ytres.streaming_data
video = ytres.streams
# ytres.streams.filter(progressive=True, file_extension="mp4").order_by(
#     "resolution"
# ).desc().first().download()
# print(type(video))
try:
    video.download("video")
except:
    print("error")
print("**********************************")
