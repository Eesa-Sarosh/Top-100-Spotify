# Top-100-Spotify
This Python code scrapes the top 100 songs from the Billboard Hot 100 chart for a specific date and creates a playlist of those songs in the user's Spotify account.

## Dependencies

- BeautifulSoup: Python library for web scraping
- Spotipy: Python library for the Spotify Web API

Note: You will need a Spotify account and valid credentials (client ID and client secret) to use this code.

## How It Works

1. The code prompts the user to input a specific date in the "YYYY-MM-DD" format to scrape the Billboard chart for that day.

2. It sends an HTTP request to the Billboard website (https://www.billboard.com/charts/hot-100/{date}) and retrieves the HTML content.

3. The BeautifulSoup library is used to parse the HTML content and extract the song titles from the chart.

4. The code utilizes the Spotipy library and SpotifyOAuth authentication to create a connection with the Spotify API.

5. For each song title obtained from the Billboard chart, the code searches for the corresponding track on Spotify, filtered by the specified year.

6. If a matching track is found, its URI (Uniform Resource Identifier) is extracted and added to a list of song URIs.

7. The code creates a private playlist on the user's Spotify account named "{date} Billboard 100" using the Spotify user ID.

8. It adds the collected song URIs to the created playlist using the `playlist_add_items` method.

## Instructions

1. Install the required dependencies: BeautifulSoup and Spotipy.

2. Obtain Spotify API credentials (client ID and client secret) from the Spotify Developer Dashboard.

3. Update the `clientID` and `clientSecret` variables in the code with your Spotify API credentials.

4. Run the code and follow the prompts to enter the desired date in the "YYYY-MM-DD" format.

5. The code will scrape the Billboard chart, search for the songs on Spotify, and create a playlist in your Spotify account.

## Acknowledgments

- This code is inspired by the Spotify API and web scraping tutorials.

