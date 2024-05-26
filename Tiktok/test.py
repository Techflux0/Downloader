from TikTokApi import TikTokApi

# Create an instance of the API
api = TikTokApi()

# Fetch trending videos (if no arguments are required)
trending_videos = api.trending()

# Iterate through the results
for idx, video in enumerate(trending_videos):
    if idx >= 5:  # Limit to 5 videos
        break
    print(video)
