function processing_link() {
    // check if url is valid (https://youtube.com/watch?v=xxxxx)
    url = document.getElementById("url").value;

    if (url.match(/^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+/gm)) {
    } else {
        button = document.getElementById("launcher");
        button.innerHTML = "Invalid URL : Try again";
        return;
    }

    button = document.getElementById("launcher");
    button.innerHTML = "Sending to the DJ...";
    // Send the URL to the server
    $.ajax({
        url: "https://dj.iefrei.fr/api.php?dl_track=true",
        type: "POST",
        data: JSON.stringify({ url: url }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            if (data.status == "success") {
                // change button color
                button.style.backgroundColor = "#4CAF50";
                button.innerHTML = data.message;
            }
            if (data.status == "failure") {
                // change button color
                button.style.backgroundColor = "#f44336";
                button.innerHTML = "Error: " + data.message;
            }
        }
    });


}