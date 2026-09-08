import scrapy
import re
import yt_dlp as ydl
from pathlib import Path
from diskcache import Cache
chnl : str
class TelegramSpider(scrapy.Spider):
    global chnl
    name = 'telegram'
    #https://t.me/troll_timarestan/20191?embed=1&mode=tme
    start_urls = []
    chnl = "troll_timarestan"
    for i in range(20000, 22000):
        start_urls.append(f'https://t.me/{chnl}/{i}?embed=1&mode=tme')
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, meta={"proxy": "socks5://127.0.0.1:1819"})
    def parse(self, response):
        global chnl
        id = response.url.replace("https://t.me/troll_timarestan/","").replace("?embed=1&mode=tme","")
        vpost = response.css("video::attr(src)").get()
        if vpost:
            with Cache(Path(f"datas/{chnl}")) as data:
                data.set(id, {
                    "caption": " ".join(response.css(".tgme_widget_message_text ::text").getall()).strip(),
                    "url": vpost,
                })
            self.log(f"Parsing : {vpost}")
            
            # with ydl.YoutubeDL({"outtmpl": f"vids/{response.url.replace("https://t.me/troll_timarestan/","").replace("?embed=1&mode=tme","")}.%(ext)s"}) as dlr:
            #     dlr.download(vpost)
        else:
            style = response.css(".tgme_widget_message_photo_wrap::attr(style)").get()
            impost = re.search(r"url\('(.+?)'\)", style).group(1) if style else None
            if impost:
                self.log(f"Parsing : {impost}")
                with Cache(Path(f"datas/{chnl}")) as data:
                    data.set(id, {
                        "caption" : " ".join(response.css(".tgme_widget_message_text ::text").get()),
                        "url": impost,
                    })
                # with ydl.YoutubeDL({"outtmpl": f"vids/{response.url.replace("https://t.me/troll_timarestan/","").replace("?embed=1&mode=tme","")}.%(ext)s"}) as dlr:
                #     dlr.download(impost)
            else:
                self.log(f"No media found : {response.url}")
