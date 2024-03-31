from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/api/post-blog", methods=['POST'])
def api_post_blog():
    header = request.headers
    data = request.get_json()
    print(data['title'], flush=True)
    print(header['Content-Type'], flush=True)
    return 'got it'

@app.route("/api/checkpoint", methods=['GET'])
def get_checkpoint():
    
    with open('variable.txt', 'r') as f:
        return f.read().strip()
    
@app.route("/api/set-checkpoint/<checkpoint>", methods=['POST'])
def set_checkpoint(checkpoint):
    
    with open('variable.txt', 'w') as f:
        f.write(str(checkpoint))
    return checkpoint

if(__name__ == 'main'):
    app.run()