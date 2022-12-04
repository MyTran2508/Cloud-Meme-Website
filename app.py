#make a virtual envirnment and install all the module 
#import the flask module
from flask import Flask,render_template,request
import requests
import json
import os
app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit
@app.route("/")
def index():
    meme_pic, subreddit =  get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)
if __name__ == '__main__':
    port = int(os.getenv("PORT", 8083))
    app.run(host="0.0.0.0",port = port)

