from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/api/post-blog", methods=['POST'])
def api_post_blog():
    data = request.get_json()
    print(data['title'])
    return 'cool bean yo'

if(__name__ == 'main'):
    app.run()