document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('launcher');
    button.addEventListener('click', function() {
        processing_link();
    });
});

/**
 * Process the link entered by the user
 */
function processing_link() {
    const url = document.getElementById('url').value;
    const message = document.getElementById('message');
    
    if (!isValidYouTubeUrl(url)) {
        message.innerHTML = "Invalid URL : Try again";
        message.style.backgroundColor = "#f44336";
        return;
    }
    
    $.ajax({
        url: '/add',
        type: 'POST',
        data: JSON.stringify({ url: url }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(data) {
            handleResponse(data);
        },
        error: function(xhr, status, error) {
            message.innerHTML = `Error: ${error}`;
            message.style.backgroundColor = "#f44336";
        }
    });
}

/**
 * Check if the given URL is a valid YouTube URL
 * @param url
 * @returns {boolean}
 */
function isValidYouTubeUrl(url) {
    return /^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+/gm.test(url);
}

/**
 * Handle the response from the server
 * @param data
 */
function handleResponse(data) {
    const message = document.getElementById('message');
    const button = document.getElementById('launcher');

    if (data.status === 'success') {
        message.style.backgroundColor = "#4CAF50";
        message.innerHTML = data.message;
        button.innerHTML = "Sent to the DJ !";
        setTimeout(() => {
            message.innerHTML = "Your video has been added to queue !";
        }, 60000);
    } else {
        message.style.backgroundColor = "#f44336";
        message.innerHTML = "Error: " + data.message;
        button.innerHTML = "Try again";
    }
}
