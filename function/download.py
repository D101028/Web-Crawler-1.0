import os
import shutil
import urllib.request as req
import bs4
import zipfile
from zipfile import ZipFile as zip
import time
def zip_dir(path, root):
    os.chdir(root) # 切換程式執行的根目錄
    zf = zip(path+'.zip', 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path):
        for file_name in files:
            zf.write(os.path.join(root, file_name))
def gethtml(url): # 輸入字串網址、輸出為 BeautifulSoup 形式
	request=req.Request(url, headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36"
	})
	with req.urlopen(request) as abc:
		data=abc.read().decode("utf-8")
	root=bs4.BeautifulSoup(data, "html.parser")
	return root
async def download_and_compress(app, number, pages):
	# 創建存檔資料夾
	sdir=app.root_path+"/download"
	saveDir=sdir+'/'
	if not os.path.isdir(saveDir):
		os.mkdir(saveDir)
	# saveDir=sdir+'/nhentai_dl/'
	# if not os.path.isdir(saveDir):
	#     os.mkdir(saveDir)
	saveDir=saveDir+number+"/"
	if not os.path.isdir(saveDir):
		os.mkdir(saveDir)

	# 下載全部
	for page in range(pages):
		x1=str(page+1)
		def gethtml(url): # 輸入字串網址、輸出為 BeautifulSoup 形式
			request=req.Request(url, headers={
				"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36"
			})
			with req.urlopen(request) as abc:
				data=abc.read().decode("utf-8")
			root=bs4.BeautifulSoup(data, "html.parser")
			return root
		# 擷取單頁圖片網址
		root=gethtml("https://nhentai.net/g/"+number+"/"+x1+"/")
		root=root.find("section", id="image-container")
		root=root.img
		root=str(root)

		# 單頁下載
		pturl=root[root.index("http"):root.index('" width=')]
		ext=pturl.split(".")
		ext=ext[-1] # 讀取副檔名
		print("page "+x1+" downloading...")
		req.urlretrieve(pturl, saveDir+x1+"."+ext)
		print("page "+x1+" was downloaded")
		
		page+=1
	
	# 壓縮檔案
	path=number
	root=app.root_path+"/download/"
	zip_dir(path, root)
def get_imformation(number):
	# 輸入下載目標
	num=number

	# 存取網頁原始碼(html)
	root01=gethtml("https://nhentai.net/g/"+num+"/")
	# 解析出標題
	root=root01.find("h2", class_="title")
	root021=root.find("span", class_="before")
	root022=root.find("span", class_="pretty")
	root023=root.find("span", class_="after")
	root021=str(root021.string)
	root022=str(root022.string)
	root023=str(root023.string)
	if root021=="None":
		root021=""
	if root022=="None":
		root022=""
	if root023=="None":
		root023=""
	title=root021+root022+root023

	# 解析頁數
	global pages
	pages=root01.find_all("div", class_="thumb-container")
	pages=len(pages)
	global message_t
	global message_n
	global message_p
	message_t="name: "+title
	message_n="number: "+num
	message_p="page: "+str(pages)