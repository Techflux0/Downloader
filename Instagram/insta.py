import os
import instaloader

instagram_link = input("Enter the Instagram link: ")

L = instaloader.Instaloader()
downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads", "InstagramDownloads")

os.makedirs(downloads_directory, exist_ok=True)

os.chdir(downloads_directory)

def get_shortcode(link):
    if 'instagram.com/p/' in link:
        return link.split('/p/')[1].split('/')[0]
    elif 'instagram.com/tv/' in link:
        return link.split('/tv/')[1].split('/')[0]
    elif 'instagram.com/reel/' in link:
        return link.split('/reel/')[1].split('/')[0]
    else:
        raise ValueError("Invalid Instagram URL")

# Main function
def main():
    try:
        shortcode = get_shortcode(instagram_link)
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        if post.typename == "GraphVideo":
            L.download_post(post, target=downloads_directory)
            print(f"Video downloaded successfully in {downloads_directory}.")
        else:
            print("No video found in the provided link.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
