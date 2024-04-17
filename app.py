import re
from datetime import datetime

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
    match = re.match(r'https?:\/\/(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]+)', url)
    if not match:
        raise ValueError("Invalid YouTube URL provided.")

    video_id = match.group(1)
    full_url = f'https://www.youtube.com/watch?v={video_id}'
    return full_url


@app.route('/')
def index():
    """
    Render the index page.
    :return:
    """
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def download_track():
    """
    Download a track from a YouTube URL.
    :return:
    """
    current_time = datetime.now()
    current_hour = current_time.hour
    current_weekday = current_time.weekday()  # Lundi est 0 et dimanche est 6

    # Vérifiez si nous sommes dans la plage horaire autorisée
    if not (current_weekday == 4 and current_hour >= 20) and not (current_weekday == 5 and current_hour < 3):
        return jsonify(
            {'status': 'failure', 'message': 'Tracks can only be downloaded from Friday 20:00 to Saturday 03:00.'})

    url = request.json['url']
    output_template = 'downloads/%(title)s.%(ext)s'

    # Check if the URL is valid
    pattern = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
    if not re.match(pattern, url):
        return jsonify({'status': 'failure', 'message': 'The URL is invalid !'})

    # Remove the &list=... part of the URL
    if "&list=" in url:
        try:
            url = convert_short_youtube_url_to_full(url.split('&list=')[0])
        except ValueError:
            return jsonify({'status': 'failure', 'message': 'This URL format is not currently supported. Try with a '
                                                            'format like the following one: '
                                                            'https://youtu.be/TGMJRnUbwwo'})

    if "?list=" in url:
        try:
            url = convert_short_youtube_url_to_full(url.split('?list=')[0])
        except ValueError:
            return jsonify({'status': 'failure', 'message': 'This URL format is not currently supported. Try with a '
                                                            'format like the following one: '
                                                            'https://youtu.be/TGMJRnUbwwo'})

    # Create the command to download the track
    command = [
        '/usr/local/bin/yt_dlp',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '0',
        '-o', output_template,
        url
    ]

    # Download the track
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

            return jsonify({'status': 'failure', 'message': 'Download failed. This software still'
                                                            ' in beta version, sorry ! You can try again '
                                                            'with another track.'})

    except Exception as e:

        if "[ExtractAudio] Destination:" in process.stderr:
            return jsonify({'status': 'success', 'message': 'Your track has been downloaded successfully !'})

        # print(e)
        # print(process.stderr)
        # print(process.stdout)

        return jsonify({'status': 'failure', 'message': "An error occurred while downloading the track. Maybe the"
                                                        " URL is invalid or the track is not available for download."})


if __name__ == '__main__':
    app.run(debug=True)
