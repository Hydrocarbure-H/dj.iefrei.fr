<!DOCTYPE html>
<html lang="fr">

<head>
    <!-- Google / Search Engine Tags -->
    <meta itemprop="name" content="iEfrei">
    <meta itemprop="description" content="iEfrei est un site Internet permettant aux étudiants d'uploader leurs prises de notes et de se les partager. Thomas Peugnet.">
    <meta itemprop="image" content="https://iefrei.fr/public/images/logo_efrei-rounded.png">

    <!-- Facebook Meta Tags -->
    <meta property="og:url" content="https://iefrei.fr">
    <meta property="og:type" content="website">
    <meta property="og:title" content="iEfrei">
    <meta property="og:description" content="iEfrei est un site Internet permettant aux étudiants d'uploader leurs prises de notes et de se les partager. Thomas Peugnet.">
    <meta property="og:image" content="https://iefrei.fr/public/images/logo_efrei-rounded.png">

    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="iEfrei">
    <meta name="twitter:description" content="iEfrei est un site Internet permettant aux étudiants d'uploader leurs prises de notes et de se les partager. Thomas Peugnet.">
    <meta name="twitter:image" content="https://iefrei.fr/public/images/logo_efrei-rounded.png">

    <meta charset="utf-8" />
    <meta name="description" content="iEfrei est un site Internet permettant aux étudiants d'uploader leurs prises de notes et de se les partager. Thomas Peugnet." />
    <meta name="keywords" content="iefrei,efrei,epita,paris,cours,lessons,leçons,nots,notes de cours">
    <meta name="robots" content="all" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <title>iEfrei.fr - DJ Listener</title>
    <link rel="stylesheet" href="index.css">
    <link rel="icon" href="favicon.png" />
    <script src="index.js"></script>

</head>

<body>
    <!-- Do an input interface to put a link -->
    <div class="container">
        <img src="bg_3.png" alt="background" width="90%" class="bg">
        <div class="title">
            <h1>iEfrei.fr</h1>
            <h2>DJ Listener</h2>
        </div>
        <div class="input">
            <?php
            display();
            ?>
        </div>
</body>

</html>

<?php
function display()
{
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE))
    {
        echo "<div class='error'>You need to be connected to the WIFI.</div>";
    }
    else
    {
        printf('<input type="text" id="url" placeholder="Enter any Youtube Url...">
            <a class="btn" id="launcher" onclick="processing_link()">Send to the DJ</a>"');
    }
}
?>