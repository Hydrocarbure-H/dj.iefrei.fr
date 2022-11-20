<?php

// check endpoint
// dl music by execute command
// rsync music from client (windows) every 1 min
$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
printf("IP : " . $ip);
if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE))
{
    if (isset($_GET["dl_track"]) && $_GET["dl_track"] == "true")
    {
        $data = json_decode(file_get_contents('php://input'), true);

        $link = $data["url"];
        // check this is a valid youtube.com url
        if (strpos($link, "youtube.com") == false)
        {
            echo "Invalid url";
            return;
        }
        // exec the command to download the music
        //shell_exec("youtube-dl -o '/home/thomas/temp_dj/%(title)s.%(ext)s' -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 ".$link);
        $your_command = "youtube-dl -o '/home/thomas/temp_dj/%(title)s.%(ext)s' -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 '" . $link . "'";
        printf($your_command);
        exec($your_command, $output, $return_var);
        var_dump($output);
        var_dump($return_var);
        printf("OK");
        // exec command to move it inside the temporary rep
    }
}
