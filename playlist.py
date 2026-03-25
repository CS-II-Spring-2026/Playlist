# PLAYLIST PROGRAM - DICTIONARY ASSESSMENT DANILO VULANOVIC
#  PLAYLIST
#DANILO VULANOVIC

playlist = [

    {"title": "Blinding Lights", "length": "3:20", "category": "Pop", "year": "2020"},
    {"title": "Shape of You", "length": "3:54", "category": "Pop", "year": "2017"},
    {"title": "HUMBLE", "length": "2:57", "category": "Hip Hop", "year": "2017"},
    {"title": "Levitating", "length": "3:23", "category": "Pop", "year": "2020"},
    {"title": "Lose Yourself", "length": "5:26", "category": "Rap", "year": "2002"}

]

# FUNCTION VIEW PLAYLIST
#Printing teh list of songs or actually looking into playlist

def view_playlist():

    print("\nCurrent Playlist:")

    for i, song in enumerate(playlist):
        print(i + 1, "-", song["title"], "|", song["length"], "|", song["category"], "|", song["year"])



# FUNCTION: ADD SONG
#(adding song using input and adding all categories one song need title, lebngth year...)

def add_song():

    title = input("Enter song title: ")
    length = input("Enter song length: ")
    category = input("Enter song category: ")
    year = input("Enter year of the song: ")

    song = {
        "title": title,
        "length": length,
        "category": category,
        "year": year
    }

    playlist.append(song)
    print("Song added successfully.")

# FUNCTION: SEARCH SONG
#(Searching for song by its name and print if exist)

def search_song():

    title = input("Enter song title to search: ")

    for song in playlist:
        if song["title"].lower() == title.lower():
            print("Song found:", song)
            return

    print("Song not found.")


#FUNCTION: DELETE SONG
#Used to delete song from playlist, to remove song that already exist in a playlist

def delete_song():

    title = input("Enter song title to delete: ")

    for song in playlist:
        if song["title"].lower() == title.lower():
            playlist.remove(song)
            print("Song deleted.")
            return

    print("Song not found.")

# FUNCTION: MODIFY SONG
# This is used to modify already existing songs in the playlist edit them their names and all categories that are into the song like title length category and year

def modify_song():

    title = input("Enter song title to modify: ")

    for song in playlist:

        if song["title"].lower() == title.lower():

            song["title"] = input("Enter new title: ")
            song["length"] = input("Enter new length: ")
            song["category"] = input("Enter new category: ")
            song["year"] = input("Enter new year: ")

            print("Song updated.")
            return

    print("Song not found.")




#CALL COMMAND
#This is menu where are commands that are possible called follow instructions to call certain function

while True:

    print("\nPLAYLIST MENU")
    print("1 - View Playlist")
    print("2 - Add Song")
    print("3 - Search Song")
    print("4 - Delete Song")
    print("5 - Modify Song")
    print("6 - Exit")

    choice = input("Enter command number: ")

    if choice == "1":
        view_playlist()

    elif choice == "2":
        add_song()

    elif choice == "3":
        search_song()

    elif choice == "4":
        delete_song()

    elif choice == "5":
        modify_song()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid command. Try again.")
