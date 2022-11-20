<!DOCTYPE html>
<html lang="fr">

<head>
    <!-- Google / Search Engine Tags -->
    <meta itemprop="name" content="iEfrei">
    <meta itemprop="description" content="The DJ has heard you.">
    <meta itemprop="image" content="https://dj.iefrei.fr/assets/images/favicon.png">

    <!-- Facebook Meta Tags -->
    <meta property="og:url" content="https://dj.iefrei.fr">
    <meta property="og:type" content="website">
    <meta property="og:title" content="iEfrei">
    <meta property="og:description" content="The DJ has heard you.">
    <meta property="og:image" content="https://dj.iefrei.fr/assets/images/favicon.png">

    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="iEfrei">
    <meta name="twitter:description" content="The DJ has heard you.">
    <meta name="twitter:image" content="https://dj.iefrei.fr/assets/images/favicon.png">

    <meta charset="utf-8" />
    <meta name="description" content="The DJ has heard you." />
    <meta name="robots" content="all" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iEfrei.fr - DJ Listener</title>
    <link rel="stylesheet" href="styles/index.css">
    <link rel="icon" href="assets/images/favicon.png" />
    <script src="js/index.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
</head>

<body>
    <div class="container">
        <img src="assets/images/bg_3.png" alt="background" width="90%" class="bg">
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