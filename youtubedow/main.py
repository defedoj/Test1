from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/download",methods = ["POST"])
def download_video():
    url = request.form['url']
    try:
       yt = YouTube(url)
       stream = yt.streams.get_highest_resolution()
       stream.download(output_path="downloads",filename="video.mp4")
       return send_file(os.path.join("downloads","video.mp4"), as_attachment=True)
    except Exception as e:
       return f"An error name:{str(e)}"
    

if __name__ == "__main__":
   app.run(debug=True)



