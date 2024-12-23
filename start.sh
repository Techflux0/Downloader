#!/bin/bash

command_exists() {
    command -v "$1" &> /dev/null
}


# function print_banner() {
#     clear
#     echo -e "${blue}##################################################\n"
#     echo -e "${blue}##                                              ##\n"
#     echo -e "${blue}##  88      a8P         db        88        88  ##\n"
#     echo -e "${blue}##  88    .88'         d88b       88        88  ##\n"
#     echo -e "${blue}##  88   88'          d8''8b      88        88  ##\n"
#     echo -e "${blue}##  88 d88           d8'  '8b     88        88  ##\n"
#     echo -e "${blue}##  8888'88.        d8YaaaaY8b    88        88  ##\n"
#     echo -e "${blue}##  88P   Y8b      d8''''''''8b   88        88  ##\n"
#     echo -e "${blue}##  88     '88.   d8'        '8b  88        88  ##\n"
#     echo -e "${blue}##  88       Y8b d8'          '8b 888888888 88  ##\n"
#     echo -e "${blue}##                                              ##\n"
#     echo -e "${blue}####  ############# NetHunter ####################${reset}\n\n"
# }



if ! command_exists figlet; then
    echo "figlet is not installed. Installing..."
    sudo apt-get install -y figlet
fi

# Check if Python is installed
if ! command_exists python3; then
    echo "Python is not installed! Please install Python and try again."
    exit 1
fi

# Check if pip is installed
if ! command_exists pip3; then
    echo "pip is not installed. Installing..."
    sudo apt-get install -y python3-pip
fi

# Install yt_dlp
if ! python3 -c "import yt_dlp" &> /dev/null; then
    echo "yt_dlp is not installed. Installing..."
    if [[ "$(uname -s)" == "Linux" ]]; then
        sudo pip3 install yt_dlp --break-system-packages
    else
        pip3 install yt_dlp
    fi
fi

while true; do
    clear
   # print_banner
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
           # python3 Youtube/ytube.py
           python3 ydlp.py
            ;;
        2)
            figlet "Instagram"
            echo "You chose Instagram."
            python3 Instagram/insta.py
            ;;
        3)
            figlet "TikTok"
            echo "You chose TikTok."
            python3 Tiktok/main.py
            ;;
        *)
            figlet "Error"
            echo "Invalid choice. Please choose a number between 1 and 3."
            continue
            ;;
    esac

    read -p "Do you want to continue? (y/n): " answer
    if [ "$answer" != "y" ]; then
        break
    fi
done
