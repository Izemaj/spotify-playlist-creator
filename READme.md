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
    <h1>How the Script Works</h1>
    <ol>
      <li>The script starts by importing the necessary libraries: datetime, requests, BeautifulSoup, and spotipy.</li>
      <li>The script prompts the user to enter a date in the format YYYY-MM-DD.</li>
      <li>The script validates the user input and ensures that the entered date is not in the future.</li>
      <li>The script constructs a URL to scrape the Billboard website for the Top 100 songs on the entered date.</li>
      <li>The script sends a GET request to the URL using the requests library and parses the HTML content of the page using BeautifulSoup.</li>
      <li>The script extracts the names of the top 100 songs from the parsed HTML using BeautifulSoup selectors.</li>
      <li>The script logs into Spotify using the SpotifyOAuth class from the spotipy library, which authenticates the user and generates an access token for the Spotify Web API.</li>
      <li>The script retrieves the user ID of the logged-in user from the Spotify Web API.</li>
      <li>The script searches Spotify for each song extracted from the Billboard website using the Spotify Web API and adds the found songs to a list of song URIs.</li>
      <li>The script creates a new private Spotify playlist with the name "{date} Billboard 100" using the Spotify Web API and adds the found songs to it using the playlist_add_items() method from the spotipy library.</li>
      <li>The script completes execution, and the user can access the new Spotify playlist with the name "{date} Billboard 100".</li>
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