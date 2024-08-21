from pytube import YouTube
import scrapy


class YoutubespiderSpider(scrapy.Spider):
    name = "youtubespider"
    # allowed_domains = ["youtube.com"]

    def start_requests(self):
        url = "https://www.youtube.com/watch?v=wQDklcWKzRA"
        yield scrapy.Request(url)

    async def parse(self, response):

        ytres = YouTube(response.url)
        print(ytres.author)
        print(ytres.age_restricted)
        print(ytres.title)
        # ytres.streaming_data
        video = ytres.streams
        # ytres.streams.filter(progressive=True, file_extension="mp4").order_by(
        #     "resolution"
        # ).desc().first().download()
        # print(type(video))
        # try:
        #     # video.download("video")
        # except:
        #     print("error")
        # print("**********************************")
