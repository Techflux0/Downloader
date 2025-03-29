import os
import yt_dlp

def download_playlist():
    while True:
        playlist_link = input("Enter the playlist link or Video Link(or type 'exit' to quit): ")
        if playlist_link.lower() == 'exit':
            break  

        try:
          
            download_single_playlist(playlist_link)
        except Exception as e:
            print(f"Error: {e}")
            print("Please enter a valid playlist URL.")

def download_single_playlist(playlist_link):
    def progress_hook(d):
        if d['status'] == 'downloading':
            print(f"Downloading: {d['_percent_str']} at {d['_speed_str']} ETA: {d['_eta_str']}")
        elif d['status'] == 'finished':
            print("Download complete, now converting...")

    downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(downloads_directory, exist_ok=True)

    def get_playlist_title(url):
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            return info_dict.get('title', 'Downloaded_Playlist')

    playlist_title = get_playlist_title(playlist_link)

    safe_playlist_title = "".join([c if c.isalnum() or c in " -_" else "_" for c in playlist_title])
    playlist_directory = os.path.join(downloads_directory, safe_playlist_title)
    os.makedirs(playlist_directory, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(playlist_directory, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_link])

    print(f"Playlist '{playlist_title}' downloaded and merged successfully.")
download_playlist()
