# 🎵 Billboard to Spotify Time Machine

A Python app that lets you **travel back in time musically**! Enter any date and it scrapes the **Billboard Hot 100** chart for that day, then automatically creates a **private Spotify playlist** with all those songs.

---

## ⚠️ Note on Billboard Scraping

> Billboard's website structure may change over time, which could affect the scraper. If songs are not being fetched correctly, inspect the current HTML structure and update the CSS selector accordingly.

---

## 🚀 Features

- Scrape Billboard Hot 100 for any historical date
- Automatically search each song on Spotify
- Create a private Spotify playlist in your account
- Handles songs not found on Spotify gracefully
- Supports adding 100+ songs in batches

---

## 🛠️ Tech Stack

- Python 3
- BeautifulSoup4 — web scraping
- Requests — HTTP calls
- Spotipy — Spotify Web API wrapper
- Python-dotenv — environment variable management

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/billboard-to-spotify.git
   cd billboard-to-spotify
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   REDIRECT_URI=http://example.com
   ```

---

## ▶️ Usage

```bash
python main.py
```

When prompted, enter a date in `YYYY-MM-DD` format:

```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2000-08-12
```

The app will:
1. Scrape the Billboard Hot 100 for that date
2. Search each song on Spotify
3. Create a private playlist in your Spotify account
4. Add all found songs to the playlist

---

## 🔑 Spotify API Setup

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Copy your `Client ID` and `Client Secret`
4. Add `http://example.com` as a Redirect URI in the app settings
5. Paste all values into your `.env` file

---

## 📄 License

This project is for educational purposes.
