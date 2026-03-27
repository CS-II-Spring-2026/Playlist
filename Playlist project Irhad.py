# playlist
playList = {
    'Band 4 Band': {'artist': 'Central Cee', 'Year': 2022},
    'Loading': {'artist': 'Central Cee', 'Year': 2021},
    'No Introduction': {'artist': 'Central Cee', 'Year': 2025},
    'GBP': {'artist': 'Central Cee', 'Year': 2025},
    'Truth in the Lies': {'artist': 'Central Cee', 'Year': 2025},
    'Gen Z Luv': {'artist': 'Central Cee', 'Year': 2025},
    'Gata': {'artist': 'Central Cee', 'Year': 2025},
    'Up North': {'artist': 'Central Cee', 'Year': 2025},
    'Sprinter': {'artist': 'Central Cee', 'Year': 2023},
    '6 for 6': {'artist': 'Central Cee', 'Year': 2021},
}

# Function to add a song
def addSong():
    song = input("Enter song name: ")
    artist = input("Enter artist name: ")
    year = int(input("Enter song year: "))

    playList[song] = {'artist': artist, 'Year': year}
    print("Song added.\n")

# Function to delete a song
def deleteSong():
    song = input("What is the song name you want to delete?: ")

    if song in playList:
        del playList[song]
        print("Song deleted.\n")
    else:
        print("Song not found in playlist.\n")

# Function to view playlist
def viewPlaylist():
    print("\n---- Current Playlist ----")

    for song, info in playList.items():
        print(f"{song} by {info['artist']} ({info['Year']})")
    print()

# Function to search
def searchSong():
    query = input("Enter song name or artist to search: ").lower()
    found = False

    print("\n---- Search Results ----")

    for song, info in playList.items():
        if query in song.lower() or query in info['artist'].lower():
            print(f"{song} by {info['artist']} ({info['Year']})")
            found = True

    if not found:
        print("No matching songs found.")
    print()

# Main menu loop
flag = True

while flag:
    print("---- Playlist Menu ----")
    print("1: Add a song")
    print("2: Delete a song")
    print("3: View playlist")
    print("4: Search for a song")
    print("5: Quit")

    selection = input("Enter your choice: ")

    if selection == "1":
        addSong()
    elif selection == "2":
        deleteSong()
    elif selection == "3":
        viewPlaylist()
    elif selection == "4":
        searchSong()
    elif selection == "5":
        flag = False
        print("See ya")
    else:
        print("Invalid choice. Try again.\n")