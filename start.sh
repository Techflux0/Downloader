#!/bin/bash

if ! command -v figlet &> /dev/null; then
    echo "figlet is not installed. Installing..."
    sudo apt-get install -y figlet
fi

while true; do
    clear
    figlet "Downloader"
    
    echo "Select an option:"
    echo "1. YouTube"
    echo "2. Instagram"
    echo "3. TikTok"
    read -p "Enter your choice (1/2/3): " choice

    case $choice in
        1)
            figlet "YouTube"
            echo "You chose YouTube."
            python Youtube/ytube.py
            ;;
        2)
            figlet "Instagram"
            echo "You chose Instagram."
            python Instagram/insta.py
            ;;
        3)
            figlet "TikTok"
            echo "You chose TikTok."
            python Tiktok/main.py
            ;;
        *)
            figlet "Error"
            echo "Invalid choice. Please choose a number between 1 and 3."
            continue
            ;;
    esac

    # Ask the user if they want to continue
    read -p "Do you want to continue? (y/n): " answer
    if [ "$answer" != "y" ]; then
        break
    fi
done
