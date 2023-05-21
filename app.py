from flask import render_template,Flask, request
import requests, os, uuid, json


app = Flask(__name__)

@app.route('/', methods=[ 'GET'])
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Read the value from the form
    original_text = request.form['text']
    target_language = request.form['langauge']

    url = os.environ['URL']

    payload = {
        "q": original_text,
        "target": target_language,
        "source": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "61eb7bb9c6msh97b9f60b8d79b9fp167b14jsneebb81eb3189",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    response = response.json()

    translated_text = response['data']['translations'][0]['translatedText']

    return render_template(
        'result.html',
        original_text = original_text,
        translated_text = translated_text,
        target_language = target_language
    )