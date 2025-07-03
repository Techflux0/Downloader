import os
import yt_dlp

def download_audio():
    while True:
        playlist_link = input("Enter the Video Link█ ")
        if playlist_link.lower() == 'exit':
            break

        try:
            download_single_audio(playlist_link)
        except Exception as e:
            print(f"Error: {e}")
            print("Please enter a valid playlist or video URL.")

def download_single_audio(playlist_link):
    def progress_hook(d):
        if d['status'] == 'downloading':
            print(f"Downloading: {d['_percent_str']} at {d['_speed_str']} ETA: {d['_eta_str']}")
        elif d['status'] == 'finished':
            print("Download complete, now converting to MP3...")

    downloads_directory = os.path.join(os.path.expanduser("~"), "Music")  # Changed to Music directory
    os.makedirs(downloads_directory, exist_ok=True)

    def get_playlist_title(url):
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            return info_dict.get('title', 'Downloaded_Audio')

    playlist_title = get_playlist_title(playlist_link)
    safe_playlist_title = "".join([c if c.isalnum() or c in " -_" else "_" for c in playlist_title])
    playlist_directory = os.path.join(downloads_directory, safe_playlist_title)
    os.makedirs(playlist_directory, exist_ok=True)

    # yt-dlp options for audio only
    ydl_opts = {
        'outtmpl': os.path.join(playlist_directory, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',  # Best audio quality only
        'extractaudio': True,       # Extract audio
        'audioformat': 'mp3',       # Convert to MP3
        'postprocessors': [{        # Post-processor to convert to MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  # Highest quality MP3
        }],
        'progress_hooks': [progress_hook],
        'quiet': False,
        'no_warnings': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_link])

    print(f"Audio from '{playlist_title}' downloaded successfully as MP3 files.")

download_audio()