from flask import Flask, jsonify
from req import request
import json

re = request()
link = re[0]
image = re[1]
video = re[2]
titlee = re[3]

output = [
    {"film": index + 1, "link": link, "image": img ,"video":vide, "titlee":title}
    for index, (link, img , vide , title) in enumerate(zip(link, image , video, titlee))
]

app = Flask(__name__)

@app.route('/')
def home():
    return "سلام! اپ Flask روی Render اجرا شد! 🚀"

@app.route('/users')
def get_users():
    users = output
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)