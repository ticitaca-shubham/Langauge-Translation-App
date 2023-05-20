from flask import render_template,Flask

app = Flask(__name__)

@app.route('/', methods=[ 'GET'])
def hello():
    return render_template('index.html')