import scrapy
import re
import yt_dlp as ydl
class TimarestanSpider(scrapy.Spider):
    name = 'timarestan'
    #https://t.me/troll_timarestan/20191?embed=1&mode=tme
    start_urls = []
    for i in range(21900, 22000):
        start_urls.append(f'https://t.me/troll_timarestan/{i}?embed=1&mode=tme')
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, meta={"proxy": "socks5://127.0.0.1:1819"})
    def parse(self, response):
        vpost = response.css("video::attr(src)").get()
        if vpost:
            self.log(f"Parsing : {vpost}")
            with ydl.YoutubeDL({"outtmpl": f"vids/{response.url.replace("https://t.me/troll_timarestan/","").replace("?embed=1&mode=tme","")}.%(ext)s"}) as dlr:
                dlr.download(vpost)
        else:
            style = response.css(".tgme_widget_message_photo_wrap::attr(style)").get()
            impost = re.search(r"url\('(.+?)'\)", style).group(1) if style else None
            if impost:
                self.log(f"Parsing : {impost}")
                with ydl.YoutubeDL({"outtmpl": f"vids/{response.url.replace("https://t.me/troll_timarestan/","").replace("?embed=1&mode=tme","")}.%(ext)s"}) as dlr:
                    dlr.download(impost)
            else:
                self.log(f"No media found : {response.url}")
