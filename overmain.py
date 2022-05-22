from flask import Flask, send_from_directory, render_template, request, redirect, url_for
# import random
import os
import shutil
import urllib.request as req
import bs4
import zipfile
from zipfile import ZipFile as zip
from function import download as dl

app=Flask(__name__, static_folder='ico/')

@app.route('/', methods=['POST','GET'])
def home():
	if os.path.isdir(app.root_path+"/download"):
		shutil.rmtree(app.root_path+"/download")
	if request.method =='POST':
		if request.values['send']=='OK':
			return redirect(url_for('download'))
	return render_template('index.html')


@app.route('/download/', methods=['GET','POST'])
def download():
	if request.method =='POST':
		if request.values['send']=='送出':
			global number
			number=request.values.get('user')
			dl.get_imformation(number)
			return render_template("dl-page.html", message_t=dl.message_t, message_n=dl.message_n, message_p=dl.message_p)
	return render_template("dl-page.html")

@app.route('/download/loading/')
def dling():
	ToF=os.path.isfile(app.root_path+"/download/"+number+'.zip')
	if ToF:
		return send_from_directory(app.root_path+"/download", number+'.zip', as_attachment=True)
	else:
		dl.download_and_compress(app, number, dl.pages)
		return send_from_directory(app.root_path+"/download", number+'.zip', as_attachment=True)

		

if __name__=="__main__": 
    app.run(debug=True)