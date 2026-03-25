# Dictionary that stores the songs in the playlist
# Each song has an artist, length, and genre
Song_list = {
    "EARFQUAKE": {'Artist': "Tyler the creator", 'length': "3:10", 'genre': "Alternative Hip-Hop"},
    "Took her to the O": {'Artist': "King Von", 'length': "3:16", 'genre': "Drill/Hip Hop"},
    "Gods plan": {'Artist': "Drake", 'length': "3:18", 'genre': "Hip Hop/Rap"},
}

# Function to add a song to the playlist
def addSong():
    # Ask the user for song info
    song = input("Enter song name: ")
    artist = input("Enter artist name: ")
    length = input("Enter song length (mm:ss): ")
    genre = input("Enter song genre: ")

    # Add the song to the dictionary
    Song_list[song] = {'Artist': artist, 'length': length, 'genre': genre}

    # Confirm to the user that the song was added
    print("Song added!")

# Function to delete a song from the playlist
def deleteSong():
    # Ask the user which song they want to delete
    song = input("Enter the song name you want to delete: ")

    # Check if the song exists in the playlist
    if song in Song_list:
        del Song_list[song]  # Remove the song from the dictionary
        print("Song deleted!")
    else:
        # If the song isn't in the playlist, tell the user
        print("Song not found in playlist.")

# Function to view all songs in the playlist
def viewPlaylist():
    print("\n---- Current Playlist ----")

    # Loop through each song and print its details
    for song in Song_list:
        print(song, "-", Song_list[song]['Artist'], "-", Song_list[song]['length'], "-", Song_list[song]['genre'])
    print()  # Add a blank line for spacing

# Function to search for songs by name, artist, or genre
def searchSong():
    # Ask user for search query and convert to lowercase for easier matching
    query = input("Enter song name, artist, or genre to search: ").lower()
    found = False  # Track if any matching songs are found
    print("\n---- Search Results ----")

    # Loop through all songs and check if query matches song name, artist, or genre
    for song, info in Song_list.items():
        if query in song.lower() or query in info['Artist'].lower() or query in info['genre'].lower():
            print(song, "-", info['Artist'], "-", info['length'], "-", info['genre'])
            found = True

    # If no matches were found, tell the user
    if not found:
        print("No matching songs found.")
    print()  # Add blank line for spacing

# Keep the menu running until the user chooses to quit
flag = True

# Main menu loop
while flag:
    # Display menu options
    print("---- Playlist Menu ----")
    print("1: Add a song")
    print("2: Delete a song")
    print("3: View playlist")
    print("4: Search for a song")
    print("5: Quit")

    # Get user choice
    selection = input("Enter your choice: ")

    # Run functions depending on user's selection
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
        print("Bye!")  # Exit message
    else:
        # Handle invalid input
        print("Invalid choice. Try again.")