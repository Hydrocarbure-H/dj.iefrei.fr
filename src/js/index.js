function processing_link() {
    button = document.getElementById("launcher");
    button.innerHTML = "Sending to the DJ...";

    url = document.getElementById("url").value;
    // Send the URL to the server
    $.ajax({
        url: "https://dj.iefrei.fr/src/api.php?dl_track=true",
        type: "POST",
        data: JSON.stringify({ url: url }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            if (data.status == "success") {
                // change button color
                button.style.backgroundColor = "#4CAF50";
                button.innerHTML = "Sent to the DJ!";
            }
            else {
                // change button color
                button.style.backgroundColor = "#f44336";
                button.innerHTML = "Error";
            }
        }
    });


}