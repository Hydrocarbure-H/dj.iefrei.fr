<?php
// display errors
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
if (isset($_GET["dl_track"]) && $_GET["dl_track"] == "true")
{
    $data = json_decode(file_get_contents('php://input'), true);

    $link = $data["url"];
    // check this is a valid youtube.com url
    // if (strpos($link, "https://www.youtube.com") == false)
    // {
    //     echo "Invalid url";
    //     return;
    // }

    // Check if the music exists 

    if (yt_exists($link))
    {
        $command = "youtube-dl -o \"music/%(title)s.%(ext)s\" -v -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 \"" . $link . "\" > /dev/null 2>&1 &";
        $output = null;
        $retval = null;
        // run command in background
        exec($command, $output, $retval);

        $response = array(
            'status' => "success", 'message' => "DJ is now downloading your track..."
        );
    }
    else
    {
        $response = array(
            'status' => "failure", 'message' => "Video not found"
        );
    }

    $json_repsonse = json_encode($response);

    echo $json_repsonse;
}


function yt_exists($url)
{
    $theURL = "https://www.youtube.com/oembed?url=" . $url . "&format=json";
    $headers = get_headers($theURL);

    return (substr($headers[0], 9, 3) !== "404");
}
