from flask import Flask, request, jsonify, render_template
import requests
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def download_track():
    url = request.json['url']
    output_template = 'downloads/%(title)s.%(ext)s'

    # Construction de la commande pour télécharger le meilleur format audio en mp3
    command = [
        '/usr/local/bin/yt_dlp',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '0',  # Qualité la plus élevée
        '-o', output_template,
        url
    ]

    try:
        # Exécution de la commande yt-dlp
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Vérifier si la commande a réussi
        if process.returncode == 0:
            return jsonify({'status': 'success', 'message': 'Download started'})
        else:
            return jsonify({'status': 'failure', 'message': 'Download failed', 'details': process.stderr})

    except Exception as e:
        return jsonify({'status': 'failure', 'message': str(e)})


def yt_exists(url):
    the_url = f"https://www.youtube.com/oembed?url={url}&format=json"
    response = requests.get(the_url)
    return response.status_code != 404


if __name__ == '__main__':
    app.run(debug=True)
