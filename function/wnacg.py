from mymodules.crawler import Get

async def download_all(num):
    url = F"https://www.wnacg.org/photos-index-aid-{num}.html"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36"
    }
    html_data = Get.GetHtml.urllibRequest(url=url, headers=headers)
