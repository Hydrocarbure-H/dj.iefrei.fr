from flask import Flask, request, jsonify, render_template
import requests
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def download_track():
    data = request.json
    url = data['url']

    # if yt_exists(url):
    #     command = f"youtube-dl -o 'music/%(title)s.%(ext)s' -v -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 '{url}' > /dev/null 2>&1 &"
    #     subprocess.Popen(command, shell=True)
    #     response = {'status': 'success', 'message': 'DJ is now downloading your track...'}
    # else:
    #     response = {'status': 'failure', 'message': 'Video not found'}

    response = {'status': 'success', 'message': 'DJ is now downloading your track...'}

    return jsonify(response)


def yt_exists(url):
    the_url = f"https://www.youtube.com/oembed?url={url}&format=json"
    response = requests.get(the_url)
    return response.status_code != 404


if __name__ == '__main__':
    app.run(debug=True)
