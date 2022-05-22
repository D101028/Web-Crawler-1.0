import urllib.request as req
import bs4
import os

# 取得 html 函式
def gethtml(url): # 輸入字串網址、輸出為 BeautifulSoup 形式
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36"
    })
    with req.urlopen(request) as abc:
        data=abc.read().decode("utf-8")
    root=bs4.BeautifulSoup(data, "html.parser")
    return root

# 輸入下載目標
print("輸入下載目標")
num=input(">>>")

# 存取網頁原始碼(html)
root01=gethtml("https://www.wnacg.org/photos-index-aid-"+num+".html")

# 解析出標題
root=root01.find("div", id="bodywrap")
root=root.find("h2")
title=root.string


# 解析頁數
root=root01.find("div", class_="asTBcell uwconn")
root=str(root)
root=root.replace(root[:root.index("頁數：")+3],"")
root=int(root.replace(root[root.index("P"):],""))
# 頁數：21P
pages=root

# 確認目標
print("title: ", title)
print("pages: ",str(pages))
ch=input("still download?"+"\n[y/n]>>>")
# tell3(['y','n'],ch)
if ch=="n":
    exit()

# 創建存檔資料夾
sdir=input("輸入存檔路徑[ex.C:/Users](默認為D槽)\n>>>")
if not os.path.isdir(sdir):
    saveDir='D:/wnacg_dl/'
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)
    saveDir='D:/wnacg_dl/'+num+"_"+title+"/"
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)
else:
    saveDir=sdir+'/wnacg_dl/'
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)
    saveDir=sdir+'/wnacg_dl/'+num+"_"+title+"/"
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)

n=pages
listpages=0
while n>0:
    n-=12
    listpages+=1

x1=0
# 下載全部
for listpage in range(listpages):
    x2=str(listpage+1)
    root1=gethtml("https://www.wnacg.org/photos-index-page-"+x2+"-aid-"+num+".html")
    root1=root1.find_all("div", class_="pic_box tb")
    root1=str(root1)
    root1=root1.split(',')
    for k in root1:
        root=k[k.index('href="')+6:k.index('\n')]
        root=root[:root.index('"')]
        root=gethtml("https://www.wnacg.org/"+root)
        root=root.find("img", id="picarea")
        root=str(root)
        root="https:"+root[root.index("//img"):root.index('.jpg')+4]
        print(root)
        x1=int(x1)
        x1+=1
        x1=str(x1)
        # 單頁下載
        pturl=root
        ext=pturl.split(".")
        ext=ext[-1] # 讀取副檔名
        print("page "+x1+" downloading...")
        opener=req.build_opener()
        opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4542.2 Safari/537.36")]
        req.install_opener(opener)
        req.urlretrieve(pturl, saveDir+x1+"."+ext)
        print("page "+x1+" was downloaded")
# 下載完成，顯示路徑
print("Download completed"+"\nfile pass: "+saveDir)