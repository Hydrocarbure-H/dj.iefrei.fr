function processing_link() {
    // check if url is valid (https://youtube.com/watch?v=xxxxx)
    var url = document.getElementById("url").value;
    var button = document.getElementById("launcher");
    var message = document.getElementById("message");

    if (url.match(/^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+/gm)) {
    } else {
        message.innerHTML = "Invalid URL : Try again";
        return;
    }

    button = document.getElementById("launcher");
    button.innerHTML = "Sent to the DJ !";
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
                message.style.backgroundColor = "#4CAF50";
                message.innerHTML = data.message;
                setTimeout(() => { message.innerHTML = "Your video has been added to queue !"; }, 60000);
            }
            if (data.status == "failure") {
                // change button color
                message.style.backgroundColor = "#f44336";
                message.innerHTML = "Error: " + data.message;
                button.innerHTML = "Try again";
            }
        }
    });


}