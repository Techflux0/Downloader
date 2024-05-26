import os
from TikTokApi import TikTokApi
from playwright.sync_api import sync_playwright

# Function to download a TikTok video
def download_tiktok_video(api, link, download_dir):
    try:
        video_id = link.split('/')[-1].split('?')[0]  # Extract the video ID from the link
        video_data = api.video(id=video_id)
        video_url = video_data['video_links'][0]  # Get the first video link
        
        # Download the video content
        video_content = api.get_video_by_download_url(video_url)
        video_filename = os.path.join(download_dir, f"tiktok_video_{video_id}.mp4")
        
        with open(video_filename, 'wb') as f:
            f.write(video_content)
        
        print(f"Video downloaded successfully in {video_filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle user input and downloading process
def main():
    tiktok_link = input("Enter the TikTok video link: ")

    # Set up the download directory
    downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads", "TikTokDownloads")
    os.makedirs(downloads_directory, exist_ok=True)
    
    with sync_playwright() as p:
        api = TikTokApi()
        
        download_tiktok_video(api, tiktok_link, downloads_directory)

if __name__ == "__main__":
    main()
