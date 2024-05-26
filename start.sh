#!/bin/bash

echo "Select an option:"
echo "1. YouTube"
echo "2. Instagram"
echo "3. TikTok"
read -p "Enter your choice (1/2/3): " choice

case $choice in
    1)
        echo "You chose YouTube."
        python Youtube/ytube.py
        ;;
    2)
        echo "You chose Instagram."
        python Instagram/insta.py
        ;;
    3)
        echo "You chose TikTok."
        python Tiktok/main.py
        ;;
    *)
        echo "Invalid choice."
        ;;
esac
