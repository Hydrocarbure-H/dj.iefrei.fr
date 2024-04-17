import re

from flask import Flask, request, jsonify, render_template
import requests
import subprocess

app = Flask(__name__)


def convert_short_youtube_url_to_full(url):
    """
    Converts a shortened YouTube URL to a full YouTube URL.

    Args:
    url (str): The shortened YouTube URL (e.g., https://youtu.be/ozthKn07Ei4).

    Returns:
    str: The full YouTube URL (e.g., https://www.youtube.com/watch?v=ozthKn07Ei4).
    """

    # Check if the URL is a valid shortened YouTube URL
    match = re.match(r'(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?/([a-zA-Z0-9_-]+)', url)
    if not match:
        raise ValueError("Invalid YouTube URL provided.")

    video_id = match.group(7)
    full_url = f'https://www.youtube.com/watch?v={video_id}'
    return full_url


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def download_track():
    url = request.json['url']
    output_template = 'downloads/%(title)s.%(ext)s'

    # Check if the URL is valid     pattern = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
    pattern = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
    if not re.match(pattern, url):
        return jsonify({'status': 'failure', 'message': 'The URL is invalid !'})

    # Remove the &list=... part of the URL
    if "&list=" in url:
        url = convert_short_youtube_url_to_full(url.split('&list=')[0])

    if "?list=" in url:
        url = convert_short_youtube_url_to_full(url.split('?list=')[0])

    print(url)

    command = [
        '/usr/local/bin/yt_dlp',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '0',
        '-o', output_template,
        url
    ]

    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Wait for the process to finish
        process.check_returncode()

        if process.returncode == 0:
            # Check if the song has already been downloaded
            if 'already' in process.stderr or 'already' in process.stdout:
                return jsonify({'status': 'warning', 'message': 'This track has already been downloaded !'})

            return jsonify({'status': 'success', 'message': 'Your track has been downloaded successfully !'})
        else:
            # Check if the song has already been downloaded
            if 'already' in process.stderr:
                return jsonify({'status': 'failure', 'message': 'This track has already been downloaded !'})

            print(process.stderr)
            return jsonify({'status': 'failure', 'message': 'Download failed. This software still'
                                                            ' in beta version, sorry ! You can try again '
                                                            'with another track.'})

    except Exception as e:
        print(e)
        return jsonify({'status': 'failure', 'message': "An error occurred while downloading the track."})


def yt_exists(url):
    the_url = f"https://www.youtube.com/oembed?url={url}&format=json"
    response = requests.get(the_url)
    return response.status_code != 404


if __name__ == '__main__':
    app.run(debug=True)
