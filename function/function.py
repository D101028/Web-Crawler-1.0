from flask import Flask, render_template
import json
with open("./setting/setting.json", mode="rb") as file:
    set_data=json.loads(file.read())


# return progress (大小(MB)+進度)
def call_back(blocknum, blocksize, totalsize):
    '''req.urlretrieve(url, 'D:/test.mp4', call_back)
    回調函數
    @blocknum: 已經下載的數據塊
    @blocksize: 數據塊的大小
    @totalsize: 遠程文件的大小
    '''
    size=int(totalsize/1048576*100)/100
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    if percent==100:
        print("size:"+str(size)+" MB "+"download "+"%.2f%%"%+percent) # 完成後避免被覆蓋
    else:
        print("size:"+str(size)+" MB "+"download "+"%.2f%%"%+percent, end="\r")

def formatFloat(num):
    return '{:.2f}'.format(num)

class GetHtml():
    """urllibRequest, _requests, seleniumChrome"""
    def __init__():
        pass
    def urllibRequest(url, headers=None):
        """
        @url: url
        @headers: for example, headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36',
            'referer' : 'https://example.com'
        }
        """
        import urllib.request
        if headers != None:
            request=urllib.request.Request(url, headers=headers)
        else:
            request=urllib.request.Request(url)
        with urllib.request.urlopen(request) as file:
            data = file.read().decode("utf-8")
        return data
    def _requests(url, headers=None):
        """
        @url: url
        @headers: for example, headers = {
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36',
            'referer' : 'https://example.com'
        }
        """
        import requests
        if headers != None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url)
        response.encoding = "utf-8"
        return response.text
    def seleniumChrome(url, selenium_driver_path, headless=False):
        """get html by selenium (Chrome)
        @url: url
        @selenium_driver_path: the path of "chromedriver.exe"
        @headless: whether to hide the programming interface
        """
        from selenium import webdriver as web
        if headless==True:
            option = web.ChromeOptions()
            option.add_argument("headless")
            driver = web.Chrome(selenium_driver_path, chrome_options=option)
        else:
            driver = web.Chrome(selenium_driver_path)
        driver.get(url)
        html=driver.page_source()
        return html


class Download():
    def __init__():
        pass
    def urllibUrlretrieve(url, filename, headers=None, callback=False):
        """
        @url: url
        @filename: download file path and name and extention
        @headers: for example, headers = [
            ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36'),
            ('referer', 'https://example.com')
        ]
        @callback: whether print the progress of downloading
        """
        import urllib
        if headers != None:
            opener=urllib.request.build_opener()
            opener.addheaders=headers
            urllib.request.install_opener(opener)

        if callback == True:
            urllib.request.urlretrieve(url, filename, call_back)
        else:
            urllib.request.urlretrieve(url, filename)

    def urllibUrlopen(url, filename, headers=None, callback=False):
        """
        @url: url
        @filename: download file path and name and extention
        @headers: for example, headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36',
            'referer' : 'https://example.com'
        }
        @callback: (not available) whether print the progress of downloading
        """
        import urllib
        if headers != None:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as file:
                data = file.read()
                with open(filename, 'wb') as f:
                    f.write(data)
                    f.close()
        else:
            with urllib.request.urlopen(url) as file:
                data = file.read()
                with open(filename, "wb") as f:
                    f.write(data)
    def _requests(url, filename, headers=None, callback=False):
        """
        @url: url
        @headers: for example, headers = {
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36',
            'referer' : 'https://example.com'
        }
        @callback: (not available) whether print the progress of downloading
        """
        import requests
        if headers != None:
            r = requests.get(url, stream=True, headers=headers)
        else:
            r = requests.get(url, stream=True)
        if callback:
            import time
            length = float(r.headers['content-length'])
            with open(filename, 'wb') as f:
                count = 0
                count_tmp = 0
                time1 = time.time()
                for chunk in r.iter_content(chunk_size = 512):
                    if chunk:
                        f.write(chunk)
                        count += len(chunk)
                        if time.time() - time1 > 0.05:
                            p = count / length * 100
                            speed = (count - count_tmp) / 1024 / 1024 / 0.05 # 時間太短速度會跳太快
                            count_tmp = count
                            print(filename + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S', end="\r")
                            time1 = time.time()
            print(filename + ': 100.00%             ' + "\n")
        else:
            with open(filename, mode="wb") as file:
                file.write(r.content)





# async def signal_judge(signal):
#     print(signal)
#     if signal!=set_data["signal"]:
#         return "window.location.href='/'"
#     else:
#         return render_template("main.html", right_signal=True)