import requests
from pytube import YouTube
from flask import Flask, render_template,request,redirect



# readable = time.ctime(1587408140)


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		video_link = request.form['video_link']
		yt = YouTube(video_link)
		print(yt.streams.filter(progressive=True, file_extension='mp4')[-1].download())
		print('downloaded')
		return render_template('index.html')
	else:
		return render_template('error.html')




if __name__ == '__main__':
	app.run(debug=True)