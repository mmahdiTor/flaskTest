from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "سلام! اپ Flask روی Render اجرا شد! 🚀"

@app.route('/users')
def get_users():
    users = [
        {"id": 1, "name": "علی"},
        {"id": 2, "name": "زهرا"},
        {"id": 3, "name": "محمد"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)