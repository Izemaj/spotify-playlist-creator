<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Billboard Top 100 Playlist Creator</title>
</head>
<body>
    <h1>Billboard Top 100 Playlist Creator</h1>
    <p>This Python script creates a Spotify playlist of the Billboard Top 100 songs for a specified date. The user is prompted to enter a date in the format YYYY-MM-DD, and the script scrapes the Billboard website for the top 100 songs on that date. The script then searches Spotify for each song and adds the songs that are found to a new playlist, which is named after the specified date.</p>
    <h2>Usage Instructions</h2>
    <ol>
        <li>Replace "REPLACE WITH YOUR CLIENT ID" and "REPLACE WITH YOUR CLIENT SECRET" with your actual Spotify client ID and secret in the Python script.</li>
        <li>Run the Python script and enter a date when prompted.</li>
        <li>The script will create a new private Spotify playlist with the name "{date} Billboard 100" and add the found songs to it.</li>
    </ol>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.7 or higher</li>
        <li>requests library</li>
        <li>BeautifulSoup4 library</li>
        <li>spotipy library</li>
    </ul>
    <h2>Disclaimer</h2>
    <p>This project is for educational purposes only. The authors do not endorse or condone any copyright infringement or illegal use of Spotify or Billboard data.</p>
</body>
</html>